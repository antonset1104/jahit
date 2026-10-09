"""Original bilingual editorial content for Jahit Terukur.

References check concepts. Their prose, diagrams and projects are not republished.
"""

SOURCES = {
    "usu": ("Utah State University Extension — Easy Table Runner", "https://extension.usu.edu/sewing/research/easy-table-runner"),
    "seam": ("Sewing & Craft Alliance — Simple Seaming Techniques", "https://www.sewing.org/files/guidelines/11_110_simple_seaming_techniques.pdf"),
    "measure": ("Sewing & Craft Alliance — Measuring Tools", "https://www.sewing.org/files/guidelines/1_135_measuring%20tools.pdf"),
    "shrink": ("CottonWorks — Shrinkage & Skewing", "https://cottonworks.com/learning-hub/quality-assurance/shrinking-and-skewing/"),
    "nist": ("NIST — Metric (SI) Units", "https://www.nist.gov/pml/owm/metric-si/si-units"),
}

GUIDES = [
    {
        "slug": "ukuran-jadi-dan-ukuran-potong", "sources": ["measure", "seam"],
        "id": {"title": "Bedakan ukuran jadi dan ukuran potong", "summary": "Dua angka yang tampak mirip dapat menghasilkan benda dengan ukuran berbeda. Mulailah dari hasil akhir, lalu tambahkan ruang untuk sambungan.",
            "sections": [
                ("Tentukan benda yang selesai", "Ukuran jadi adalah lebar dan panjang benda setelah tepi disambung atau dilipat. Tuliskan ukuran ini sebelum membuat pola. Untuk panel persegi panjang, catat lebar dan panjang secara terpisah, termasuk sisi mana yang akan menjadi bagian atas. Sketsa kecil dengan tanda arah kain membantu mencegah kedua sisi tertukar."),
                ("Tambahkan kampuh pada tepi yang dijahit", "Kampuh adalah jarak antara tepi potong dan garis jahit. Jika keempat tepi memakai kampuh yang sama, lebar potong = lebar jadi + dua kali kampuh; panjang potong = panjang jadi + dua kali kampuh. Jika ada lipatan kelim, ritsleting, atau sambungan khusus, hitung tepinya satu per satu dan jangan memakai rumus sederhana ini tanpa penyesuaian."),
                ("Catat angka sebelum memotong", "Tulis ukuran jadi, kampuh tiap tepi, dan ukuran potong pada pola. Periksa dengan penggaris yang sama dan satuan yang sama. Pola komersial dapat sudah memuat kampuh; menambahkannya sekali lagi akan mengubah ukuran hasil. Jahit sampel kecil saat ketepatan ukuran penting."),
            ], "example": "Panel jadi 40 × 50 cm dengan kampuh 1 cm pada semua sisi perlu potongan 42 × 52 cm. Angka ini belum memasukkan kelim atau susut kain.", "pitfall": "Jangan menyamakan garis jahit dengan tepi potong, atau menambah kampuh pada pola yang sudah memilikinya."},
        "en": {"title": "Finished size versus cut size", "summary": "Similar-looking measurements can produce different finished objects. Start with the result you want, then allow for joins.",
            "sections": [
                ("Describe the finished object", "Finished size means the width and length after edges are sewn or folded. Write these dimensions before drafting a pattern. For a rectangular panel, record width and length separately and mark which edge will be the top. A small sketch with fabric direction prevents swapped dimensions."),
                ("Add allowance at sewn edges", "Seam allowance is the distance from the cut edge to the stitching line. If all four edges use the same allowance, cut width equals finished width plus twice the allowance; cut length follows the same rule. A folded hem, zipper or special join needs its own edge-by-edge calculation rather than this simple formula."),
                ("Record numbers before cutting", "Put finished size, allowance at each edge and cut size on the pattern. Check with one ruler and one unit system. A commercial pattern may already include allowances; adding them again changes the finished size. Sew a small sample when fit matters."),
            ], "example": "A 40 × 50 cm finished panel with 1 cm seam allowance on all sides needs a 42 × 52 cm cut. This excludes hems and fabric shrinkage.", "pitfall": "Do not confuse a stitching line with a cut edge, or add allowance again to a pattern that already includes it."},
    },
    {
        "slug": "kampuh-dan-kelim", "sources": ["seam", "measure"],
        "id": {"title": "Kampuh dan kelim memiliki fungsi berbeda", "summary": "Sambungan dua potong kain berbeda dari lipatan tepi yang tampak. Rencanakan masing-masing sebagai bagian pola.",
            "sections": [
                ("Kampuh berada di sambungan", "Kampuh memberi ruang untuk menjahit dua sisi. Lebarnya ditentukan pola, jenis kain, dan teknik finishing; tidak ada satu angka yang cocok untuk semua proyek. Tandai garis jahit dan arah menyatukan kain. Jika sambungan ada pada dua sisi panel, hitung tambahan pada kedua sisi tersebut."),
                ("Kelim berada di tepi luar", "Kelim melipat tepi kain agar tampak rapi dan tidak mudah terurai. Kelim lipat ganda memerlukan bahan sesuai dua lipatannya, bukan otomatis sama dengan kampuh. Tentukan berapa sentimeter setiap lipatan sebelum menentukan ukuran potong, lalu uji pada sisa kain untuk melihat ketebalannya."),
                ("Buat daftar tepi", "Gambarkan persegi panjang dan tulis perlakuan pada setiap sisi: jahit, kelim, atau dibiarkan sesuai pola. Jumlahkan tambahan hanya pada sisi yang memerlukannya. Jika teknik finishing berubah, ulangi hitungan karena ukuran potong juga berubah."),
            ], "example": "Panel jadi selebar 40 cm dengan kampuh kiri 1 cm dan kelim kanan dua lipatan masing-masing 1 cm membutuhkan lebar potong 43 cm.", "pitfall": "Jangan mengganti kelim lipat ganda dengan satu angka kampuh tanpa menghitung seluruh lipatan."},
        "en": {"title": "Seam allowances and hems do different jobs", "summary": "Joining two pieces differs from folding a visible outer edge. Plan each edge as part of the pattern.",
            "sections": [
                ("Allowances belong to joins", "A seam allowance provides space to stitch two edges. Its width depends on the pattern, fabric and finishing method; no single number suits every project. Mark the stitching line and how pieces meet. If a panel has a join on both sides, add space at both sides."),
                ("Hems belong to outer edges", "A hem folds a fabric edge for a tidy finish and to control fraying. A double-fold hem needs material for both folds; it does not automatically equal the seam allowance. Decide each fold depth before sizing the cut piece, then test on a scrap to see how bulky it becomes."),
                ("List every edge", "Draw a rectangle and label each edge: seam, hem or another treatment from the pattern. Add material only where required. If the finishing method changes, calculate the cut dimensions again."),
            ], "example": "A panel 40 cm wide when finished, with a 1 cm seam on the left and two 1 cm hem folds on the right, needs a 43 cm cut width.", "pitfall": "Do not replace a double-fold hem with one seam-allowance number without accounting for both folds."},
    },
    {
        "slug": "arah-serat-dan-lebar-kain", "sources": ["usu", "measure"],
        "id": {"title": "Baca arah serat dan lebar kain", "summary": "Perhitungan potongan hanya benar jika orientasi pola memang boleh dipasang pada lebar kain yang tersedia.",
            "sections": [
                ("Kenali tepi kain", "Kain tenun umumnya memiliki dua tepi memanjang yang disebut pinggir kain atau selvage. Arah sejajar pinggir ini adalah arah panjang kain. Lebar kain tercetak pada label gulungan, tetapi bagian yang benar-benar dapat dipakai mungkin lebih sempit karena pinggir, cacat, atau keputusan finishing."),
                ("Ikuti arah pola", "Tanda arah serat pada pola membantu menempatkan potongan sesuai rancangan. Memutar potongan 90 derajat bisa menghemat kain secara matematis, tetapi dapat mengubah jatuh kain, arah motif, atau elastisitas. Kalkulator panel situs ini menganggap lebar potong dibentangkan melintang lebar kain; gunakan hanya jika orientasi itu sesuai pola."),
                ("Ukur lebar efektif", "Ukur lebar kain sebenarnya setelah persiapan, lalu kurangi bagian tepi yang tidak ingin dipakai. Catat lebar efektif sebagai masukan alat. Bila ada motif searah, beludru, atau kain berbulu, susun semua panel dengan arah yang sama dan pertimbangkan tambahan di luar hasil alat."),
            ], "example": "Kain berlabel 150 cm dengan 3 cm tepi yang disisihkan di setiap sisi memberi lebar efektif 144 cm. Tiga panel selebar 42 cm muat dalam satu baris jika orientasinya sesuai.", "pitfall": "Jangan memutar pola hanya agar angka kebutuhan kain turun ketika tanda serat atau arah motif melarangnya."},
        "en": {"title": "Read grain direction and usable width", "summary": "A cutting calculation works only when the pattern may be oriented across the available fabric width.",
            "sections": [
                ("Identify the fabric edges", "Woven fabric usually has two lengthwise selvage edges. The direction parallel to them is the lengthwise grain. The bolt label states a nominal width, but usable width may be smaller because of selvages, defects or the chosen edge finish."),
                ("Follow the pattern direction", "Grainline marks place pieces as designed. Rotating a piece 90 degrees may save fabric in arithmetic but can change drape, print direction or stretch. This site's panel calculator lays the cut width across the fabric width; use it only when that orientation matches your pattern."),
                ("Measure usable width", "Measure actual fabric width after preparation and subtract the edges you will not use. Enter that usable width in the tool. With one-way prints, pile or nap, align every panel in the same direction and allow extra fabric beyond the tool's result."),
            ], "example": "A fabric labeled 150 cm wide with 3 cm reserved at each edge has 144 cm usable width. Three 42 cm panels fit in one row if their orientation is valid.", "pitfall": "Do not rotate pattern pieces just to reduce yardage when grainline or print direction prohibits it."},
    },
    {
        "slug": "susun-panel-persegi-panjang", "sources": ["measure", "nist"],
        "id": {"title": "Susun panel persegi panjang pada kain", "summary": "Hitung berapa potong muat per baris sebelum mengalikan panjang kain. Susunan ini transparan, tetapi sengaja sederhana.",
            "sections": [
                ("Tentukan ukuran potong", "Mulai dari ukuran panel setelah dipotong, bukan ukuran jadi. Tambahkan kampuh atau kelim sebelum membuka alat. Pastikan satuan semua angka adalah sentimeter dan catat orientasi. Jika panel memiliki ukuran berbeda, kelompokkan lebih dahulu; kalkulator ini menangani satu ukuran yang diulang."),
                ("Isi lebar efektif dan jumlah", "Bagi lebar efektif kain dengan lebar potong panel, lalu bulatkan hasil ke bawah untuk jumlah panel per baris. Bagi jumlah panel yang dibutuhkan dengan panel per baris, lalu bulatkan ke atas untuk jumlah baris. Panjang dasar kain sama dengan jumlah baris dikali panjang potong panel."),
                ("Tambahkan cadangan yang dijelaskan", "Alat menerima tambahan panjang tetap dari pengguna dalam sentimeter. Angka itu dapat menampung kebutuhan uji potong atau margin kerja yang telah Anda pilih; alat tidak menebak persentase limbah. Motif berulang, arah serat, sambungan, dan cacat kain harus ditinjau pada sketsa nyata."),
            ], "example": "Enam panel 42 × 52 cm pada kain efektif 144 cm: tiga panel per baris, dua baris, panjang dasar 104 cm. Jika Anda menambah 10 cm, panjang rencana menjadi 114 cm.", "pitfall": "Luas total enam panel tidak cukup untuk menentukan panjang kain; susunan pada lebar gulungan juga menentukan hasil."},
        "en": {"title": "Lay out rectangular fabric panels", "summary": "Find how many pieces fit across each row before multiplying fabric length. The layout is transparent and deliberately simple.",
            "sections": [
                ("Start with cut dimensions", "Use each panel's cut dimensions, not finished dimensions. Add seam or hem allowance before opening the tool. Keep all inputs in centimetres and note orientation. Group different panel sizes separately; this calculator repeats one size only."),
                ("Enter usable width and count", "Divide usable fabric width by panel cut width and round down to find panels per row. Divide required panel count by panels per row and round up to find rows. Base fabric length is rows multiplied by panel cut length."),
                ("Add an explained margin", "The tool accepts a fixed extra length in centimetres chosen by you. It can represent test cutting or a work margin you have planned; it does not invent a waste percentage. Pattern repeat, grain, joins and defects still need a real cutting sketch."),
            ], "example": "Six 42 × 52 cm panels on 144 cm usable fabric: three per row, two rows, 104 cm base length. Add 10 cm and the planned length is 114 cm.", "pitfall": "Total area of six panels alone cannot determine fabric length; their arrangement across the bolt matters."},
    },
    {
        "slug": "pita-tepi-dan-keliling", "sources": ["measure", "nist"],
        "id": {"title": "Perkirakan pita tepi dari keliling", "summary": "Untuk bentuk persegi panjang, keliling memberi dasar panjang pita; sambungan dan cadangan tetap harus dicatat.",
            "sections": [
                ("Ukur tepi yang benar-benar dilapisi", "Untuk panel persegi panjang yang seluruh tepinya diberi pita, keliling adalah dua kali jumlah panjang dan lebar. Bila satu sisi tidak dilapisi, kurangi panjang sisi itu; alat situs ini menganggap keempat sisi dilapisi. Ukur pada garis pemasangan yang sesuai teknik, bukan sekadar menyalin ukuran proyek lain."),
                ("Tambahkan panjang sambungan", "Pita sering memerlukan panjang ekstra untuk sambungan awal dan akhir, mitra sudut, atau uji teknik. Masukkan tambahan panjang yang Anda pilih sendiri. Perhitungan tidak menentukan cara menyambung bias tape, lebar pita, maupun ketahanan hasil jahitan."),
                ("Cocokkan dengan kemasan", "Jika pita dibeli per gulung, bagi panjang rencana dengan panjang per gulung dan bulatkan ke atas. Periksa apakah panjang pada kemasan benar serta apakah ada sambungan yang tidak boleh ditempatkan pada sisi tertentu. Simpan sedikit sampel untuk menguji sudut sebelum memotong semua pita."),
            ], "example": "Panel 40 × 50 cm memiliki keliling 180 cm. Tambahan sambungan 20 cm menjadikan 200 cm; pita 150 cm per gulung memerlukan dua gulung.", "pitfall": "Jangan menganggap pita 180 cm tepat cukup untuk keliling 180 cm ketika ujungnya perlu disambung."},
        "en": {"title": "Estimate edging tape from perimeter", "summary": "For a rectangle, perimeter starts the tape estimate; joins and allowances still need recording.",
            "sections": [
                ("Measure the edges being bound", "A rectangle bound on all four sides has perimeter twice the sum of length and width. If one edge remains unbound, subtract that edge; this site's tool assumes all four sides are bound. Measure along the installation line appropriate to your technique rather than copying another project's dimensions."),
                ("Allow for joining", "Tape may need extra length for the starting and ending join, mitred corners or a technique test. Enter the extra length you choose. The arithmetic does not prescribe how to join bias tape, select its width or assess seam strength."),
                ("Compare pack lengths", "When tape is sold by the roll, divide planned length by length per roll and round up. Verify the pack label and whether joins must avoid certain edges. Try a small corner sample before cutting every length."),
            ], "example": "A 40 × 50 cm panel has a 180 cm perimeter. Add 20 cm for joining to reach 200 cm; at 150 cm per roll, two rolls are needed.", "pitfall": "Do not expect exactly 180 cm of tape to finish a 180 cm perimeter when its ends need joining."},
    },
    {
        "slug": "motif-berulang-dan-arah", "sources": ["usu", "measure"],
        "id": {"title": "Rencanakan motif berulang dan arah gambar", "summary": "Kain bermotif dapat membutuhkan lebih banyak panjang daripada susunan polos yang tampak cukup di kalkulator.",
            "sections": [
                ("Temukan satu ulangan motif", "Ukur jarak dari satu titik motif ke titik identik berikutnya pada arah panjang kain. Catat posisi motif terhadap tepi potong setiap panel. Jika gambar memiliki atas dan bawah, semua panel perlu diletakkan searah walau susunan terbalik akan lebih hemat."),
                ("Uji dengan sketsa skala", "Gambar lebar efektif kain serta kotak ukuran potong. Tandai titik awal motif pada tiap baris. Geser baris jika pola perlu bertemu pada sambungan, lalu ukur tambahan panjangnya. Hasil kalkulator panel adalah batas aritmetika untuk kotak berulang, bukan simulasi pencocokan motif."),
                ("Simpan ukuran motif", "Saat membeli, catat angka ulangan motif, arah kain, dan panjang tambahan yang benar-benar Anda tetapkan. Bila informasi tidak tersedia, jangan mengarang cadangan universal. Mintalah sampel atau pengukuran gulungan dan ulangi rencana sebelum membeli banyak kain."),
            ], "example": "Dua baris panel masing-masing 52 cm memberi panjang dasar 104 cm. Jika penyelarasan motif pada sketsa menambah 14 cm, masukkan 14 cm sebagai tambahan sehingga rencana menjadi 118 cm.", "pitfall": "Jangan menyebut angka tambahan motif sebagai persentase pasti untuk semua kain; pola dan orientasinya berbeda."},
        "en": {"title": "Plan repeat patterns and print direction", "summary": "Printed fabric can require more length than a plain-fabric layout suggests.",
            "sections": [
                ("Measure a repeat", "Measure from one motif point to its identical next point along the fabric length. Record motif placement against each panel's cut edge. If the print has an up and down, align all panels one way even when alternating direction would use less fabric."),
                ("Test with a scaled sketch", "Draw usable fabric width and rectangles at cut size. Mark each row's motif start. Move rows when prints must match at a seam, then measure the extra length. The panel calculator provides simple repeat-rectangle arithmetic, not print-matching simulation."),
                ("Keep the print measurement", "At purchase, record the measured repeat, direction and extra length you actually decided on. When repeat information is unavailable, avoid an invented universal margin. Ask for a sample or measure the bolt and redo the plan before a large purchase."),
            ], "example": "Two rows of 52 cm panels give 104 cm base length. If a scaled print plan adds 14 cm, enter 14 cm extra for a total of 118 cm.", "pitfall": "Do not present one extra percentage as correct for every print; designs and orientations differ."},
    },
    {
        "slug": "persiapan-kain-dan-susut", "sources": ["shrink", "usu"],
        "id": {"title": "Siapkan kain dan periksa penyusutan", "summary": "Perubahan ukuran setelah pencucian dapat mengalahkan perhitungan yang rapi. Ikuti label perawatan dan ukur ulang kain.",
            "sections": [
                ("Baca label perawatan", "Cara membersihkan bergantung pada serat, anyaman atau rajutan, finishing, dan instruksi produsen. Jangan mencuci bahan yang harus ditangani dengan cara lain. Untuk bahan yang boleh dicuci, persiapan sebelum potong membantu Anda melihat perubahan dimensi dan tampilan."),
                ("Bandingkan ukuran sebelum dan sesudah", "Jika punya sampel, ukur sisi panjang dan lebar sebelum perawatan, lalu ulangi sesudah kering sesuai instruksi. Persentase perubahan untuk tiap arah = (ukuran awal − ukuran akhir) ÷ ukuran awal × 100. Nilai dapat berbeda antara arah panjang dan lebar; satu angka umum tidak mewakili semua kain."),
                ("Ukur ulang untuk pola", "Setelah persiapan, ukur lebar efektif lagi dan periksa apakah tepi masih lurus. Pakai ukuran kain yang benar-benar akan dipotong untuk kalkulator. Uji sampel tidak menjamin seluruh gulungan identik, tetapi memberi bukti lebih baik daripada menebak."),
            ], "example": "Sampel sepanjang 50 cm menjadi 49 cm setelah perawatan sesuai label: perubahan panjang 2%. Ini hasil sampel tersebut, bukan klaim susut semua kain sejenis.", "pitfall": "Jangan menerapkan angka susut contoh pada bahan berbeda atau mengabaikan label perawatan."},
        "en": {"title": "Prepare fabric and check shrinkage", "summary": "Dimensional change after care can undo careful arithmetic. Follow the care label and remeasure the fabric.",
            "sections": [
                ("Read the care label", "Cleaning depends on fibre, weave or knit, finish and manufacturer instructions. Do not wash a material that needs another treatment. For washable fabric, preparation before cutting can reveal changes in size and appearance."),
                ("Compare measurements", "With a sample, measure length and width before care and again after drying as directed. Percentage change in each direction equals (initial size minus final size) divided by initial size, times 100. Length and width may change differently; one generic number does not describe every fabric."),
                ("Remeasure for the pattern", "After preparation, measure usable width again and check whether edges remain straight. Use the fabric dimensions you will actually cut in the calculator. A sample does not guarantee an entire bolt is identical, but it is better evidence than a guess."),
            ], "example": "A 50 cm sample becomes 49 cm long after label-directed care: 2% length change. That is this sample's result, not a claim for all similar fabric.", "pitfall": "Do not apply the example shrinkage to another material or ignore its care label."},
    },
    {
        "slug": "lembar-rencana-potong", "sources": ["measure", "usu", "shrink"],
        "id": {"title": "Buat lembar rencana sebelum membeli kain", "summary": "Daftar satu halaman menjaga hubungan antara ukuran jadi, ukuran potong, orientasi, dan panjang belanja.",
            "sections": [
                ("Catat kebutuhan benda", "Tuliskan jumlah panel dan ukuran jadi tiap panel. Di sebelahnya, catat perlakuan setiap tepi, ukuran potong, dan arah serat atau motif. Jika ada beberapa ukuran panel, buat kelompok terpisah. Jangan hanya menyimpan total meter kain tanpa alasan hitungnya."),
                ("Catat kondisi bahan", "Masukkan lebar kain sebenarnya, lebar yang disisihkan untuk tepi, dan lebar efektif. Tulis apakah kain telah dipersiapkan sesuai label dan apakah ada ulangan motif. Cantumkan tanggal serta sumber spesifikasi agar angka bisa diperiksa saat pilihan bahan berubah."),
                ("Tinjau hasil pembelian", "Gunakan alat panel untuk susunan sederhana dan alat pita tepi untuk keliling. Tambahan panjang adalah keputusan pengguna yang perlu alasan tertulis. Periksa ukuran gulungan, ketersediaan, dan aturan potong toko sebelum transaksi; kalkulator tidak menjamin stok atau kecocokan pola."),
            ], "example": "Catatan: 6 panel jadi 40 × 50 cm; potong 42 × 52 cm; kain efektif 144 cm; 3 panel/baris; 2 baris; dasar 104 cm; tambahan uji 10 cm; rencana 114 cm.", "pitfall": "Jangan menghapus ukuran dan orientasi asal setelah hanya menyimpan hasil akhir 1,14 m."},
        "en": {"title": "Make a cutting plan before buying", "summary": "A one-page note keeps finished size, cut size, orientation and purchase length connected.",
            "sections": [
                ("Record the object", "Write panel count and finished dimensions for each. Next to them, note edge treatments, cut dimensions and grain or print direction. Group different panel sizes separately. Do not save only a total fabric length without the calculation behind it."),
                ("Record the material", "Enter actual fabric width, width reserved at the edges and usable width. Note whether the material has been prepared as its care label allows and whether the print repeats. Include a date and specification source so the figures can be reviewed when fabric choice changes."),
                ("Review the buying figure", "Use the panel tool for a simple layout and the edging tool for perimeter. Extra length is a user decision that needs a written reason. Check roll size, availability and the shop's cutting rules before purchase; a calculator cannot promise stock or pattern fit."),
            ], "example": "Plan: 6 finished 40 × 50 cm panels; cut 42 × 52 cm; usable width 144 cm; 3 panels/row; 2 rows; 104 cm base; 10 cm test margin; 114 cm planned.", "pitfall": "Do not discard the source dimensions and orientation after saving only the final 1.14 m result."},
    },
]
