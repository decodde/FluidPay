
window.onload = async () => {
    Home.start()
}

let Home = {
    start: async () => {
        Home.load.availablePorts();
    },
    load: {
        availablePorts: async () => {
            let a = await Main.api.fetchAvailablePorts();
            console.log(a);
            let selectHtml = "";
            let html = "";
            if (a.length > 0) {
                
                if (a.length > 0) {
                    a.forEach(p => {
                        selectHtml += `<option value='${p.name}'>${p.description}<option>`;
                        html += `<p> ${p.description}</p>`;
                    })
                }
                

            }
            else{
                selectHtml += `<option disabled selected>No Available Port<option>`;
                html += `<p> No Available Port</p>`;
            }
            
            let container = await Main.class("availablePortsContainer");
            console.log(selectHtml)
            container.length > 0 ? Object.keys(container).forEach(c => container[c].innerHTML = html) : "";
            let selectContainers = await Main.class("availablePortsSelect");
            console.log(selectContainers);
            selectContainers ? Object.keys(selectContainers).forEach(c => selectContainers[c].innerHTML = selectHtml) : "";
        }
    }
}

let availablePorts = async () => {

}

