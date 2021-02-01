import requests
import json

class JSONBin:

    """
    @Param: key - (str) JSONBin API Secret key
    @Param: PATH - {2 possible types}
        (bool) you do not want to add a 
        unique boot.json filepath
        (str) the filepath of your 
        boot.json
    @Desc: Creates a JSONBin Object, defines boot.json
    """
    def __init__(self, key, PATH):
        self.key = key
        self.bins = []
        
        if isinstance(PATH, bool):
            self.PATH = "boot.json"
        else:
            self.PATH = PATH
    
    """
    @Return: (bool)
        True on success
        False on fail
            due to either invalid JSON or invalid PATH
    @Desc: updates self.bins with bin_ids from boot.json
    """
    def boot(self):
        with open(self.PATH) as f:
            data = json.loads(f.read())
        
        try:
            bin_ids = [data["bin_ids"]]
            
            for bin_id in bin_ids:
                self.bins.append(bin_id)
            return True
        except Exception:
            return False
        
    """
    @Param: bin_id - (str) JSONBin Bin ID
    @Desc: adds bin (by bin_id) to reference list
    """
    def add_bin(self, bin_id):
        self.bins.append(bin_id)

    """
    @Return: bins - (list) Registered JSONBin Id's
    @Desc: exports all known bin id's
    """
    def get_bins(self):
        return self.bins
    
    """
    @Param: name - (str) the name of your bin
    @Param: visibility - (bool) the privacy
        True -> makes bin public
        False -> makes bin private
    @Param: data - (dict) the data to be in the JSON bin
    @Return: http status code
    @Desc: creates a JSON bin
    """
    def create(self, name, visibility, data):
        if visibility == True:
            visibility = "true"
        else:
            visibility = "false"

        url = 'https://api.jsonbin.io/v3/b'
        
        headers = {
          'Content-Type': 'application/json',
          'X-Master-Key': self.key,
          'X-Bin-Private' : visibility,
          'X-Bin-Name' : name
        }
        r = requests.post(url, json=data, headers=headers)
        response = json.loads(r.text)
        self.bins.append(response["metadata"]["id"])
        return r
    
    """
    @Param: bin_id - {2 possible types}
        (int) the index of the bin_id in self.bins
            use if you created or added the bin
            within your running instance
            (or from a boot.json file)
        (str) the reference id of the bin
            use if bin wasn't created or added
            within your running instance
            (or from a boot.json file)
    @Return: http status code
    @Desc: gets json data from a bin
    """
    def get(self, bin_id):
        
        if isinstance(bin_id, int):
            url = f"https://api.jsonbin.io/v3/b/{self.bins[bin_id]}/latest"
        else:
            url = f"https://api.jsonbin.io/v3/b/{bin_id}/latest"
            
        headers = {
          'X-Master-Key': self.key,
        }
        r = requests.get(url, json=None, headers=headers)
        return r.text

    """
    @Param: bin_id - {2 possible types}
        (int) the index of the bin_id in self.bins
            use if you created or added the bin
            within your running instance
            (or from a boot.json file)
        (str) the reference id of the bin
            use if bin wasn't created or added
            within your running instance
            (or from a boot.json file)
    @Param: data - (dict) the new data for the bin
    @Return: http status code
    @Desc: updates bin data
    """
    def update(self, bin_id, data):
        
        if isinstance(bin_id, int):
            url = f"https://api.jsonbin.io/v3/b/{self.bins[bin_id]}"
        else:
            url = f"https://api.jsonbin.io/v3/b/{bin_id}"
            
        url = f"https://api.jsonbin.io/v3/b/{self.bins[bin_id]}"
        headers = {
          'Content-Type': 'application/json',
          'X-Master-Key': self.key
        }
        
        r = requests.put(url, json=data, headers=headers)
        return r

    """
    @Param: bin_id - {2 possible types}
        (int) the index of the bin_id in self.bins
            use if you created or added the bin
            within your running instance
            (or from a boot.json file)
        (str) the reference id of the bin
            use if bin wasn't created or added
            within your running instance
            (or from a boot.json file)
    @Param: visibility - (bool) the new privacy
        True -> makes bin public
        False -> makes bin private
    @Return: http status code
    @Desc: updates bin visibility
    """
    def privacy(self, bin_id, visibility):
        
        if isinstance(bin_id, int):
            url = f"https://api.jsonbin.io/v3/b/{self.bins[bin_id]}/meta/privacy"
        else:
            url = f"https://api.jsonbin.io/v3/b/{bin_id}"

        if visibility == True:
            visibility = "true"
        else:
            visibility = "false"
            
        headers = {
          'X-Master-Key': self.key,
          'X-Bin-Private': visibility
        }
        
        r = requests.delete(url, json=None, headers=headers)
        return r

    """
    @Param: bin_id - {2 possible types}
        (int) the index of the bin_id in self.bins
            use if you created or added the bin
            within your running instance
            (or from a boot.json file)
        (str) the reference id of the bin
            use if bin wasn't created or added
            within your running instance
            (or from a boot.json file)
    @Return: http status code
    @Desc: deletes bin
    """
    def delete(self, bin_id):
        
        if isinstance(bin_id, int):
            url = f"https://api.jsonbin.io/v3/b/{self.bins[bin_id]}"
        else:
            url = f"https://api.jsonbin.io/v3/b/{bin_id}"
            
        headers = {
          'X-Master-Key': self.key
        }
        
        r = requests.delete(url, json=None, headers=headers)
        return r