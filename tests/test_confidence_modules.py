from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
INDEX = (ROOT / 'index.html').read_text()
APP = (ROOT / 'app.js').read_text()


class ConfidenceModulesTest(unittest.TestCase):
    def test_interview_cards_include_answer_blueprint_and_pressure_ladder(self):
        self.assertIn('answer-blueprint', APP)
        self.assertIn('pressure-ladder', APP)
        self.assertIn('Context', APP)
        self.assertIn('Business impact', APP)

    def test_planning_labs_include_visible_decision_models(self):
        self.assertIn('forecast-evidence-funnel', INDEX)
        self.assertIn('psi-flow', INDEX)
        self.assertIn('data-role="opening"', INDEX)
        self.assertIn('data-role="approved"', INDEX)

    def test_psi_flow_is_updated_from_simulator_inputs(self):
        self.assertIn('syncPsiFlow', APP)
        self.assertIn('psiOpening', APP)
        self.assertIn('psiEnding', APP)


if __name__ == '__main__':
    unittest.main()
