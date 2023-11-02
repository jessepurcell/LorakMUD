# """Zone class
# Holds the tile data and helper functions for translating between world and grid coordinates.
# """
#
#
# class Zone:
#     """Zone class."""
#
#     def __init__(self, filepath):
#         """Initialize zone."""
#         self.filepath = filepath
#         self.tiles = []
#         self.load(filepath)
#
#     def load(self, filepath):
#         """Loads zone in from the given file.
#         Format: JSON?
#         """
#         test_data = [0, 0, 0, 0, 0, 0, 0,
#                      0, 1, 1, 0, 0, 0, 0,
#                      0, 1, 0, 0, 0, 0, 0,
#                      0, 0, 0, 1, 1, 0, 0,
#                      0, 0, 0, 0, 0, 0, 0,
#                      0, 0, 0, 0, 0, 0, 0,
#                      0, 0, 0, 0, 0, 0, 0]
#         for data in test_data:
#             break
