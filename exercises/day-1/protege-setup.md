# Protégé Setup and Troubleshooting

This exercise requires **Protégé Desktop**, not WebProtégé. The desktop application includes direct support for OWL reasoners and can resolve the local BFO import supplied with the exercise.

## 1. Download Protégé Desktop

Use the official Protégé software page:

- [Protégé software and downloads](https://protege.stanford.edu/software/)

The course materials were prepared for **Protégé Desktop 5.6.9**. Later compatible 5.6.x releases should also work, but using the same version as the instructors reduces avoidable differences.

Official installation documentation:

- [Windows installation](https://protegeproject.github.io/protege/installation/windows/)
- [macOS installation](https://protegeproject.github.io/protege/installation/osx/)
- [Linux installation](https://protegeproject.github.io/protege/installation/linux/)
- [Protégé getting-started guide](https://protegeproject.github.io/protege/getting-started/)

Protégé's Windows, macOS, and Linux distributions include a Java runtime. A separate Java installation should not normally be necessary.

---

## 2. Install Protégé

### Windows

1. Download the Windows ZIP archive.
2. Right-click the ZIP file and select **Extract All**.
3. Move the extracted folder to a stable location.
4. Launch `Protege.exe`.

Do not run Protégé from inside the ZIP archive.

### macOS

1. Download the macOS ZIP archive.
2. Extract it.
3. Drag the Protégé application to the **Applications** folder.
4. Launch Protégé.

If macOS reports that the application cannot be opened:

1. Open **System Settings**.
2. Open **Privacy & Security**.
3. Find the entry concerning Protégé or Java.
4. Select **Allow** or **Open Anyway**, subject to your institution's security policies.
5. Launch Protégé again.

### Linux

1. Download the Linux `.tar.gz` archive.
2. Extract it:

   ```bash
   tar zxvf Protege-5.6.9-linux.tar.gz
   ```

3. Enter the extracted directory.
4. Launch:

   ```bash
   ./protege
   ```

---

## 3. Download the course repository correctly

The exercise uses a local ontology import. You must preserve the supplied folder structure.

### Recommended method

1. Open the course repository on GitHub.
2. Select **Code → Download ZIP**.
3. Extract the ZIP file fully.
4. Navigate to the Day 1 exercise folder.

Do not:

- open ontology files while they are still inside the downloaded ZIP;
- download only `patrol-boat-starter.ttl`;
- move `patrol-boat-starter.ttl` away from `catalog-v001.xml`;
- rename the `imports` folder.

The expected structure is:

```text
starter/
├── patrol-boat-starter.ttl
├── catalog-v001.xml
└── imports/
    └── bfo-core.ttl
```

---

## 4. Open the starter ontology

1. Launch Protégé Desktop.
2. Select **File → Open**.
3. Open:

   ```text
   starter/patrol-boat-starter.ttl
   ```

4. Wait for the ontology and its import to load.

Do not open `bfo-core.ttl` as the ontology you intend to edit. BFO is supplied as an imported dependency.

---

## 5. Confirm that BFO loaded locally

The starter ontology contains an `owl:imports` statement for BFO. The file `catalog-v001.xml` tells Protégé to satisfy that import using the local copy in `starter/imports/`.

To inspect imports:

1. Open the **Active Ontology** tab.
2. Find the **Direct Imports** section.

For more detail:

1. Select **Window → Views → Ontology views → Imported Ontologies**.
2. Confirm that BFO is listed.
3. Confirm that the loaded location points to the local `imports/bfo-core.ttl` file.

If only the import IRI is shown and no loaded location is shown, the import did not resolve.

Official documentation:

- [Imported Ontologies view](https://protegeproject.github.io/protege/views/imported-ontologies/)

---

## 6. Display human-readable labels

If the class hierarchy displays identifiers such as `BFO_0000040` instead of labels such as `material entity`:

1. Select **File → Preferences**.
2. Open the **Renderer** tab.
3. Choose **Render entities using annotation values**.
4. Select `rdfs:label` as the preferred annotation property if necessary.

Official guidance:

- [Human-readable entity names in Protégé](https://protegeproject.github.io/protege/getting-started/#human-readable-entity-names)

---

## 7. Select and run HermiT

Protégé Desktop includes the HermiT reasoner.

1. Select **Reasoner → HermiT**.
2. Start or synchronize the reasoner by selecting **Reasoner → Start reasoner** or by pressing:
   - **Ctrl+R** on Windows or Linux;
   - **Command+R** on macOS.

Inferred information is normally displayed with a pale yellow background.

Official guidance:

- [Protégé reasoning quick start](https://protegeproject.github.io/protege/getting-started/#reasoning)
- [Protégé reasoner preferences](https://protegeproject.github.io/protege/preferences/reasoner/)

---

# Troubleshooting

## Protégé does not start

### Windows

- Confirm that the archive was fully extracted.
- Launch `Protege.exe` from the extracted folder.
- If the normal launcher fails, run `run.bat` to display console output.
- Do not move only the executable away from the rest of the Protégé distribution.

### macOS

- Move the application to **Applications** before launching.
- Check **System Settings → Privacy & Security** for an approval option.
- Confirm that you downloaded the macOS package rather than the platform-independent package.

### Linux

- Confirm that the archive was extracted.
- In a terminal, enter the Protégé directory and run:

  ```bash
  ./protege
  ```

- If the file is not executable:

  ```bash
  chmod +x protege
  ./protege
  ```

---

## The BFO import does not load

Check all of the following:

1. You extracted the repository ZIP.
2. `patrol-boat-starter.ttl` and `catalog-v001.xml` are in the same folder.
3. `bfo-core.ttl` is located at:

   ```text
   starter/imports/bfo-core.ttl
   ```

4. The filename is exactly:

   ```text
   catalog-v001.xml
   ```

5. You did not rename or relocate the `imports` folder.
6. You opened the starter ontology from the extracted folder, not from a browser preview or compressed archive.

Then close Protégé and reopen the starter ontology.

---

## Protégé tries to retrieve BFO from the internet

This normally means that the XML catalog was not found or its mapping did not match the import IRI.

Verify that:

- the catalog is beside the starter ontology;
- the catalog contains a `<uri>` entry whose `name` exactly matches the IRI used in the starter ontology's `owl:imports` statement;
- the `uri` path in the catalog correctly points to the local BFO file;
- the catalog is well-formed XML.

Do not edit the BFO import IRI merely to point to a file on your own computer. The ontology should retain the authoritative ontology IRI; the catalog handles the local redirection.

---

## The ontology opens, but BFO classes are missing

1. Inspect **Active Ontology → Direct Imports**.
2. Open the **Imported Ontologies** view.
3. Confirm that BFO has a loaded file location.
4. Search globally for:

   ```text
   material entity
   ```

5. If labels are not displayed, configure the renderer as described above.

---

## `participates in` does not appear in the property selector

1. Confirm that BFO loaded.
2. Search for:

   ```text
   participates in
   ```

3. If Protégé displays identifiers instead of labels, configure the renderer.
4. Confirm that you are adding an **object-property assertion**, not a data-property assertion.

The BFO property has the IRI:

```text
http://purl.obolibrary.org/obo/BFO_0000056
```

---

## The Manchester expression is rejected

The intended expression is:

```text
PatrolBoat and 'participates in' some ActOfMotion
```

Check:

- capitalization of `PatrolBoat` and `ActOfMotion`;
- single quotation marks around `participates in`;
- that BFO loaded successfully;
- that all three entities appear in Protégé's autocomplete suggestions;
- that you entered the expression under **Equivalent To**, not as an annotation.

Names containing spaces must be enclosed in single quotation marks in Manchester syntax.

Official reference:

- [Protégé class-expression syntax](https://protegeproject.github.io/protege/class-expression-syntax/)

---

## HermiT is selected, but no inferred type appears

Check the asserted facts:

```text
patrol_boat_01 Type PatrolBoat
patrol_boat_01 participates in motion_01
motion_01 Type ActOfMotion
```

Check the class definition:

```text
MovingPatrolBoat EquivalentTo:
    PatrolBoat and 'participates in' some ActOfMotion
```

Then:

1. synchronize or restart HermiT;
2. select `patrol_boat_01`;
3. inspect the **Types** section;
4. ensure inferred types are enabled in **Reasoner Preferences**.

The inferred type may appear with a pale yellow background rather than as an ordinary asserted row.

---

## The reasoner says the ontology is inconsistent earlier than expected

Check whether an individual has accidentally been assigned incompatible types.

The deliberate inconsistency should occur only after `motion_01` is asserted to be both:

```text
ActOfMotion
SpeedMeasurementDatum
```

Remove unintended type assertions, synchronize HermiT, and try again.

---

## The reasoner remains inconsistent after the error is removed

1. Confirm that the incorrect assertion was removed from `motion_01`.
2. Search the ontology for other uses of `SpeedMeasurementDatum`.
3. Stop HermiT.
4. Save the ontology.
5. Restart HermiT.
6. If necessary, close and reopen the working ontology.

Do not delete imported BFO axioms in an attempt to restore consistency.

---

## Protégé is slow

This exercise ontology is small. Significant delay usually indicates an import or configuration problem.

- Confirm that BFO is loaded from the local file.
- Close other large ontologies in Protégé.
- Disable unnecessary reasoner display tasks under **File → Preferences → Reasoner**.
- Restart Protégé and reopen only the working ontology.

---

## Last-resort recovery

If your working file becomes difficult to repair:

1. close it without overwriting the starter;
2. reopen `patrol-boat-starter.ttl`;
3. save a new working copy;
4. repeat the exercise steps.

The starter ontology and imported BFO file should remain unchanged.
