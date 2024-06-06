import unittest
from collections import defaultdict
import sys 
import argparse
sys.path.append("C:/Users/pdmpe/Desktop/ProyectoPython/dna_analysis/")

from dna_analysis.operations.codon_frecuency import extraer_secuencia_fasta, contar_codones, calcular_frecuencias

class TestCodonFrequency(unittest.TestCase):
    def test_contar_codones(self):
        sequence = "ATGCGTATGCGTATGCGT"
        expected_codons = defaultdict(int, {"ATG": 3, "CGT": 3})
        expected_total_codons = 6
        codons, total_codons = contar_codones(sequence)
        self.assertEqual(codons, expected_codons)
        self.assertEqual(total_codons, expected_total_codons)

    def test_calcular_frecuencias(self):
        codons = {"ATG": 3, "CGT": 3}
        total_codons = 6
        expected_frequencies = {"ATG": 0.5, "CGT": 0.5}
        frequencies = calcular_frecuencias(codons, total_codons)
        self.assertEqual(frequencies, expected_frequencies)

if __name__ == '__main__':
    unittest.main()