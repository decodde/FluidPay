let Main = {
    req: async (url, post, data, auth) => {
        let opt = {
            method: post ? "POST" : "GET",
            body: JSON.stringify(data),
            headers: {
                "Content-Type": "application/json",
                "Authorization": auth ? `Bearer ${authKey}` : ""
            }
        }
        try {
            let _req = await fetch(url, opt);
            _req = await _req.json();
            return _req;
        }
        catch (e) {
            console.log(e);
            return e
        }
    },
    api : {
        fetchAvailablePorts : async () => await Main.req("/getAvailablePorts")
    },
    class : (className) => {
        return document.getElementsByClassName(className);
    },
    id : (id) => {
        return document.getElementById(id);
    },
    $ : (el) => {
        return document.querySelector(el);
    }
}