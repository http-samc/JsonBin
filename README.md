# JsonBin
 A Pythonic wrapper for [JSON Bin](https://jsonbin.io).

# How To Use
1. Import api and the JSONBin class
2. Create a JSONBin object
3. Use any of the methods to interact with the API

# Class Methods

``__init__``
    **@Param**: key - ``(str)`` JSONBin API Secret key
    **@Param**: PATH - {2 possible types}
        ``(bool)`` you do not want to add a 
        unique *boot.json* filepath
        ``(str)`` the filepath of your 
        *boot.json*
    **@Desc**: Creates a JSONBin Object, defines *boot.json*

``boot``
    **@Return**: ``(bool)``
        True on success
        False on fail
            due to either invalid JSON or invalid PATH
    **@Desc**: updates self.bins with bin_ids from *boot.json*

``add_bin``
    **@Param**: bin_id - ``(str)`` JSONBin Bin ID
    **@Desc**: adds bin (by bin_id) to reference list

``get_bins``
    **@Return**: bins - ``(list)`` Registered JSONBin Id's
    **@Desc**: exports all known bin id's

``create``
    **@Param**: name - ``(str)`` the name of your bin
    **@Param**: visibility - ``(bool)`` the privacy
        True -> makes bin public
        False -> makes bin private
    **@Param**: data - (dict) the data to be in the JSON bin
    **@Return**: http status code
    **@Desc**: creates a JSON bin

``get``
    **@Param**: bin_id - {2 possible types}
        ``(int)`` the index of the bin_id in self.bins
            use if you created or added the bin
            within your running instance
            (or from a *boot.json* file)
        ``(str)`` the reference id of the bin
            use if bin wasn't created or added
            within your running instance
            (or from a *boot.json* file)
    **@Return**: http status code
    **@Desc**: gets json data from a bin

``update``
    **@Param**: bin_id - {2 possible types}
        ``(int)`` the index of the bin_id in self.bins
            use if you created or added the bin
            within your running instance
            (or from a *boot.json* file)
        ``(str)`` the reference id of the bin
            use if bin wasn't created or added
            within your running instance
            (or from a *boot.json* file)
    **@Param**: data - (dict) the new data for the bin
    **@Return**: http status code
    **@Desc**: updates bin data

``privacy``
    **@Param**: bin_id - {2 possible types}
        ``(int)`` the index of the bin_id in self.bins
            use if you created or added the bin
            within your running instance
            (or from a *boot.json* file)
        ``(str)`` the reference id of the bin
            use if bin wasn't created or added
            within your running instance
            (or from a *boot.json* file)
    **@Param**: visibility - ``(bool)`` the new privacy
        True -> makes bin public
        False -> makes bin private
    **@Return**: http status code
    **@Desc**: updates bin visibility

``delete``
    **@Param**: bin_id - {2 possible types}
        ``(int)`` the index of the bin_id in self.bins
            use if you created or added the bin
            within your running instance
            (or from a *boot.json* file)
        ``(str)`` the reference id of the bin
            use if bin wasn't created or added
            within your running instance
            (or from a *boot.json* file)
    **@Return**: http status code
    **@Desc**: deletes bin