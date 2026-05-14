from django.shortcuts import render
from django.http import HttpResponse

PRODUK_LIST = [
    {
        'id': 1,
        'nama': 'Laptop Dell XPS 13',
        'harga': 'Rp 15.999.000',
        'deskripsi': 'Laptop premium dengan prosesor Intel Core i7, layar 4K, dan desain yang elegan.'
    },
    {
        'id': 2,
        'nama': 'Smartphone Samsung Galaxy A52',
        'harga': 'Rp 5.999.000',
        'deskripsi': 'Smartphone mid-range dengan kamera 64MP, baterai 4500mAh, dan layar AMOLED.'
    },
    {
        'id': 3,
        'nama': 'Headphone Sony WH-1000XM4',
        'harga': 'Rp 3.499.000',
        'deskripsi': 'Headphone noise-cancelling dengan kualitas audio terbaik dan baterai tahan lama.'
    },
    {
        'id': 4,
        'nama': 'Tablet iPad Pro 12.9"',
        'harga': 'Rp 12.999.000',
        'deskripsi': 'Tablet flagship dengan prosesor M1, layar Liquid Retina, dan dukungan Apple Pencil.'
    },
]


# View untuk Homepage
def homepage(request):
    context = {}
    return render(request, 'katalog/homepage.html', context)


# View untuk Daftar Produk
def daftar_produk(request):
    context = {
        'produk_list': PRODUK_LIST
    }
    return render(request, 'katalog/daftar_produk.html', context)


# View untuk Detail Produk
def detail_produk(request, id):
    produk = None
    for p in PRODUK_LIST:
        if p['id'] == id:
            produk = p
            break
    
    if produk is None:
        return HttpResponse('<h1>Produk tidak ditemukan</h1>', status=404)
    
    context = {
        'produk': produk
    }
    return render(request, 'katalog/detail_produk.html', context)


# View untuk Halaman Kontak
def kontak(request):
    context = {}
    return render(request, 'katalog/kontak.html', context)
