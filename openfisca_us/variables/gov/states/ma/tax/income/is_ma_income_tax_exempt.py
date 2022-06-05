from openfisca_us.model_api import *


class is_ma_income_tax_exempt(Variable):
    value_type = float
    entity = TaxUnit
    label = "MA income tax exempt"
    unit = USD
    definition_period = YEAR
    is_eligible = in_state("MA")
    reference = "https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter62/Section5"

    def formula(tax_unit, period, parameters):
        agi = tax_unit("ma_agi", period)
        threshold = tax_unit("ma_income_tax_exemption_threshold", period)
        return agi <= threshold