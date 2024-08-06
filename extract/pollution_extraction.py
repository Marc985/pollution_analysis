from utils.utils import collect_and_save_data

def los_angeles_pollution():
    return collect_and_save_data("34.052235", "-118.243683","Los Angeles")


def tokyo_pollution():
    return collect_and_save_data("35.682839", "139.759455","Tokyo")


def antananarivo_pollution():
    return collect_and_save_data("-18.918869188079366", "47.5192845707442","Antananarivo")


def nairobi_pollution():
    return collect_and_save_data("-1.286389", "36.817223","Nairobi")


def lima_pollution():
    return collect_and_save_data("-12.046373", "-77.042755","Lima")


lima_pollution()


