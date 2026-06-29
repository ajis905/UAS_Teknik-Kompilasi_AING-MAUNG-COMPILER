# 🐯 AING MAUNG COMPILER

> **Ngoding ku Basa Sunda.**

AING MAUNG adalah sebuah **mini compiler** berbasis Python yang dibuat sebagai proyek **Ujian Akhir Semester (UAS) Mata Kuliah Teknik Kompilasi**.

Bahasa pemrograman ini menggunakan **Bahasa Sunda** sebagai keyword utama sehingga sintaks yang digunakan lebih dekat dengan bahasa daerah dibandingkan bahasa pemrograman konvensional.

Compiler ini dibangun melalui beberapa tahapan proses kompilasi, yaitu:

* Lexer
* Parser
* Parse Tree
* Abstract Syntax Tree (AST)
* Semantic Analysis
* Code Optimization
* Code Generation

Hasil akhir dari proses kompilasi adalah kode Python yang dapat dijalankan, kemudian compiler dapat dibangun menjadi file executable (.exe).

---

# Tujuan

Project ini dibuat untuk:

* Mempelajari konsep dasar pembuatan compiler.
* Mengimplementasikan tahapan-tahapan compiler menggunakan  Python.
* Memperkenalkan Bahasa Sunda sebagai inspirasi dalam perancangan bahasa pemrograman sederhana.

---

# Ekstensi File

Program AING MAUNG menggunakan ekstensi:

```text
.am
```

Contoh:

```text
halo.am
latihan.am
uas.am
```

---

# Keyword

| AING MAUNG | Python   |
| ---------- | -------- |
| lamun      | if       |
| ari        | elif     |
| sanesna    | else     |
| keur       | for      |
| salila     | while    |
| dina       | in       |
| gawe       | def      |
| balikkeun  | return   |
| eureun     | break    |
| tuluy      | continue |
| jeung      | and      |
| atawa      | or       |
| lain       | not      |
| asupkeun   | import   |

---

# Built-in Function

| AING MAUNG | Python  |
| ---------- | ------- |
| ngomong()  | print() |
| nanya()    | input() |
| panjang()  | len()   |
| rentang()  | range() |
| angka()    | int()   |
| tulisan()  | str()   |

---

# Nilai Boolean

| AING MAUNG | Python |
| ---------- | ------ |
| enya       | True   |
| henteu     | False  |

---

# Komentar

Komentar menggunakan keyword:

```text
catetan:
```

Contoh:

```text
catetan: Ieu program kahiji AING MAUNG
```

---

# Contoh Program

```text
catetan: Program Kahiji

ngaran = nanya("Saha ngaran maneh?")

lamun ngaran == "Ajis" {

    ngomong("Wilujeng Sumping!")

}

sanesna {

    ngomong("Halo!")

}
```

---

# Struktur Project

```text
AingMaung/
│
├── main.py
├── lexer.py
├── parser.py
├── ast_nodes.py
├── semantic.py
├── optimizer.py
├── code_generator.py
├── token_types.py
├── grammar.txt
├── sample.am
├── generated.py
├── README.md
│
└── output/
```

---

# Tahapan Compiler

```
Source Code (.am)
        │
        ▼
      Lexer
        │
        ▼
      Parser
        │
        ▼
    Parse Tree
        │
        ▼
        AST
        │
        ▼
Semantic Analysis
        │
        ▼
Code Optimization
        │
        ▼
Code Generation
        │
        ▼
 Generated Python
        │
        ▼
 Executable (.exe)
```

---

# Identitas Bahasa

Nama Bahasa:

**AING MAUNG**

Tagline:

> **Ngoding ku Basa Sunda.**

---

# Pengembang

Mini Compiler AING MAUNG

Muhammad Sahrul Ajis - 221011400849 - 06TPLP025

Mata Kuliah Teknik Kompilasi

Universitas Pamulang

Tahun 2026
