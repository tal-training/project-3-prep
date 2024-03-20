let HOST="http://127.0.0.1:5000/api/services"

function showServices(){
    axios.get(HOST).then(r=>{
        r.data.services.map((service,i)=>{
            let e=document.createElement("div")
            e.className="service"
            e.innerText=service
            e.id=i
            document.getElementById("navbar").appendChild(e)
        })
    })
}

showServices();