function add_item(){
    document.getElementById("add_product").style.display = "block"
    document.getElementById("show_products").style.display = "none"
    document.getElementById("action_selection").innerHTML = "Abbrechen"
    document.getElementById("action_selection").onclick = show_products
}
function show_products(){
    document.getElementById("add_product").style.display = "none"
    document.getElementById("show_products").style.display = "block"
    document.getElementById("action_selection").innerHTML = "Hinzufügen"
    document.getElementById("action_selection").onclick = add_item
}
$("#add_item_backend").change(function () {
    const file = this.files[0];
    console.log("Datei ausgewählt:", file.name);

    // FormData erstellen und Datei anhängen
    const formData = new FormData();
    formData.append("file", file);

    fetch("http://localhost:5000/api", {
        method: "POST",
        body: formData,
    })
        .then((response) => response.json())
        .then((result) => {
            console.log("Erfolgreiche Antwort:", result);
            console.log(result)
            document.getElementById("product_info_container").style.display = "grid"
            document.getElementById("detailname_value").innerText = result[1]
            document.getElementById("vendor_value").innerText = result[2]
            document.getElementById("origin_value").innerText = result[3]
        })
        .catch((error) => {
            console.error("Fehler beim Hochladen:", error);
        });
    
});