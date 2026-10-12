# Organon PDF Editions

All generated Organon PDFs are written directly into this directory. The
single `build.sh` accepts the volume and study kind; no per-edition build
directories or scripts are needed.
Kārikā outputs end in `-Karika.pdf`; Bhāṣya outputs end in `-Bhasya.pdf`.

Build a complete chapter:

```sh
./build.sh --volume 4 --kind karika
./build.sh --volume 4 --kind bhasya
```

Build a selected verse range or validate the configuration without invoking
Pandoc:

```sh
./build.sh --volume 4 --kind karika --start 1 --end 16 --output /tmp/karma-preview.pdf
./build.sh --volume 4 --kind karika --start 1 --end 16 --dry-run
```

Volumes 1–8 correspond to Dhātu, Indriya, Loka, Karma, Anuśaya, Mārga, Jñāna,
and Samāpatti. The default range is the current complete study sequence; Loka
Bhāṣya has 38 studies while Loka Kārikā has 102. Each build verifies that all
requested source files and the shared page-break/header assets exist before
starting Pandoc.

Requirements: Pandoc, XeLaTeX, FreeSerif, Lato, and FreeMono.
