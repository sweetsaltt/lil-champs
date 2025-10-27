# lil-champs
Tugas 2 PBP
Chris Darren Imanuel
2406396956

https://github.com/sweetsaltt/lil-champs
https://chris-darren-lilchamps.pbp.cs.ui.ac.id/

1. Saya telah mengimplementasikan checklist di atas secara bertahap dan runut. Pertama, saya buat proyek baru dan siapkan dependencies dan requirements yang dibutuhkan. Setelah itu, saya siapkan environment serta keperluan untuk deploy yang menghubungkan dengan kredensial untuk database. Selain itu, saya juga configure untuk settings nya dan run server. Setelah berhasil run server, segera saya push dan deploy ke PWS supaya nantinya saya bisa update pengerjaan saya. Kedua, Setelah memastikan bahwa proyek saya berjalan, saya kemudian mulai untuk membuat aplikasi main dan routing ke settings proyek agar terhubung. Setelahnya saya mulai kerjakan Template yaitu cetakan yang nantinya akan menampilkan aplikasi saya melalui HTML. Selanjutnya, saya buat dan kerjakan model Product dan tambahkan atribut produk saya. Ketiga, saya handling bagian views.py dan integrasikan logic yang ada ke bagian template sebelumnya. Tak lupa, saya atur routing URL aplikasi main dan juga proyek supaya view dapat dijalankan. 

2. ![alt text](pbp-1.jpg)

3. settings.py dalam proyek django berfungsi untuk mengatur dan menyusun bagaimana suatu proyek berjalan dan berperilaku. Berdasarkan tutorial dan pengerjaan yang dilakukan, settings.py digunakan untuk enabler environment variables, memberikan akses aplikasi web, melakukan production, hingga mengatur konfigurasi database.

4. Migrasi database dilakukan dengan melakukan makemigrations terlebih dahulu. makemigrations berfungsi untuk mengumpulkan perubahan yang terjadi pada model menjadi satu file migrasi. Setelahnya, kita lakukan migrate untuk menerapkan perubahan tersebut ke database. Dengan demikian, migrasi dilakukan untuk memperbarui dan update model pengerjaan kita agar tetap suitable dengan database.

5. Menurut saya, framework Django cocok untuk belajar sebagai beginner karena Django sendiri berjalan di atas Python. Python sendiri memiliki struktur dan sintaks layaknya seperti berbahasa inggris biasa sehingga familiar untuk dipelajari. Selain itu, Django sendiri telah didevelop dan mempunyai resource dan fasilitas yang mumpuni untuk pembelajaran.

6. Saya sendiri tidak menemukan masalah atau issue dalam pengerjaan tutorial. Mungkin sedikit pesan dari saya untuk teman-teman asdos untuk terus semangat dan mohon bimbingannya selama satu semester ini belajar PBP.

#
Tugas 3 PBP

1. Data delivery atau pengiriman data dari satu titik ke titik lain, seperti dari client - browser atau sistem ke sistem lain, sangatlah penting diimplementasikan dalam sebuah platform. Kita memerlukan data delivery untuk menjaga integrasi sistem agar berfungsi dengan baik, memastikan kita sebagai pengguna memiliki data yang relevan dan terbaru, serta membantu kita untuk upscale dan eskalasi platform agar semakin cepat dan efisien sehingga bermanfaat untuk kebutuhan kita.

2. JSON dan XML mempunyai kelebihan dan kekurangannya masing-masing. Di satu sisi, JSON lebih popular untuk kalangan umum karena sifatnya yang lightweight dan ringan, lebih mudah untuk dibaca dan dimengerti, cepat dan mudah diparsing, serta memiliki dukungan yang luas dan langsung terintegrasi dengan JavaScript sehingga pengembangannya lebih baik. Sedangkan untuk XML unggul dalam mengatasi dokumen yang lebih kompleks dan validasi yang lebih ketat.

3. Fungsi is_valid() digunakan untuk membersihkan input atau data yang masuk dan kemudian dilakukan validasi pemeriksaan apakah sesuai atau memenuhi syarat dari form yang kita buat. Kita membutuhkannya untuk menjaga keamanan dengan mencegah masuknya data yang berbahaya, menjaga integritas data agar tetap tersimpan, serta menjaga pengalaman pengguna.

4. Kita membutuhkan CSRF token untuk menghindari CSRF itu sendiri. CSRF token berfungsi untuk melindungi dari serangan Cross-Site Request Forgery (CSRF). CSRF adalah serangan siber yang memanfaatkan pengguna yang telah divalidasi kebenarannya untuk melakukan suatu tindakan di sebuah website lain tanpa sepengetahuan pengguna.Kehadian csrf_token memberikan keamanan karena Django akan memverifikasi apakah token yang dikirimkan sesuai dengan token yang tersimpan di server sehingga permintaan sah apabila match. Jika kita tidak mengimplementasi csrf_token, kita akan rentan terhadap serangan CSRF dan penyerang dapat memanfaatkan kerugian yang mengatasnamakan kita. Contohnya, seseorang login ke website internet banking sehingga browser menyimpan kredensial dalam cookie sesi. Dalam waktu yang bersamaan, beliau juga mengakses website lain yang dibuat oleh oknum penyerang. Website yang disisipi kode berbahaya tersebut secara otomatis melakukan request POST ke website banking tersebut seperti transfer/tarik tunai. Nah, karena browser korban masih menyimpan sesi login tersebut, server bank menganggap bahwa permintaan tersebut valid dan menyetujui sehingga transaksi pun berhasil tanpa sepengetahuan korban.

5. Implementasi checklist pada tugas 3 kali ini saya lakukan dari pembuatan form yang kemudian dilanjutkan dengan membuat function-function pendukung pada views.py. Tak lupa saya juga sambungkan path nya di urls agar hal yang ingin diakses memiliki tampilan dan destinasi yang sesuai. Setelah mempersiapkan logic nya, saya mulai eksekusi dan handle bagian tampilan html nya. Menurut saya, bagian ini adalah yang paling challenging karena saya harus menghubungkan antara apa yang saya ingin tampilkan di web dapat bekerja sesuai program yang dibuat. Setelah selesai, kemudian saya tambahkan beberapa method data delivery dalam bentuk XML dan JSON. Saya juga pastikan agar function dapat bekerja dengan baik.

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/bd08fd09-3cb6-4954-87f8-b040c5ae62e5" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/61f4f0d3-1de5-4fe7-a00d-15527e4c6a01" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/c35e3f3f-7cf6-498e-9083-e929f02c751b" />
<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/6bbc0855-8f14-49f0-8c18-6f08ef0b50ab" />

#
Tugas 4 PBP

1. AuthenticationForm adalah form bawaan Django yang digunakan untuk melakukan autentikasi pengguna. Form ini menangani proses login dengan memverifikasi kredensial yang dimasukkan pengguna kemudian diproses apakah sesuai dan benar. AuthenticationForm ini telah terintegrasi dengan sistem Django sehingga validasi dilakukan otomatis, mempunyai keamanan bawaan sistem, dan mudah untuk dipakai pengguna sesuai kebutuhan. Namun, kustomisasinya cukup kompleks dan tampilannya sederhana sehingga kurang menarik.

2. Autentikasi adalah proses verifikasi identitas atau penentuan apakah pengguna tersebut exist. Proses ini seperti login dengan username dan password dan dihandle dengan AuthenticationForm. Sedangkan, autorisasi adalah proses menentukan hak akses si pengguna tersebut, apa yang boleh dilakukan atau batasan yang dimiliki. Implementasinya seperti dengan menentukan properti dekorator @login_required untuk mengizinkan pengguna memiliki akses melihat main asalkan seseorang tersebut login dahulu.

3. Session sendiri lebih aman karena data disimpan di server, mempunyai kapasitas yang lebih besar sehingga mampu menyimpan data yang lebih kompleks, serta terenkripsi. Kekurangannya, session jadi lebih berat untuk dihandle server dan lebih sulit untuk scale-up. Sedangkan, cookie ringan dan mudah untuk diimplementasi, namun keamanannya cukup rawan dan banyak dimanfaatkan untuk kejahatan siber.

4. Pada tugas ini, saya mengimplementasi proses autentikasi dengan membuat logic di views, kemudian saya routing ke urls, dan buat template html agar hasil olahan autentikasi dapat direpresentasikan ke pengguna. Selain itu, saya juga lakukan untuk implementasi cookie dengan memanfaatkan last_login. Dan pada akhirmya, saya bisa membedakan setiap dari pada user punya autorisasi hak nya masing-masing sesuai postingan yang dibuat

#
Tugas 5
1. Urutan prioritas CSS selector dimulai dari yang tertinggi hingga terendah. Posisi tertinggi ditempati oleh ID selector, yang memiliki kekuatan spesifisitas paling kuat karena menargetkan elemen secara unik berdasarkan atribut ID. Selanjutnya terdapat class selector, yang meskipun dapat diterapkan pada multiple elemen, tetap memiliki prioritas lebih tinggi daripada element selector. Posisi terendah dalam hierarki ini adalah element selector, yang hanya menargetkan elemen berdasarkan nama tag HTML dan memiliki spesifisitas paling lemah.

2. Responsive design merupakan konsep penting dalam pengembangan web karena memastikan tampilan website dapat beradaptasi optimal di berbagai perangkat dan ukuran layar. Dengan maraknya penggunaan perangkat mobile, responsive design menjadi krusial untuk memberikan pengalaman pengguna yang konsisten dan memenuhi standar SEO modern. Contoh aplikasi yang telah menerapkan responsive design dengan baik adalah Tokopedia dan Netflix.

3. Margin, border, dan padding adalah tiga komponen fundamental dalam CSS box model. Padding merupakan ruang internal antara konten elemen dengan border, border adalah garis batas yang mengelilingi padding dan konten, sedangkan margin adalah ruang eksternal yang memisahkan elemen dengan elemen lain di sekitarnya. Implementasinya menggunakan properti CSS seperti padding: 10px; border: 1px solid black; margin: 20px;

4. Flexbox dan grid layout merupakan sistem tata letak CSS. Flexbox dirancang untuk tata letak satu dimensi yang mengatur elemen dalam garis lurus (baik horizontal maupun vertical) dan ideal untuk komponen kecil seperti navigasi bar. Sementara grid layout merupakan sistem dua dimensi yang mengatur elemen dalam baris dan kolom secara bersamaan dan cocok untuk tata letak halaman yang kompleks seperti layout website lengkap dengan header, sidebar, dan main content.