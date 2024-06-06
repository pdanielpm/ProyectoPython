import argparse
import unittest
from io import StringIO
from unittest.mock import patch, mock_open
from dna_analysis.scripts.main import main

class TestMain(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=">TestSequence\nATGCGTATGCGTATGCGTATGCGT")
    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file='dummy_path.fasta'))
    def test_main(self, mock_args, mock_stdout, mock_file):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Secuencia de ADN extraída", output)
        self.assertIn("Frecuencia de codones", output)
        self.assertIn("Secuencia de ADN para TestSequence", output)
        self.assertIn("Frame 1 (5' to 3')", output)
        self.assertIn("Frame 4 (3' to 5')", output)

    @patch('builtins.open', new_callable=mock_open, read_data="ATGCGTATGCGTATGCGTATGCGT")
    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file='invalid_fasta.fasta'))
    def test_invalid_fasta(self, mock_args, mock_stdout, mock_file):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: El archivo 'invalid_fasta.fasta' no tiene formato FASTA válido.", output)

    @patch('builtins.open', new_callable=mock_open, read_data=">TestSequence\nATGXYZ")
    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(file='invalid_dna.fasta'))
    def test_invalid_dna_sequence(self, mock_args, mock_stdout, mock_file):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Error: La secuencia de ADN 'ATGXYZ' contiene caracteres no válidos.", output)

if __name__ == '__main__':
    unittest.main()

