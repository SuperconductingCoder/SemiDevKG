from mp_api.client import MPRester
from emmet.core.summary import HasProps
import json

MP_API_KEY = "dvLdlOGxotqbTIBE6OwjpQOnqooTiRDk"
mpr = MPRester(MP_API_KEY)    

def material_summry_ID(material_id):
    try:
        summary = mpr.materials.summary.search(material_id)[0]
        return summary.material_id, summary.band_gap, summary.is_gap_direct, summary.is_magnetic, summary.total_magnetization, summary.e_electronic

    except:
        return "", "", "", "", "", ""
    
def material_summry_formula(formula):
    try:
        summary = mpr.materials.summary.search(formula=formula)[0]
        return summary.material_id, summary.band_gap, summary.is_gap_direct, summary.is_magnetic, summary.total_magnetization, summary.e_electronic

    except:
        return "", "", "", "", "", ""
        
    

def generate_material_dict():
    with open(r"material_data.json", 'r') as read_file:
        electronic_materials = json.load(read_file)

    elements_dict = electronic_materials["elements"] #the element dictionary
    compounds_dict = electronic_materials["compounds"] #the compounds dictionary

    elements={}
    for element in elements_dict:
        formula=elements_dict[element]["formula"]
        print(f"formula: {formula}")
        if "material_id" in elements_dict[element]:
            id = elements_dict[element]["material_id"]
            summary = material_summry_ID(id)
        else:
            summary = material_summry_formula(formula)
        elements[element] = {"formula": formula, 
                             "material_id": summary[0],
                             "band_gap": summary[1],
                             "is_gap_direct": summary[2],
                             "is_magnetic": summary[3],
                             "total_magnetization": summary[4],
                             "e_electronic": summary[5]}
    compounds={}
    for compound in compounds_dict:
        formula=compounds_dict[compound]["formula"]
        print(f"formula: {formula}")
        if "material_id" in compounds_dict[compound]:
            id = compounds_dict[compound]["material_id"]
            summary = material_summry_ID(id)
        else:
            summary = material_summry_formula(formula)
        compounds[compound] = {"formula": formula,  
                             "material_id": summary[0],
                             "band_gap": summary[1],
                             "is_gap_direct": summary[2],
                             "is_magnetic": summary[3],
                             "total_magnetization": summary[4],
                             "e_electronic": summary[5]}
    
    with open(r"material_data2.json", 'w') as output_file:
        semiconductor_dict = {"elements":elements, "compounds":compounds}
        json.dump(semiconductor_dict, output_file, ensure_ascii=True, indent=2, sort_keys=True)

if __name__ == "__main__":
    generate_material_dict()
    
    
    