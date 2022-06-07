# Import basic Flask methods (request is the method that actually makes HTTP requests)
from flask import Flask, request, abort, make_response, url_for, jsonify
# Work with json data
import json

datafilename = '/home/myapp/network_equipment.json'

def read_datafile(datafile):
    with open(datafile, 'r') as filedata:
        jsonstring = filedata.read()
        network_equipment_list = json.loads(jsonstring)
        type(network_equipment_list)
        print(network_equipment_list)
    return network_equipment_list

def write_datafile(datafilename,file_data):
    with open(datafilename, 'w') as datafile:
        jsonstring = json.dumps(file_data, indent=3)
        datafile.write(jsonstring)

# Create Flask environment
app = Flask(__name__)
app.debug = True

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@app.route('/api/v1.0/equipment', methods=['GET'])
def get_all_equipment():
    network_equipment_list = read_datafile(datafilename)
    return jsonify({'Equipment': network_equipment_list})
    
@app.route('/api/v1.0/equipment/<int:equipment_id>', methods=['GET'])
def get_device(equipment_id):
    network_equipment_list = read_datafile(datafilename)
    equipment = [ equipment for equipment in network_equipment_list if equipment['id'] == equipment_id]
    if len(equipment) == 0:
        abort(404)
    return jsonify({'Equipment': equipment})

@app.route('/api/v1.0/equipment', methods=['POST'])
def create_equipment():
    if not request.json or not 'Hostname' in request.json:
        abort(400)
    network_equipment_list = read_datafile(datafilename)
    new_equipment = { 
        "id": network_equipment_list[-1]['id'] + 1,
        "Hostname": request.json['Hostname'],
        "Type": request.json['Type'],
        "Make": request.json['Make'],
        "Model": request.json['Model'],
        "Firmware": request.json['Firmware'],
        "ManagementIP": request.json['ManagementIP'],
        "ManagementVlan": request.json['ManagementVlan']
    }
    network_equipment_list.append(new_equipment)
    write_datafile(datafilename,network_equipment_list)
    return jsonify({'Equipment': new_equipment}), 201

@app.route('/api/v1.0/equipment/<int:equipment_id>', methods=['PUT'])
def update_device(equipment_id):
    network_equipment_list = read_datafile(datafilename)
    equipment = [ equipment for equipment in network_equipment_list if equipment['id'] == equipment_id]
    if len(equipment) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'Hostname' in request.json:
        if type(request.json['Hostname']) is not str:
            abort(400)
        equipment[0]['Hostname'] = request.json.get('Hostname', equipment[0]['Hostname'])
    else:
        equipment[0]['Hostname'] = ""
    if 'Type' in request.json:
        if (request.json['Type'] != "Router" and request.json['Type'] != "Switch"):
            abort(400)
        equipment[0]['Type'] = request.json.get('Type', equipment[0]['Type'])
    else:
        equipment[0]['Type'] = ""
    if 'Make' in request.json:
        if type(request.json['Make']) is not str:
            abort(400)
        equipment[0]['Make'] = request.json.get('Make', equipment[0]['Make'])
    else:
        equipment[0]['Make'] = ""
    if 'Model' in request.json:
        if type(request.json['Model']) is not str:
            abort(400)
        equipment[0]['Model'] = request.json.get('Model', equipment[0]['Model'])
    else:
        equipment[0]['Model'] = ""
    if 'ManagementIP' in request.json:
        if type(request.json['ManagementIP']) is not str:
           abort(400)
        equipment[0]['ManagementIP'] = request.json.get('ManagementIP', equipment[0]['ManagementIP'])
    else:
        equipment[0]['ManagementIP'] = ""
    if 'ManagementVlan' in request.json:
        if type(request.json['ManagementVlan']) is not int:
           abort(400)
        equipment[0]['ManagementVlan'] = request.json.get('ManagementVlan', equipment[0]['ManagementVlan'])
    else:
        equipment[0]['ManagementVlan'] = ""
    if 'Firmware' in request.json:
        if type(request.json['Firmware']) is not float:
            abort(400)
        equipment[0]['Firmware'] = request.json.get('Firmware', equipment[0]['Firmware'])
    else:
        equipment[0]['Firmware'] = ""
    write_datafile(datafilename,network_equipment_list)
    return jsonify({'equipment': equipment[0]})

@app.route('/api/v1.0/equipment/<int:equipment_id>', methods=['DELETE'])
def delete_device():
    network_equipment_list = read_datafile(datafilename)
    equipment = [ equipment for equipment in network_equipment_list if equipment['id'] == equipment_id]
    if len(equipment) == 0:
        abort(404)
    network_equipment_list.remove(equipment[0])
    write_datafile(datafilename,network_equipment_list)
    return jsonify({'result': True})

@app.route('/api/v1.0/equipment/<int:equipment_id>', methods=['PATCH'])
def update_field(equipment_id):
    network_equipment_list = read_datafile(datafilename)
    equipment = [ equipment for equipment in network_equipment_list if equipment['id'] == equipment_id]
    if len(equipment) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'Hostname' in request.json:
        if type(request.json['Hostname']) is not str:
            abort(400)
        else:
            equipment[0]['Hostname'] = request.json.get('Hostname', equipment[0]['Hostname'])
    if 'Type' in request.json:
        if request.json['Type'] != "Router" and request.json['Type'] != "Switch":
            abort(400)
        else:
           equipment[0]['Type'] = request.json.get('Hostname', equipment[0]['Hostname'])
    if 'Make' in request.json:
        if type(request.json['Make']) is not str:
            abort(400)
        else:
            equipment[0]['Make'] = request.json.get('Make', equipment[0]['Make'])
    if 'Model' in request.json:
        if type(request.json['Model']) is not str:
            abort(400)
        else:
            equipment[0]['Model'] = request.json.get('Model', equipment[0]['Model'])
    if 'ManagementIP' in request.json:
        if type(request.json['ManagementIP']) is not str:
            abort(400)
        else:
            equipment[0]['ManagementIP'] = request.json.get('ManagementIP', equipment[0]['ManagementIP'])
    if 'ManagementVlan' in request.json:
        if type(request.json['ManagementVlan']) is not int:
            abort(400)
        else:
            equipment[0]['ManagementVlan'] = request.json.get('ManagementVlan', equipment[0]['ManagementVlan'])
    if 'Firmware' in request.json:
        if type(request.json['Firmware']) is not float:
            abort(400)
        else:
            equipment[0]['Firmware'] = request.json.get('Firmware', equipment[0]['Firmware'])
    write_datafile(datafilename,network_equipment_list)
    return jsonify({'equipment': equipment[0]})
   
@app.route('/')
def default_page():
    return "\nWhy hello there, DSYS601 student. There is an api on this website - reachable via http://localhost:5050/api\n\n"

@app.route('/api')
def api_page():
    return "\nHi there you devops guru, you. Base api url is http://localhost:5050/api/v1.0/equipment\n\n"

# If the app was called from the command line then run the app on TCP port 5002, turning debug messages on
if __name__ == '__main__':
  app.run(port='5050',debug=True)

