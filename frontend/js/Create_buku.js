// ============================================
function addcoy() {
    var url_string = window.location.href
    var url = new URL(url_string);
    // var contract_id = Number(url.searchParams.get("contract_id"));
    createBuku_()
}
// ============================================

// ADD BUKU ============================================================
function createBuku_() {
    // var quiz_id = document.getElementById("quiz").value;
    var judul = $('input#judul').val()
    var tahun_terbit = $('input#tahun_terbit').val()
    var pengarang = $('input#pengarang').val()



    console.log(judul);
    console.log(tahun_terbit);
    console.log(pengarang);



    $.ajax({
        url: `http://127.0.0.1:5000/addBuku`,
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            judul : judul,
            tahun_terbit : tahun_terbit,
            pengarang : pengarang
        }),
        success: function () {
            alert("buku ditambahkan");
            // window.location.href = 'ke view.html'
        },
        error: function () {
            alert("cek semua inputanya");
        },
        complete: function () {
            console.log("done");
        }
    });
} 

