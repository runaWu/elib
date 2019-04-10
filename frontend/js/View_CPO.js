
// VIEW BUKU BY ======================================
$.ajax({
    url: `http:http://127.0.0.1:5000/getBukuBy/${buku_id}`,
    method: "GET",
    async: true,

    success: function (profil) {

        $('#buku_id').val(profil.buku_id)
        $('#judul').val(profil.judul)
        $('#pengarang').val(profil.pengarang)
        $('#tahun_terbit').val(profil.tahun_terbit)

        console.log(profil.buku_id)
        console.log(profil.judul)
        console.log(profil.pengarang)
        console.log(profil.tahun_terbit)
    },
    error: function (error) {
        //error handling

    },
    complete: function () {

    }
})

