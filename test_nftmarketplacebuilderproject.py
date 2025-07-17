# test_nftmarketplacebuilderproject.py
"""
Tests for NftMarketplaceBuilderProject module.
"""

import unittest
from nftmarketplacebuilderproject import NftMarketplaceBuilderProject

class TestNftMarketplaceBuilderProject(unittest.TestCase):
    """Test cases for NftMarketplaceBuilderProject class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMarketplaceBuilderProject()
        self.assertIsInstance(instance, NftMarketplaceBuilderProject)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMarketplaceBuilderProject()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
