import unittest
from unittest.mock import mock_open, patch
from dna_analysis.utils.validators import validar_dna_sequence, validar_fasta

class TestValidators(unittest.TestCase):
    def test_validar_dna_sequence(self):
        self.assertTrue(validar_dna_sequence("ATGCGT"))
        self.assertFalse(validar_dna_sequence("ATGXYZ"))

    def test_validar_fasta(self):
        valid_fasta_content = """>TestSequence
        ATGCGTATGCGTATGCGTATGCGT
        """
        invalid_fasta_content = "ATGCGTATGCGTATGCGTATGCGT"

        with patch("builtins.open", mock_open(read_data=valid_fasta_content)):
            self.assertTrue(validar_fasta("dummy_path.fasta"))

        with patch("builtins.open", mock_open(read_data=invalid_fasta_content)):
            self.assertFalse(validar_fasta("dummy_path.fasta"))

if __name__ == '__main__':
    unittest.main()