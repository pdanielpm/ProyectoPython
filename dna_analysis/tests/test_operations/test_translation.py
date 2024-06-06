from io import StringIO, SeqIO

from unittest.mock import patch
from Bio.Seq import Seq
import unittest
from collections import defaultdict
import sys 
import argparse
sys.path.append("C:/Users/pdmpe/Desktop/ProyectoPython/dna_analysis/")
from dna_analysis.operations.translate_dna import translate_all_frames

class TestTranslation(unittest.TestCase):
    def test_translate_frames(self):
        sequence = Seq("ATGCGT")
        expected_frames = {
            "Frame 1 (5' to 3')": "MR",
            "Frame 2 (5' to 3')": "C",
            "Frame 3 (5' to 3')": "A",
            "Frame 4 (3' to 5')": "CR",
            "Frame 5 (3' to 5')": "A",
            "Frame 6 (3' to 5')": "T"
        }
        frames = translate_all_frames(sequence)
        self.assertEqual(frames, expected_frames)

    @patch('sys.stdout', new_callable=StringIO)
    def test_translate_all_frames(self, mock_stdout):
        fasta_data = """>TestSequence
        ATGCGTATGCGTATGCGTATGCGT
        """
        with patch('dna_analysis.operations.translation.SeqIO.parse', return_value=[SeqIO.SeqRecord(Seq("ATGCGTATGCGTATGCGTATGCGT"), id="TestSequence")]):
            translate_all_frames("dummy_path.fasta")
            output = mock_stdout.getvalue()
            self.assertIn("Secuencia de ADN para TestSequence", output)
            self.assertIn("Frame 1 (5' to 3')", output)
            self.assertIn("Frame 4 (3' to 5')", output)

if __name__ == '__main__':
    unittest.main()