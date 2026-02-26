async function uploadImage(){

    let file = document.getElementById("imageInput").files[0];
    if(!file) return;

    document.getElementById("preview").innerHTML =
        `<img src="${URL.createObjectURL(file)}">`;

    let formData = new FormData();
    formData.append("file", file);

    let res = await fetch("/predict",{
        method:"POST",
        body:formData
    });

    let result = await res.json();

    let color = result.prediction==="Uninfected" ? "green":"red";
    let cls = result.prediction==="Uninfected" ? "success":"danger";

    document.getElementById("result").className="report "+cls;

    document.getElementById("result").innerHTML=`

        <h2>Diagnostic Report</h2>

        <h1>${result.prediction}</h1>

        <p>Confidence Level: ${result.confidence}%</p>

        <div class="progress">
            <div class="bar ${color}" style="width:${result.confidence}%"></div>
        </div>

        <br>
        <p>Parasitized Probability: ${result.parasitized_probability}%</p>
        <p>Uninfected Probability: ${result.uninfected_probability}%</p>
        <p>Timestamp: ${result.timestamp}</p>

        <br>
        <h3>Medical Disclaimer</h3>
        <p>This AI system is a screening tool. Consult healthcare professionals.</p>
    `;
}