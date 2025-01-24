import unittest
import six

from nd2reader.artificial import ArtificialND2
from nd2reader.label_map import LabelMap
from nd2reader.raw_metadata import RawMetadata
from nd2reader.common_raw_metadata import parse_roi_shape, parse_roi_type, parse_dimension_text_line


class TestRawMetadata(unittest.TestCase):
    def setUp(self):
        self.nd2 = ArtificialND2('test_data/test_nd2_raw_metadata001.nd2')
        self.raw_text, self.locations, self.file_data = self.nd2.raw_text, self.nd2.locations, self.nd2.data
        self.label_map = LabelMap(self.raw_text)
        self.metadata = RawMetadata(self.nd2.file_handle, self.label_map)

    def test_parse_roi_shape(self):
        self.assertEqual(parse_roi_shape(3), 'rectangle')
        self.assertEqual(parse_roi_shape(9), 'circle')
        self.assertIsNone(parse_roi_shape(-1))

    def test_parse_roi_type(self):
        self.assertEqual(parse_roi_type(3), 'reference')
        self.assertEqual(parse_roi_type(2), 'background')
        self.assertEqual(parse_roi_type(4), 'stimulation')
        self.assertIsNone(parse_roi_type(-1))

    def test_parse_dimension_text(self):
        line = six.b('Metadata:\r\nDimensions: T(443) x \xce\xbb(1)\r\nCamera Name: Andor Zyla VSC-01537')
        self.assertEqual(parse_dimension_text_line(line), six.b('Dimensions: T(443) x \xce\xbb(1)'))
        self.assertIsNone(parse_dimension_text_line(six.b('Dim: nothing')))

    def test_parse_z_levels(self):
        # smokescreen test to check if the fallback to z_coordinates is working
        # for details, see RawMetadata._parse_z_levels()
        dimension_text = self.metadata._parse_dimension_text()
        z_levels = self.metadata._parse_dimension(r""".*?Z\((\d+)\).*?""", dimension_text)
        z_coords = self.metadata._parse_z_coordinates()

        self.assertEqual(len(dimension_text), 0)
        self.assertEqual(len(z_levels), 0)
        self.assertEqual(len(self.metadata._parse_z_levels()), len(z_coords))

    def test_dict(self):
        self.assertTrue(type(self.metadata.__dict__) is dict)

    def test_parsed_metadata_has_all_keys(self):
        metadata = self.metadata.get_parsed_metadata()
        self.assertTrue(type(metadata) is dict)
        required_keys = ["height", "width", "date", "fields_of_view", "frames", "z_levels", "total_images_per_channel",
                         "channels", "pixel_microns"]
        for required in required_keys:
            self.assertTrue(required in metadata)

    def test_cached_metadata(self):
        metadata_one = self.metadata.get_parsed_metadata()
        metadata_two = self.metadata.get_parsed_metadata()
        self.assertEqual(metadata_one, metadata_two)

    def test_pfs_status(self):
        self.assertEqual(self.file_data['pfs_status'], self.metadata.pfs_status[0])

    def _assert_dicts_equal(self, parsed_dict, original_dict):
        for attribute in original_dict.keys():
            parsed_key = six.b(attribute)
            self.assertIn(parsed_key, parsed_dict.keys())

            if isinstance(parsed_dict[parsed_key], dict):
                self._assert_dicts_equal(parsed_dict[parsed_key], original_dict[attribute])
            else:
                self.assertEqual(parsed_dict[parsed_key], original_dict[attribute])

    def test_image_attributes(self):
        parsed_dict = self.metadata.image_attributes

        self._assert_dicts_equal(parsed_dict, self.file_data['image_attributes'])

    def test_color_channels(self):
        parsed_channels = self.metadata.get_parsed_metadata()['channels']

        self.assertEquals(parsed_channels, ['TRITC'])
