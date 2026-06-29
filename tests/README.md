# 🐯 AING MAUNG COMPILER

Mini Compiler Bahasa Sunda Kasar berbasis Python.

AING MAUNG adalah bahasa pemrograman sederhana yang dibuat untuk memenuhi tugas UAS Mata Kuliah Teknik Kompilasi. Bahasa ini menggunakan keyword dan fungsi bawaan dalam Bahasa Sunda sebagai pengganti sintaks Python. Compiler ini menerapkan tahapan dasar pembuatan compiler mulai dari Lexical Analysis hingga Code Generation.

---

# 👨‍🎓 Informasi Proyek

**Nama Proyek:** AING MAUNG COMPILER

**Bahasa Implementasi:** Python

**Jenis Compiler:** Source-to-Source Compiler

**Target Output:** Python Code (`generated.py`)

**Pengembang:** Muhammad Sahrul Ajis (Revisi)

**NIM:** 221011400849

**Kelas:** 06TPLP025

**Mata Kuliah:** Teknik Kompilasi

**Universitas:** Universitas Pamulang

---

# 📌 Fitur Compiler

* ✅ Lexer
* ✅ Parser (Recursive Descent Parser)
* ✅ Parse Tree
* ✅ Abstract Syntax Tree (AST)
* ✅ Semantic Analysis
* ✅ Code Optimization
* ✅ Code Generation
* ✅ Eksekusi otomatis hasil generate
* ✅ Pesan Error menggunakan Bahasa Sunda

---

# 📖 Keyword Bahasa

| AING MAUNG | Python |
| ---------- | ------ |
| lamun      | if     |
| ari        | elif   |
| sanesna    | else   |
| keur       | for    |
| salila     | while  |
| gawe       | def    |
| balikkeun  | return |
| ngomong    | print  |
| nanya      | input  |
| rentang    | range  |
| panjang    | len    |
| enya       | True   |
| henteu     | False  |

---

# 🔣 Simbol Bahasa

| Simbol | Fungsi                  |
| ------ | ----------------------- |
| =      | Assignment              |
| +      | Penjumlahan             |
| -      | Pengurangan             |
| *      | Perkalian               |
| /      | Pembagian               |
| %      | Modulus                 |
| ==     | Sama Dengan             |
| !=     | Tidak Sama Dengan       |
| >      | Lebih Besar             |
| <      | Lebih Kecil             |
| >=     | Lebih Besar Sama Dengan |
| <=     | Lebih Kecil Sama Dengan |
| ( )    | Parameter / Expression  |
| { }    | Blok Program            |
| [ ]    | Array                   |
| ,      | Pemisah Parameter       |

---

# 📚 Grammar AING MAUNG (EBNF)

```text
program         ::= statement*

statement       ::= assignment
                 | function_definition
                 | function_call
                 | if_statement
                 | while_statement
                 | for_statement
                 | return_statement

assignment      ::= IDENTIFIER "=" expression

function_definition
                ::= "gawe" IDENTIFIER "(" parameters ")" "{" statement* "}"

parameters      ::= IDENTIFIER ("," IDENTIFIER)*

function_call   ::= IDENTIFIER "(" arguments ")"

arguments       ::= expression ("," expression)*

if_statement    ::= "lamun" "(" expression ")" "{" statement* "}"
                    ("ari" "(" expression ")" "{" statement* "}")*
                    ("sanesna" "{" statement* "}")?

while_statement ::= "salila" "(" expression ")" "{" statement* "}"

for_statement   ::= "keur" IDENTIFIER "dina"
                    "rentang" "(" expression "," expression ")"
                    "{" statement* "}"

expression      ::= comparison

comparison      ::= addition
                    (("=="|"!="|">"|"<"|">="|"<=") addition)*

addition        ::= multiplication
                    (("+"|"-") multiplication)*

multiplication  ::= factor
                    (("*"|"/"|"%") factor)*

factor          ::= NUMBER
                 | STRING
                 | IDENTIFIER
                 | function_call
                 | "(" expression ")"
                 | array
```

---

# 📝 Contoh Program

## Source Code AING MAUNG

```am
gawe tambah(a,b){
    balikkeun a+b
}

hasil = tambah(10,20)

ngomong("Hasil:")
ngomong(hasil)
```

## Hasil Generate Python

```python
def tambah(a, b):
    return a + b

hasil = tambah(10,20)

print("Hasil:")
print(hasil)
```

## Output

```text
Hasil:
30
```

---

# ⚙️ Alur Kompilasi

```text
Source Code (.am)
        │
        ▼
+-------------------+
|       Lexer       |
+-------------------+
        │
        ▼
+-------------------+
|      Parser       |
+-------------------+
        │
        ▼
+-------------------+
|    Parse Tree     |
+-------------------+
        │
        ▼
+-------------------+
|        AST        |
+-------------------+
        │
        ▼
+-------------------+
| Semantic Analysis |
+-------------------+
        │
        ▼
+-------------------+
| Code Optimization |
+-------------------+
        │
        ▼
+-------------------+
| Code Generation   |
+-------------------+
        │
        ▼
generated.py
        │
        ▼
Program Berjalan
```

---

# 📂 Struktur Folder

```text
AingMaung/
│
├── sample.am
├── generated.py
│
├── lexer.py
├── parser.py
├── parse_tree.py
├── parse_tree_printer.py
│
├── ast_nodes.py
├── ast_printer.py
│
├── semantic_analyzer.py
├── optimizer.py
├── code_generator.py
│
├── am_token.py
├── token_types.py
│
├── main.py
│
└── README.md
```

---

# 🔍 Tahapan Compiler

## 1. Lexical Analysis (Lexer)

Mengubah source code menjadi token.

Contoh:

```text
lamun ngaran == "Ajis"
```

menjadi

```text
LAMUN
IDENTIFIER
EQUAL
STRING
```

---

## 2. Syntax Analysis (Parser)

Parser menggunakan metode **Recursive Descent Parser** untuk memeriksa apakah susunan token sesuai dengan grammar yang telah didefinisikan.

---

## 3. Parse Tree

Membangun struktur pohon sintaks lengkap berdasarkan grammar bahasa AING MAUNG.

---

## 4. Abstract Syntax Tree (AST)

Menyederhanakan Parse Tree sehingga hanya menyimpan informasi yang diperlukan pada proses kompilasi berikutnya.

---

## 5. Semantic Analysis

Melakukan pemeriksaan terhadap:

* Variabel telah dideklarasikan
* Fungsi telah didefinisikan
* Assignment valid
* Pemanggilan fungsi valid
* Penggunaan array valid

Contoh pesan error:

```text
Kasalahan Semantic:
variabel 'ngaran' can acan dijieun.
```

---

## 6. Code Optimization

Compiler melakukan optimasi sederhana, di antaranya:

* Constant Folding
* Dead Code Elimination

---

## 7. Code Generation

AST diterjemahkan menjadi kode Python (`generated.py`) yang kemudian dijalankan secara otomatis.

---

# 🚀 Cara Menjalankan

```bash
python main.py
```

Compiler akan:

1. Membaca file `sample.am`
2. Melakukan proses Lexical Analysis
3. Melakukan Parsing
4. Membentuk Parse Tree
5. Membentuk AST
6. Melakukan Semantic Analysis
7. Melakukan Code Optimization
8. Menghasilkan `generated.py`
9. Menjalankan hasil generate secara otomatis

---

# 📹 Dokumentasi

Video demonstrasi minimal **15 menit** berisi:

* Desain Bahasa AING MAUNG
* Lexer
* Parser
* Parse Tree
* AST
* Semantic Analysis
* Code Optimization
* Code Generation
* Demonstrasi Program

---

# 🎯 Tujuan Proyek

Proyek ini dibuat sebagai implementasi konsep dasar compiler yang meliputi:

* Lexical Analysis
* Syntax Analysis
* Parse Tree
* Abstract Syntax Tree (AST)
* Semantic Analysis
* Code Optimization
* Code Generation

menggunakan bahasa daerah Indonesia, yaitu **Bahasa Sunda**, sebagai bentuk implementasi teori compiler sekaligus pelestarian bahasa daerah dalam dunia pemrograman.

---

# 🐯 Motto

> **"Lamun bisa dijieun ku Python, naha henteu ku AING MAUNG?"**

