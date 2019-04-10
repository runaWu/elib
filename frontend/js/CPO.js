
// ============================================
function addcoy() {
    var url_string = window.location.href
    var url = new URL(url_string);
    // var contract_id = Number(url.searchParams.get("contract_id"));
    createPeminjaman()
}
// ============================================

// ADD PURCHASE ORDER ============================================================
function createPeminjaman() {
    // var quiz_id = document.getElementById("quiz").value;
    var person_id = $('input#person_id').val()
    var buku_id = $('input#buku_id').val()
    var nama = $('input#nama').val()
    var judul = $('input#judul').val()
    var tanggal_peminjaman = $('input#tanggal_peminjaman').val()
    var tanggal_pengembalian = $('#tanggal_pengembalian').val()


    console.log(person_id);
    console.log(buku_id);
    console.log(nama);
    console.log(judul);
    console.log(tanggal_peminjaman);
    console.log(tanggal_pengembalian);


    $.ajax({
        url: `http://127.0.0.1:5000/addPeminjaman`,
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            person_id : person_id,
            buku_id : buku_id,
            nama : nama,
            judul : judul,
            tanggal_peminjaman : tanggal_peminjaman,
            tanggal_pengembalian : tanggal_pengembalian
        }),
        success: function () {
            alert("peminjaman ditambahkan");
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

