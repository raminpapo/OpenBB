# File Documentation: open-data-platform-SBOM-cargo.cdx.xml

## Metadata
- **Path**: `desktop/src-tauri/open-data-platform-SBOM-cargo.cdx.xml`
- **Size**: 1,115,786 bytes
- **Lines**: 21,940
- **Category**: text
- **Extension**: .xml

---

## Original Source

```
<?xml version="1.0" encoding="UTF-8"?>
<bom xmlns="http://cyclonedx.org/schema/bom/1.3" serialNumber="urn:uuid:073f9bc5-842d-47c7-8fd8-1877e64b52f3" version="1">
  <metadata>
    <timestamp>2025-10-22T15:34:16.482852000Z</timestamp>
    <tools>
      <tool>
        <vendor>CycloneDX</vendor>
        <name>cargo-cyclonedx</name>
        <version>0.5.7</version>
      </tool>
    </tools>
    <authors>
      <author>
        <name>OpenBB, Inc.</name>
      </author>
    </authors>
    <component type="application" bom-ref="path+file:///Users/darrenlee/github/OpenBB/desktop/src-tauri#openbb-platform@1.0.0">
      <author>OpenBB, Inc.</author>
      <name>openbb-platform</name>
      <version>1.0.0</version>
      <description>Open Data Platform by OpenBB. A desktop application for managing virtual environments, application backend servers.</description>
      <scope>required</scope>
      <licenses>
        <expression>AGPL-3.0</expression>
      </licenses>
      <purl>pkg:cargo/openbb-platform@1.0.0?download_url=file://.</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/OpenBB-finance/OpenBB/</url>
        </reference>
      </externalReferences>
      <components>
        <component type="application" bom-ref="path+file:///Users/darrenlee/github/OpenBB/desktop/src-tauri#openbb-platform@1.0.0 bin-target-0">
          <name>openbb-platform</name>
          <version>1.0.0</version>
          <purl>pkg:cargo/openbb-platform@1.0.0?download_url=file://.#src/main.rs</purl>
        </component>
      </components>
    </component>
    <properties>
      <property name="cdx:rustc:sbom:target:triple">x86_64-apple-darwin</property>
    </properties>
  </metadata>
  <components>
    <component type="library" bom-ref="git+https://github.com/tauri-apps/fix-path-env-rs#fix-path-env@0.0.0">
      <author>Tauri Programme within The Commons Conservancy</author>
      <name>fix-path-env</name>
      <version>0.0.0</version>
      <scope>required</scope>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/fix-path-env@0.0.0?vcs_url=git%2Bhttps://github.com/tauri-apps/fix-path-env-rs%40c4c45d503ea115a839aae718d02f79e7c7f0f673</purl>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#addr2line@0.25.1">
      <name>addr2line</name>
      <version>0.25.1</version>
      <description>A cross-platform symbolication library written in Rust, using `gimli`</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1b5d307320b3181d6d7954e663bd7c774a838b8220fe0593c86d9fb09f498b4b</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/addr2line@0.25.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/addr2line</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/gimli-rs/addr2line</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#adler2@2.0.1">
      <author>Jonas Schievink &lt;jonasschievink@gmail.com&gt;, oyvindln &lt;oyvindln@users.noreply.github.com&gt;</author>
      <name>adler2</name>
      <version>2.0.1</version>
      <description>A simple clean-room implementation of the Adler-32 checksum</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">320119579fcad9c21884f5c4861d16174d0e06250625266f50fe6898340abefa</hash>
      </hashes>
      <licenses>
        <expression>0BSD OR MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/adler2@2.0.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/adler2/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oyvindln/adler2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#aead@0.5.2">
      <author>RustCrypto Developers</author>
      <name>aead</name>
      <version>0.5.2</version>
      <description>Traits for Authenticated Encryption with Associated Data (AEAD) algorithms, such as AES-GCM as ChaCha20Poly1305, which provide a high-level API </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d122413f284cf2d62fb1b7db97e02edb8cda96d769b16e443a4f6195e35662b0</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/aead@0.5.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/aead</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/traits</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#aes-gcm@0.10.3">
      <author>RustCrypto Developers</author>
      <name>aes-gcm</name>
      <version>0.10.3</version>
      <description>Pure Rust implementation of the AES-GCM (Galois/Counter Mode) Authenticated Encryption with Associated Data (AEAD) Cipher with optional architecture-specific hardware acceleration </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">831010a0f742e1209b3bcea8fab6a8e149051ba6099432c8cb2cc117dec3ead1</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/aes-gcm@0.10.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/aes-gcm</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/AEADs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#aes@0.8.4">
      <author>RustCrypto Developers</author>
      <name>aes</name>
      <version>0.8.4</version>
      <description>Pure Rust implementation of the Advanced Encryption Standard (a.k.a. Rijndael)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b169f7a6d4742236a0a00c541b845991d0ac43e546831af1249753ab4c3aa3a0</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/aes@0.8.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/aes</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/block-ciphers</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ahash@0.7.8">
      <author>Tom Kaitchuck &lt;Tom.Kaitchuck@gmail.com&gt;</author>
      <name>ahash</name>
      <version>0.7.8</version>
      <description>A non-cryptographic hash function using AES-NI for high performance</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">891477e0c6a8957309ee5c45a6368af3ae14bb510732d2684ffa19af310920f9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/ahash@0.7.8</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/ahash</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/tkaitchuck/ahash</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ahash@0.8.12">
      <author>Tom Kaitchuck &lt;Tom.Kaitchuck@gmail.com&gt;</author>
      <name>ahash</name>
      <version>0.8.12</version>
      <description>A non-cryptographic hash function using AES-NI for high performance</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5a15f179cd60c4584b8a8c596927aadc462e27f2ca70c04e0071964a73ba7a75</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/ahash@0.8.12</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/ahash</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/tkaitchuck/ahash</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#aho-corasick@1.1.3">
      <author>Andrew Gallant &lt;jamslam@gmail.com&gt;</author>
      <name>aho-corasick</name>
      <version>1.1.3</version>
      <description>Fast multiple substring searching.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">8e60d3430d3a69478ad0993f19238d2df97c507009a52b3c10addcd7f6bcb916</hash>
      </hashes>
      <licenses>
        <expression>Unlicense OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/aho-corasick@1.1.3</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/BurntSushi/aho-corasick</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/BurntSushi/aho-corasick</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#aligned-vec@0.6.4">
      <author>sarah &lt;&gt;</author>
      <name>aligned-vec</name>
      <version>0.6.4</version>
      <description>Aligned vector and box containers</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">dc890384c8602f339876ded803c97ad529f3842aba97f6392b3dba0dd171769b</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/aligned-vec@0.6.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sarah-ek/aligned-vec/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#alloc-no-stdlib@2.0.4">
      <author>Daniel Reiter Horn &lt;danielrh@dropbox.com&gt;</author>
      <name>alloc-no-stdlib</name>
      <version>2.0.4</version>
      <description>A dynamic allocator that may be used with or without the stdlib. This allows a package with nostd to allocate memory dynamically and be used either with a custom allocator, items on the stack, or by a package that wishes to simply use Box&lt;&gt;. It also provides options to use calloc or a mutable global variable for pre-zeroed memory</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">cc7bb162ec39d46ab1ca8c77bf72e890535becd1751bb45f64c597edb4c8c6b3</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/alloc-no-stdlib@2.0.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://raw.githubusercontent.com/dropbox/rust-alloc-no-stdlib/master/tests/lib.rs</url>
        </reference>
        <reference type="website">
          <url>https://github.com/dropbox/rust-alloc-no-stdlib</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dropbox/rust-alloc-no-stdlib</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#alloc-stdlib@0.2.2">
      <author>Daniel Reiter Horn &lt;danielrh@dropbox.com&gt;</author>
      <name>alloc-stdlib</name>
      <version>0.2.2</version>
      <description>A dynamic allocator example that may be used with the stdlib</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">94fb8275041c72129eb51b7d0322c29b8387a0386127718b096429201a5d6ece</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/alloc-stdlib@0.2.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://raw.githubusercontent.com/dropbox/rust-alloc-no-stdlib/master/alloc-stdlib/tests/lib.rs</url>
        </reference>
        <reference type="website">
          <url>https://github.com/dropbox/rust-alloc-no-stdlib</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dropbox/rust-alloc-no-stdlib</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#allocator-api2@0.2.21">
      <author>Zakarum &lt;zaq.dev@icloud.com&gt;</author>
      <name>allocator-api2</name>
      <version>0.2.21</version>
      <description>Mirror of Rust's allocator API</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">683d7910e743518b0e34f1186f92494becacb047c7b6bf616c96772180fef923</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/allocator-api2@0.2.21</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/allocator-api2</url>
        </reference>
        <reference type="website">
          <url>https://github.com/zakarumych/allocator-api2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/zakarumych/allocator-api2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#anstream@0.6.21">
      <name>anstream</name>
      <version>0.6.21</version>
      <description>IO stream adapters for writing colored text that will gracefully degrade according to your terminal's capabilities.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">43d5b281e737544384e969a5ccad3f1cdd24b48086a0fc1b2a5262a26b8f4f4a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/anstream@0.6.21</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-cli/anstyle.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#anstyle-parse@0.2.7">
      <name>anstyle-parse</name>
      <version>0.2.7</version>
      <description>Parse ANSI Style Escapes</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4e7644824f0aa2c7b9384579234ef10eb7efb6a0deb83f9630a49594dd9c15c2</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/anstyle-parse@0.2.7</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-cli/anstyle.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#anstyle-query@1.1.4">
      <name>anstyle-query</name>
      <version>1.1.4</version>
      <description>Look up colored console capabilities</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9e231f6134f61b71076a3eab506c379d4f36122f2af15a9ff04415ea4c3339e2</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/anstyle-query@1.1.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-cli/anstyle.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#anstyle@1.0.13">
      <name>anstyle</name>
      <version>1.0.13</version>
      <description>ANSI text styling</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5192cca8006f1fd4f7237516f40fa183bb07f8fbdfedaa0036de5ea9b0b45e78</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/anstyle@1.0.13</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-cli/anstyle.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#anyhow@1.0.100">
      <author>David Tolnay &lt;dtolnay@gmail.com&gt;</author>
      <name>anyhow</name>
      <version>1.0.100</version>
      <description>Flexible concrete Error type built on std::error::Error</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">a23eb6b1614318a8071c9b2521f36b424b2c83db5eb3a0fead4a6c0809af6e61</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/anyhow@1.0.100</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/anyhow</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dtolnay/anyhow</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#apple-bundles@0.19.0">
      <author>Gregory Szorc &lt;gregory.szorc@gmail.com&gt;</author>
      <name>apple-bundles</name>
      <version>0.19.0</version>
      <description>Interface with Apple bundle primitives</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">abb7c27ee2ca7826adfdc84228cd4c5a84ab57b0a11d269d1d7cd0615238e5a2</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/apple-bundles@0.19.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/indygreg/apple-platform-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/indygreg/apple-platform-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#apple-codesign@0.27.0">
      <author>Gregory Szorc &lt;gregory.szorc@gmail.com&gt;</author>
      <name>apple-codesign</name>
      <version>0.27.0</version>
      <description>Pure Rust interface to code signing on Apple platforms</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">329820aac7259ca0529d3cc21dd3b4c11651225dfce9e0ce25b121b23f923164</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/apple-codesign@0.27.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/indygreg/apple-platform-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/indygreg/apple-platform-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#apple-flat-package@0.18.0">
      <author>Gregory Szorc &lt;gregory.szorc@gmail.com&gt;</author>
      <name>apple-flat-package</name>
      <version>0.18.0</version>
      <description>Apple flat package (.pkg) format handling</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b6adc520e05304de5ec383487786fa20e9c636fe972e59719cdd93621a2db6f1</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/apple-flat-package@0.18.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/indygreg/apple-platform-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/indygreg/apple-platform-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#apple-xar@0.18.0">
      <author>Gregory Szorc &lt;gregory.szorc@gmail.com&gt;</author>
      <name>apple-xar</name>
      <version>0.18.0</version>
      <description>XAR archive reading and writing</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">844e00dc1e665b3cf0bba745aa9c6464292ca512db0c11384511586701eb0335</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/apple-xar@0.18.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/indygreg/apple-platform-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/indygreg/apple-platform-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ar@0.9.0">
      <author>Matthew D. Steele &lt;mdsteele@alum.mit.edu&gt;</author>
      <name>ar</name>
      <version>0.9.0</version>
      <description>A library for encoding/decoding Unix archive files.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d67af77d68a931ecd5cbd8a3b5987d63a1d1d1278f7f6a60ae33db485cdebb69</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/ar@0.9.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/mdsteele/rust-ar</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#arg_enum_proc_macro@0.3.4">
      <author>Luca Barbato &lt;lu_zero@gentoo.org&gt;</author>
      <name>arg_enum_proc_macro</name>
      <version>0.3.4</version>
      <description>A procedural macro compatible with clap arg_enum</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0ae92a5119aa49cdbcf6b9f893fe4e1d98b04ccbf82ee0584ad948a44a734dea</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/arg_enum_proc_macro@0.3.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/lu-zero/arg_enum_proc_macro</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#arrayref@0.3.9">
      <author>David Roundy &lt;roundyd@physics.oregonstate.edu&gt;</author>
      <name>arrayref</name>
      <version>0.3.9</version>
      <description>Macros to take array references of slices</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">76a2e8124351fda1ef8aaaa3bbd7ebbcb486bbcd4225aca0aa0d84bb2db8fecb</hash>
      </hashes>
      <licenses>
        <expression>BSD-2-Clause</expression>
      </licenses>
      <purl>pkg:cargo/arrayref@0.3.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/arrayref</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/droundy/arrayref</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#arrayvec@0.7.6">
      <author>bluss</author>
      <name>arrayvec</name>
      <version>0.7.6</version>
      <description>A vector with fixed capacity, backed by an array (it can be stored on the stack too). Implements fixed capacity ArrayVec and ArrayString.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7c02d123df017efcdfbd739ef81735b36c5ba83ec3c59c80a9d7ecc718f92e50</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/arrayvec@0.7.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/arrayvec/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/bluss/arrayvec</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#asn1-rs-derive@0.4.0">
      <author>Pierre Chifflier &lt;chifflier@wzdftpd.net&gt;</author>
      <name>asn1-rs-derive</name>
      <version>0.4.0</version>
      <description>Derive macros for the `asn1-rs` crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">726535892e8eae7e70657b4c8ea93d26b8553afb1ce617caee529ef96d7dee6c</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/asn1-rs-derive@0.4.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/rusticata/asn1-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rusticata/asn1-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#asn1-rs-impl@0.1.0">
      <author>Pierre Chifflier &lt;chifflier@wzdftpd.net&gt;</author>
      <name>asn1-rs-impl</name>
      <version>0.1.0</version>
      <description>Implementation details for the `asn1-rs` crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2777730b2039ac0f95f093556e61b6d26cebed5393ca6f152717777cec3a42ed</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/asn1-rs-impl@0.1.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/rusticata/asn1-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rusticata/asn1-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#asn1-rs@0.5.2">
      <author>Pierre Chifflier &lt;chifflier@wzdftpd.net&gt;</author>
      <name>asn1-rs</name>
      <version>0.5.2</version>
      <description>Parser/encoder for ASN.1 BER/DER data</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7f6fd5ddaf0351dff5b8da21b2fb4ff8e08ddd02857f0bf69c47639106c0fff0</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/asn1-rs@0.5.2</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/rusticata/asn1-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rusticata/asn1-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#assert-unchecked@0.1.2">
      <author>skmendez</author>
      <name>assert-unchecked</name>
      <version>0.1.2</version>
      <description>Unsafe assertions that allow for optimizations in release mode.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7330592adf847ee2e3513587b4db2db410a0d751378654e7e993d9adcbe5c795</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/assert-unchecked@0.1.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/assert-unchecked/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/skmendez/assert-unchecked</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#async-trait@0.1.89">
      <author>David Tolnay &lt;dtolnay@gmail.com&gt;</author>
      <name>async-trait</name>
      <version>0.1.89</version>
      <description>Type erasure for async trait methods</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9035ad2d096bed7955a320ee7e2230574d28fd3c3a0f186cbea1ff3c7eed5dbb</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/async-trait@0.1.89</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/async-trait</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dtolnay/async-trait</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#atomic-waker@1.1.2">
      <author>Stjepan Glavina &lt;stjepang@gmail.com&gt;, Contributors to futures-rs</author>
      <name>atomic-waker</name>
      <version>1.1.2</version>
      <description>A synchronization primitive for task wakeup</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1505bd5d3d116872e7271a6d4e16d81d0c8570876c8de68093a09ac269d8aac0</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/atomic-waker@1.1.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/smol-rs/atomic-waker</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#autocfg@1.5.0">
      <author>Josh Stone &lt;cuviper@gmail.com&gt;</author>
      <name>autocfg</name>
      <version>1.5.0</version>
      <description>Automatic cfg for Rust compiler features</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">c08606f8c3cbf4ce6ec8e28fb0014a2c086708fe954eaa885384a6165172e7e8</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/autocfg@1.5.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/autocfg/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/cuviper/autocfg</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#av1-grain@0.2.4">
      <name>av1-grain</name>
      <version>0.2.4</version>
      <description>Helpers for generating and parsing AV1 film grain data</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4f3efb2ca85bc610acfa917b5aaa36f3fcbebed5b3182d7f877b02531c4b80c8</hash>
      </hashes>
      <licenses>
        <expression>BSD-2-Clause</expression>
      </licenses>
      <purl>pkg:cargo/av1-grain@0.2.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/av1-grain</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-av/av1-grain</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-av/av1-grain</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#avif-serialize@0.8.6">
      <author>Kornel Lesiński &lt;kornel@geekhood.net&gt;</author>
      <name>avif-serialize</name>
      <version>0.8.6</version>
      <description>Minimal writer for AVIF header structure (MPEG/HEIF/MIAF/ISO-BMFF)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">47c8fbc0f831f4519fe8b810b6a7a91410ec83031b8233f730a0480029f6a23f</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/avif-serialize@0.8.6</purl>
      <externalReferences>
        <reference type="website">
          <url>https://lib.rs/avif-serialize</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/kornelski/avif-serialize</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#axum-core@0.5.5">
      <name>axum-core</name>
      <version>0.5.5</version>
      <description>Core types and traits for axum</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">59446ce19cd142f8833f856eb31f3eb097812d1479ab224f54d72428ca21ea22</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/axum-core@0.5.5</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/tokio-rs/axum</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/tokio-rs/axum</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#axum@0.8.6">
      <name>axum</name>
      <version>0.8.6</version>
      <description>Web framework that focuses on ergonomics and modularity</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">8a18ed336352031311f4e0b4dd2ff392d4fbb370777c9d18d7fc9d7359f73871</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/axum@0.8.6</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/tokio-rs/axum</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/tokio-rs/axum</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#backtrace@0.3.76">
      <author>The Rust Project Developers</author>
      <name>backtrace</name>
      <version>0.3.76</version>
      <description>A library to acquire a stack trace (backtrace) at runtime in a Rust program. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bb531853791a215d7c62a30daf0dde835f381ab5de4589cfe7c649d2cbe92bd6</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/backtrace@0.3.76</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/backtrace</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-lang/backtrace-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/backtrace-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#base16ct@0.2.0">
      <author>RustCrypto Developers</author>
      <name>base16ct</name>
      <version>0.2.0</version>
      <description>Pure Rust implementation of Base16 a.k.a hexadecimal (RFC 4648) which avoids any usages of data-dependent branches/LUTs and thereby provides portable "best effort" constant-time operation and embedded-friendly no_std support </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4c7f02d4ea65f2c1853089ffd8d2787bdbc63de2f0d29dedbcf8ccdfa0ccd4cf</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/base16ct@0.2.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/base16ct</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/formats/tree/master/base16ct</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#base64@0.13.1">
      <author>Alice Maz &lt;alice@alicemaz.com&gt;, Marshall Pierce &lt;marshall@mpierce.org&gt;</author>
      <name>base64</name>
      <version>0.13.1</version>
      <description>encodes and decodes base64 as bytes or utf8</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9e1b586273c5702936fe7b7d6896644d8be71e6314cfe09d3167c95f712589e8</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/base64@0.13.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/base64</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/marshallpierce/rust-base64</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#base64@0.21.7">
      <author>Alice Maz &lt;alice@alicemaz.com&gt;, Marshall Pierce &lt;marshall@mpierce.org&gt;</author>
      <name>base64</name>
      <version>0.21.7</version>
      <description>encodes and decodes base64 as bytes or utf8</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9d297deb1925b89f2ccc13d7635fa0714f12c87adce1c75356b39ca9b7178567</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/base64@0.21.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/base64</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/marshallpierce/rust-base64</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#base64@0.22.1">
      <author>Marshall Pierce &lt;marshall@mpierce.org&gt;</author>
      <name>base64</name>
      <version>0.22.1</version>
      <description>encodes and decodes base64 as bytes or utf8</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">72b3254f16251a8381aa12e40e3c4d2f0199f8c6508fbecb9d91f575e0fbb8c6</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/base64@0.22.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/base64</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/marshallpierce/rust-base64</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#base64ct@1.8.0">
      <author>RustCrypto Developers</author>
      <name>base64ct</name>
      <version>1.8.0</version>
      <description>Pure Rust implementation of Base64 (RFC 4648) which avoids any usages of data-dependent branches/LUTs and thereby provides portable "best effort" constant-time operation and embedded-friendly no_std support </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">55248b47b0caf0546f7988906588779981c43bb1bc9d0c44087278f80cdb44ba</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/base64ct@1.8.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/base64ct</url>
        </reference>
        <reference type="website">
          <url>https://github.com/RustCrypto/formats/tree/master/base64ct</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/formats</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bcder@0.7.6">
      <author>NLnet Labs &lt;rust-team@nlnetlabs.nl&gt;</author>
      <name>bcder</name>
      <version>0.7.6</version>
      <description>Handling of data encoded in BER, CER, and DER.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1f7c42c9913f68cf9390a225e81ad56a5c515347287eb98baa710090ca1de86d</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/bcder@0.7.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bcder/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/nlnetlabs/bcder</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bincode@1.3.3">
      <author>Ty Overby &lt;ty@pre-alpha.com&gt;, Francesco Mazzoli &lt;f@mazzo.li&gt;, David Tolnay &lt;dtolnay@gmail.com&gt;, Zoey Riordan &lt;zoey@dos.cafe&gt;</author>
      <name>bincode</name>
      <version>1.3.3</version>
      <description>A binary serialization / deserialization strategy that uses Serde for transforming structs into bytes and vice versa!</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b1f45e9417d87227c7a56d22e471c6206462cba514c7590c09aff4cf6d1ddcad</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/bincode@1.3.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bincode</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/bincode</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bit-set@0.8.0">
      <author>Alexis Beingessner &lt;a.beingessner@gmail.com&gt;</author>
      <name>bit-set</name>
      <version>0.8.0</version>
      <description>A set of bits</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">08807e080ed7f9d5433fa9b275196cfc35414f66a0c79d864dc51a0d825231a3</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/bit-set@0.8.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bit-set/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/contain-rs/bit-set</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/contain-rs/bit-set</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bit-vec@0.8.0">
      <author>Alexis Beingessner &lt;a.beingessner@gmail.com&gt;</author>
      <name>bit-vec</name>
      <version>0.8.0</version>
      <description>A vector of bits</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5e764a1d40d510daf35e07be9eb06e75770908c27d411ee6c92109c9840eaaf7</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/bit-vec@0.8.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bit-vec/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/contain-rs/bit-vec</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/contain-rs/bit-vec</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bit_field@0.10.3">
      <author>Philipp Oppermann &lt;dev@phil-opp.com&gt;</author>
      <name>bit_field</name>
      <version>0.10.3</version>
      <description>Simple bit field trait providing get_bit, get_bits, set_bit, and set_bits methods for Rust's integral types.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1e4b40c7323adcfc0a41c4b88143ed58346ff65a288fc144329c5c45e05d70c6</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/bit_field@0.10.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bit_field</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/phil-opp/rust-bit-field</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bitflags@1.3.2">
      <author>The Rust Project Developers</author>
      <name>bitflags</name>
      <version>1.3.2</version>
      <description>A macro to generate structures which behave like bitflags. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bef38d45163c2f1dde094a7dfd33ccf595c92905c8f8f4fdc18d06fb1037718a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/bitflags@1.3.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bitflags</url>
        </reference>
        <reference type="website">
          <url>https://github.com/bitflags/bitflags</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/bitflags/bitflags</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bitflags@2.9.4">
      <author>The Rust Project Developers</author>
      <name>bitflags</name>
      <version>2.9.4</version>
      <description>A macro to generate structures which behave like bitflags. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2261d10cca569e4643e526d8dc2e62e433cc8aba21ab764233731f8d369bf394</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/bitflags@2.9.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bitflags</url>
        </reference>
        <reference type="website">
          <url>https://github.com/bitflags/bitflags</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/bitflags/bitflags</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bitstream-io@2.6.0">
      <author>Brian Langenberger &lt;bjl@usa.net&gt;</author>
      <name>bitstream-io</name>
      <version>2.6.0</version>
      <description>Library for reading/writing un-aligned values from/to streams in big-endian and little-endian formats.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6099cdc01846bc367c4e7dd630dc5966dccf36b652fae7a74e17b640411a91b2</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/bitstream-io@2.6.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bitstream-io/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/tuffy/bitstream-io</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/tuffy/bitstream-io</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bitvec-nom2@0.2.1">
      <author>contact@geoffroycouprie.com</author>
      <name>bitvec-nom2</name>
      <version>0.2.1</version>
      <description>Bit level parsing for nom with bitvec</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d988fcc40055ceaa85edc55875a08f8abd29018582647fd82ad6128dba14a5f0</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/bitvec-nom2@0.2.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/nom-bitvec</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-bakery/nom-bitvec</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bitvec@1.0.1">
      <name>bitvec</name>
      <version>1.0.1</version>
      <description>Addresses memory by bits, for packed collections and bitfields</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1bc2832c24239b0141d5674bb9174f9d68a8b5b3f2753311927c172ca46f7e9c</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/bitvec@1.0.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bitvec/latest/bitvec</url>
        </reference>
        <reference type="website">
          <url>https://bitvecto-rs.github.io/bitvec</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/bitvecto-rs/bitvec</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#block-buffer@0.10.4">
      <author>RustCrypto Developers</author>
      <name>block-buffer</name>
      <version>0.10.4</version>
      <description>Buffer type for block processing of data</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3078c7629b62d3f0439517fa394996acacc5cbc91c5a20d8c658e77abd503a71</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/block-buffer@0.10.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/block-buffer</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/utils</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#block-padding@0.3.3">
      <author>RustCrypto Developers</author>
      <name>block-padding</name>
      <version>0.3.3</version>
      <description>Padding and unpadding of messages divided into blocks.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">a8894febbff9f758034a5b8e12d87918f56dfc64a8e1fe757d65e29041538d93</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/block-padding@0.3.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/block-padding</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/utils</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#block2@0.5.1">
      <author>Steven Sheldon, Mads Marquart &lt;mads@marquart.dk&gt;</author>
      <name>block2</name>
      <version>0.5.1</version>
      <description>Apple's C language extension of blocks</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2c132eebf10f5cad5289222520a4a058514204aed6d791f1cf4fe8088b82d15f</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/block2@0.5.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/block2/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#block2@0.6.2">
      <author>Mads Marquart &lt;mads@marquart.dk&gt;</author>
      <name>block2</name>
      <version>0.6.2</version>
      <description>Apple's C language extension of blocks</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">cdeb9d870516001442e364c5220d3574d2da8dc765554b4a617230d33fa58ef5</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/block2@0.6.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#borrow-or-share@0.2.2">
      <author>Scallop Ye &lt;yescallop@gmail.com&gt;</author>
      <name>borrow-or-share</name>
      <version>0.2.2</version>
      <description>Traits for either borrowing or sharing data.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3eeab4423108c5d7c744f4d234de88d18d636100093ae04caf4825134b9c3a32</hash>
      </hashes>
      <licenses>
        <expression>MIT-0</expression>
      </licenses>
      <purl>pkg:cargo/borrow-or-share@0.2.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/borrow-or-share</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/yescallop/borrow-or-share</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#borsh-derive@1.5.7">
      <author>Near Inc &lt;hello@nearprotocol.com&gt;</author>
      <name>borsh-derive</name>
      <version>1.5.7</version>
      <description>Binary Object Representation Serializer for Hashing </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">fdd1d3c0c2f5833f22386f252fe8ed005c7f59fdcddeef025c01b4c3b9fd9ac3</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/borsh-derive@1.5.7</purl>
      <externalReferences>
        <reference type="website">
          <url>https://borsh.io</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/near/borsh-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#borsh@1.5.7">
      <author>Near Inc &lt;hello@near.org&gt;</author>
      <name>borsh</name>
      <version>1.5.7</version>
      <description>Binary Object Representation Serializer for Hashing </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ad8646f98db542e39fc66e68a20b2144f6a732636df7c2354e74645faaa433ce</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/borsh@1.5.7</purl>
      <externalReferences>
        <reference type="website">
          <url>https://borsh.io</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/near/borsh-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#brotli-decompressor@5.0.0">
      <author>Daniel Reiter Horn &lt;danielrh@dropbox.com&gt;, The Brotli Authors</author>
      <name>brotli-decompressor</name>
      <version>5.0.0</version>
      <description>A brotli decompressor that with an interface avoiding the rust stdlib. This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. Alternatively, --features=unsafe turns off array bounds checks and memory initialization but provides a safe interface for the caller.  Without adding the --features=unsafe argument, all included code is safe. For compression in addition to this library, download https://github.com/dropbox/rust-brotli </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">874bb8112abecc98cbd6d81ea4fa7e94fb9449648c93cc89aa40c81c24d7de03</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/brotli-decompressor@5.0.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://github.com/dropbox/rust-brotli-decompressor/blob/master/README.md</url>
        </reference>
        <reference type="website">
          <url>https://github.com/dropbox/rust-brotli-decompressor</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dropbox/rust-brotli-decompressor</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#brotli@8.0.2">
      <author>Daniel Reiter Horn &lt;danielrh@dropbox.com&gt;, The Brotli Authors</author>
      <name>brotli</name>
      <version>8.0.2</version>
      <description>A brotli compressor and decompressor that with an interface avoiding the rust stdlib. This makes it suitable for embedded devices and kernels. It is designed with a pluggable allocator so that the standard lib's allocator may be employed. The default build also includes a stdlib allocator and stream interface. Disable this with --features=no-stdlib. All included code is safe.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4bd8b9603c7aa97359dbd97ecf258968c95f3adddd6db2f7e7a5bef101c84560</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause AND MIT</expression>
      </licenses>
      <purl>pkg:cargo/brotli@8.0.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/brotli/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/dropbox/rust-brotli</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dropbox/rust-brotli</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bstr@1.12.0">
      <author>Andrew Gallant &lt;jamslam@gmail.com&gt;</author>
      <name>bstr</name>
      <version>1.12.0</version>
      <description>A string type that is not required to be valid UTF-8.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">234113d19d0d7d613b40e86fb654acf958910802bcceab913a4f9e7cda03b1a4</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/bstr@1.12.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bstr</url>
        </reference>
        <reference type="website">
          <url>https://github.com/BurntSushi/bstr</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/BurntSushi/bstr</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#built@0.7.7">
      <author>Lukas Lueg &lt;lukas.lueg@gmail.com&gt;</author>
      <name>built</name>
      <version>0.7.7</version>
      <description>Provides a crate with information from the time it was built.</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">56ed6191a7e78c36abdb16ab65341eefd73d64d303fffccdbb00d51e4205967b</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/built@0.7.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/built</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/lukaslueg/built</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bumpalo@3.19.0">
      <author>Nick Fitzgerald &lt;fitzgen@gmail.com&gt;</author>
      <name>bumpalo</name>
      <version>3.19.0</version>
      <description>A fast bump allocation arena for Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">46c5e41b57b8bba42a04676d81cb89e9ee8e859a1a66f80a5a72e1cb76b34d43</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/bumpalo@3.19.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bumpalo</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/fitzgen/bumpalo</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#byte-unit@5.1.6">
      <author>Magic Len &lt;len@magiclen.org&gt;</author>
      <name>byte-unit</name>
      <version>5.1.6</version>
      <description>A library for interacting with units of bytes.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e1cd29c3c585209b0cbc7309bfe3ed7efd8c84c21b7af29c8bfae908f8777174</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/byte-unit@5.1.6</purl>
      <externalReferences>
        <reference type="website">
          <url>https://magiclen.org/byte-unit</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/magiclen/byte-unit</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bytecheck@0.6.12">
      <author>David Koloski &lt;djkoloski@gmail.com&gt;</author>
      <name>bytecheck</name>
      <version>0.6.12</version>
      <description>Derive macro for bytecheck</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">23cdc57ce23ac53c931e88a43d06d070a6fd142f2617be5855eb75efc9beb1c2</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/bytecheck@0.6.12</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bytecheck</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/djkoloski/bytecheck</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bytecheck_derive@0.6.12">
      <author>David Koloski &lt;djkoloski@gmail.com&gt;</author>
      <name>bytecheck_derive</name>
      <version>0.6.12</version>
      <description>Derive macro for bytecheck</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3db406d29fbcd95542e92559bed4d8ad92636d1ca8b3b72ede10b4bcc010e659</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/bytecheck_derive@0.6.12</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bytecheck_derive</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/djkoloski/bytecheck</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bytecount@0.6.9">
      <author>Andre Bogus &lt;bogusandre@gmail.de&gt;, Joshua Landau &lt;joshua@landau.ws&gt;</author>
      <name>bytecount</name>
      <version>0.6.9</version>
      <description>count occurrences of a given byte, or the number of UTF-8 code points, in a byte slice, fast</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">175812e0be2bccb6abe50bb8d566126198344f707e304f45c648fd8f2cc0365e</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/bytecount@0.6.9</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/llogiq/bytecount</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bytemuck@1.24.0">
      <author>Lokathor &lt;zefria@gmail.com&gt;</author>
      <name>bytemuck</name>
      <version>1.24.0</version>
      <description>A crate for mucking around with piles of bytes.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1fbdf580320f38b612e485521afda1ee26d10cc9884efaaa750d383e13e3c5f4</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/bytemuck@1.24.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Lokathor/bytemuck</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#byteorder-lite@0.1.0">
      <name>byteorder-lite</name>
      <version>0.1.0</version>
      <description>Library for reading/writing numbers in big-endian and little-endian.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">8f1fe948ff07f4bd06c30984e69f5b4899c516a3ef74f34df92a2df2ab535495</hash>
      </hashes>
      <licenses>
        <expression>Unlicense OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/byteorder-lite@0.1.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/byteorder-lite</url>
        </reference>
        <reference type="website">
          <url>https://github.com/image-rs/byteorder-lite</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/image-rs/byteorder-lite</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#byteorder@1.5.0">
      <author>Andrew Gallant &lt;jamslam@gmail.com&gt;</author>
      <name>byteorder</name>
      <version>1.5.0</version>
      <description>Library for reading/writing numbers in big-endian and little-endian.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1fd0f2584146f6f2ef48085050886acf353beff7305ebd1ae69500e27c67f64b</hash>
      </hashes>
      <licenses>
        <expression>Unlicense OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/byteorder@1.5.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/byteorder</url>
        </reference>
        <reference type="website">
          <url>https://github.com/BurntSushi/byteorder</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/BurntSushi/byteorder</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bytes@1.10.1">
      <author>Carl Lerche &lt;me@carllerche.com&gt;, Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>bytes</name>
      <version>1.10.1</version>
      <description>Types and traits for working with bytes</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d71b6127be86fdcfddb610f7182ac57211d4b18a3e9c82eb2d17662f2227ad6a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/bytes@1.10.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/tokio-rs/bytes</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bytesize@1.3.3">
      <author>Hyunsik Choi &lt;hyunsik.choi@gmail.com&gt;</author>
      <name>bytesize</name>
      <version>1.3.3</version>
      <description>an utility for human-readable bytes representations</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2e93abca9e28e0a1b9877922aacb20576e05d4679ffa78c3d6dc22a26a216659</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/bytesize@1.3.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bytesize/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/bytesize-rs/bytesize/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/bytesize-rs/bytesize/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bzip2-sys@0.1.13+1.0.8">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>bzip2-sys</name>
      <version>0.1.13+1.0.8</version>
      <description>Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">225bff33b2141874fe80d71e07d6eec4f85c5c216453dd96388240f96e1acc14</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/bzip2-sys@0.1.13+1.0.8</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bzip2-sys</url>
        </reference>
        <reference type="website">
          <url>https://github.com/alexcrichton/bzip2-rs</url>
        </reference>
        <reference type="other">
          <url>bzip2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/alexcrichton/bzip2-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#bzip2@0.4.4">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>bzip2</name>
      <version>0.4.4</version>
      <description>Bindings to libbzip2 for bzip2 compression and decompression exposed as Reader/Writer streams. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bdb116a6ef3f6c3698828873ad02c3014b3c85cadb88496095628e3ef1e347f8</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/bzip2@0.4.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/bzip2</url>
        </reference>
        <reference type="website">
          <url>https://github.com/alexcrichton/bzip2-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/alexcrichton/bzip2-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#camino@1.2.1">
      <author>Without Boats &lt;saoirse@without.boats&gt;, Ashley Williams &lt;ashley666ashley@gmail.com&gt;, Steve Klabnik &lt;steve@steveklabnik.com&gt;, Rain &lt;rain@sunshowers.io&gt;</author>
      <name>camino</name>
      <version>1.2.1</version>
      <description>UTF-8 paths</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">276a59bf2b2c967788139340c9f0c5b12d7fd6630315c15c217e559de85d2609</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/camino@1.2.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/camino</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/camino-rs/camino</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cargo-mobile2@0.20.7">
      <author>Tauri Programme within The Commons Conservancy, Brainium Studios LLC, Francesca Lovebloom &lt;francesca@brainiumstudios.com&gt;</author>
      <name>cargo-mobile2</name>
      <version>0.20.7</version>
      <description>Rust on mobile made easy!</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3ca76a1e55f3b1e020d8f069e46926334ba7d9cad71a59098602c59b69cbc29d</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/cargo-mobile2@0.20.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cargo-mobile2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/tauri-apps/cargo-mobile2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cargo-platform@0.1.9">
      <name>cargo-platform</name>
      <version>0.1.9</version>
      <description>Cargo's representation of a target platform.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e35af189006b9c0f00a064685c727031e3ed2d8020f7ba284d78cc2671bd36ea</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cargo-platform@0.1.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cargo-platform</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-lang/cargo</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/cargo</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cargo_metadata@0.19.2">
      <author>Oliver Schneider &lt;git-spam-no-reply9815368754983@oli-obk.de&gt;</author>
      <name>cargo_metadata</name>
      <version>0.19.2</version>
      <description>structured access to the output of `cargo metadata`</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">dd5eb614ed4c27c5d706420e4320fbe3216ab31fa1c33cd8246ac36dae4479ba</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/cargo_metadata@0.19.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/oli-obk/cargo_metadata</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cargo_toml@0.22.3">
      <author>Kornel &lt;kornel@geekhood.net&gt;</author>
      <name>cargo_toml</name>
      <version>0.22.3</version>
      <description>`Cargo.toml` struct definitions for parsing with Serde</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">374b7c592d9c00c1f4972ea58390ac6b18cbb6ab79011f3bdc90a0b82ca06b77</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/cargo_toml@0.22.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cargo_toml</url>
        </reference>
        <reference type="website">
          <url>https://lib.rs/cargo_toml</url>
        </reference>
        <reference type="vcs">
          <url>https://gitlab.com/lib.rs/cargo_toml</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#castaway@0.2.4">
      <author>Stephen M. Coakley &lt;me@stephencoakley.com&gt;</author>
      <name>castaway</name>
      <version>0.2.4</version>
      <description>Safe, zero-cost downcasting for limited compile-time specialization.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">dec551ab6e7578819132c713a93c022a05d60159dc86e7a7050223577484c55a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/castaway@0.2.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sagebind/castaway</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cbc@0.1.2">
      <author>RustCrypto Developers</author>
      <name>cbc</name>
      <version>0.1.2</version>
      <description>Cipher Block Chaining (CBC) block cipher mode of operation</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">26b52a9543ae338f279b96b0b9fed9c8093744685043739079ce85cd58f289a6</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cbc@0.1.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cbc</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/block-modes</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cc@1.2.40">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>cc</name>
      <version>1.2.40</version>
      <description>A build-time dependency for Cargo build scripts to assist in invoking the native C compiler to compile native C code into a static archive to be linked into Rust code. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e1d05d92f4b1fd76aad469d46cdd858ca761576082cd37df81416691e50199fb</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cc@1.2.40</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cc</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-lang/cc-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/cc-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cfb@0.7.3">
      <author>Matthew D. Steele &lt;mdsteele@alum.mit.edu&gt;</author>
      <name>cfb</name>
      <version>0.7.3</version>
      <description>Read/write Compound File Binary (structured storage) files</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d38f2da7a0a2c4ccf0065be06397cc26a81f4e528be095826eee9d4adbb8c60f</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/cfb@0.7.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://mdsteele.github.io/rust-cfb/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/mdsteele/rust-cfb</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cfg-if@1.0.3">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>cfg-if</name>
      <version>1.0.3</version>
      <description>A macro to ergonomically define an item depending on a large number of #[cfg] parameters. Structured like an if-else chain, the first matching branch is the item that gets emitted. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2fd1289c04a9ea8cb22300a459a72a385d7c73d3259e2ed7dcb2af674838cfa9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cfg-if@1.0.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-lang/cfg-if</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cfg_aliases@0.2.1">
      <author>Zicklag &lt;zicklag@katharostech.com&gt;</author>
      <name>cfg_aliases</name>
      <version>0.2.1</version>
      <description>A tiny utility to help save you a lot of effort with long winded `#[cfg()]` checks.</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">613afe47fcd5fac7ccf1db93babcb082c5994d996f20b8b159f2ad1658eb5724</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/cfg_aliases@0.2.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cfg_aliases</url>
        </reference>
        <reference type="website">
          <url>https://github.com/katharostech/cfg_aliases</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/katharostech/cfg_aliases</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#chrono@0.4.42">
      <name>chrono</name>
      <version>0.4.42</version>
      <description>Date and time library for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">145052bdd345b87320e369255277e3fb5152762ad123a901ef5c262dd38fe8d2</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/chrono@0.4.42</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/chrono/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/chronotope/chrono</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/chronotope/chrono</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cipher@0.4.4">
      <author>RustCrypto Developers</author>
      <name>cipher</name>
      <version>0.4.4</version>
      <description>Traits for describing block ciphers and stream ciphers</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">773f3b9af64447d2ce9850330c473515014aa235e6a783b02db81ff39e4a3dad</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cipher@0.4.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cipher</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/traits</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#clap@4.5.48">
      <name>clap</name>
      <version>4.5.48</version>
      <description>A simple to use, efficient, and full-featured Command Line Argument Parser</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e2134bb3ea021b78629caa971416385309e0131b351b25e01dc16fb54e1b5fae</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/clap@4.5.48</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/clap-rs/clap</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#clap_builder@4.5.48">
      <name>clap_builder</name>
      <version>4.5.48</version>
      <description>A simple to use, efficient, and full-featured Command Line Argument Parser</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c2ba64afa3c0a6df7fa517765e31314e983f51dda798ffba27b988194fb65dc9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/clap_builder@4.5.48</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/clap-rs/clap</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#clap_complete@4.5.58">
      <name>clap_complete</name>
      <version>4.5.58</version>
      <description>Generate shell completion scripts for your clap::Command</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">75bf0b32ad2e152de789bb635ea4d3078f6b838ad7974143e99b99f45a04af4a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/clap_complete@4.5.58</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/clap-rs/clap</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#clap_derive@4.5.47">
      <name>clap_derive</name>
      <version>4.5.47</version>
      <description>Parse command line argument by defining a struct, derive crate.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bbfd7eae0b0f1a6e63d4b13c9c478de77c2eb546fba158ad50b4203dc24b9f9c</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/clap_derive@4.5.47</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/clap-rs/clap</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#clap_lex@0.7.5">
      <name>clap_lex</name>
      <version>0.7.5</version>
      <description>Minimal, flexible command line parser</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b94f61472cee1439c0b966b47e3aca9ae07e45d070759512cd390ea2bebc6675</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/clap_lex@0.7.5</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/clap-rs/clap</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#color_quant@1.1.0">
      <author>nwin &lt;nwin@users.noreply.github.com&gt;</author>
      <name>color_quant</name>
      <version>1.1.0</version>
      <description>Color quantization library to reduce n colors to 256 colors.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3d7b894f5411737b7867f4827955924d7c254fc9f4d91a6aad6b097804b1018b</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/color_quant@1.1.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/image-rs/color_quant.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#colorchoice@1.0.4">
      <name>colorchoice</name>
      <version>1.0.4</version>
      <description>Global override of color control</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b05b61dc5112cbb17e4b6cd61790d9845d13888356391624cbe7e41efeac1e75</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/colorchoice@1.0.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-cli/anstyle.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#colored@2.2.0">
      <author>Thomas Wickham &lt;mackwic@gmail.com&gt;</author>
      <name>colored</name>
      <version>2.2.0</version>
      <description>The most simple way to add colors in your terminal</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">117725a109d387c937a1533ce01b450cbde6b88abceea8473c4d7a85853cda3c</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/colored@2.2.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/mackwic/colored</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/mackwic/colored</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#common-path@1.0.0">
      <author>Paul Woolcock &lt;paul@woolcock.us&gt;</author>
      <name>common-path</name>
      <version>1.0.0</version>
      <description>Finds the common prefix between a set of paths </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2382f75942f4b3be3690fe4f86365e9c853c1587d6ee58212cebf6e2a9ccd101</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/common-path@1.0.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/common-path</url>
        </reference>
        <reference type="website">
          <url>https://gitlab.com/pwoolcoc/common-path</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#compact_str@0.8.1">
      <author>Parker Timmerman &lt;parker@parkertimmerman.com&gt;</author>
      <name>compact_str</name>
      <version>0.8.1</version>
      <description>A memory efficient string type that transparently stores strings on the stack, when possible</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3b79c4069c6cad78e2e0cdfcbd26275770669fb39fd308a752dc110e83b9af32</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/compact_str@0.8.1</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/ParkMyCar/compact_str</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/ParkMyCar/compact_str</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#console@0.15.11">
      <author>Armin Ronacher &lt;armin.ronacher@active-4.com&gt;</author>
      <name>console</name>
      <version>0.15.11</version>
      <description>A terminal and console abstraction for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">054ccb5b10f9f2cbf51eb355ca1d05c2d279ce1804688d0db74b4733a5aeafd8</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/console@0.15.11</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/console</url>
        </reference>
        <reference type="website">
          <url>https://github.com/console-rs/console</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/console-rs/console</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#const-oid@0.9.6">
      <author>RustCrypto Developers</author>
      <name>const-oid</name>
      <version>0.9.6</version>
      <description>Const-friendly implementation of the ISO/IEC Object Identifier (OID) standard as defined in ITU X.660, with support for BER/DER encoding/decoding as well as heapless no_std (i.e. embedded) support </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c2459377285ad874054d797f3ccebf984978aa39129f6eafde5cdc8315b612f8</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/const-oid@0.9.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/const-oid</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/formats/tree/master/const-oid</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#const_panic@0.2.15">
      <author>rodrimati1992 &lt;rodrimatt1985@gmail.com&gt;</author>
      <name>const_panic</name>
      <version>0.2.15</version>
      <description>const panic with formatting</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e262cdaac42494e3ae34c43969f9cdeb7da178bdb4b66fa6a1ea2edb4c8ae652</hash>
      </hashes>
      <licenses>
        <expression>Zlib</expression>
      </licenses>
      <purl>pkg:cargo/const_panic@0.2.15</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rodrimati1992/const_panic/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#convert_case@0.4.0">
      <author>David Purdum &lt;purdum41@gmail.com&gt;</author>
      <name>convert_case</name>
      <version>0.4.0</version>
      <description>Convert strings into any case</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6245d59a3e82a7fc217c5828a6692dbc6dfb63a0c8c90495621f7b9d79704a0e</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/convert_case@0.4.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rutrum/convert-case</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cookie-factory@0.3.3">
      <author>Geoffroy Couprie &lt;geo.couprie@gmail.com&gt;, Pierre Chifflier &lt;chifflier@wzdftpd.net&gt;</author>
      <name>cookie-factory</name>
      <version>0.3.3</version>
      <description>nom inspired serialization library</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9885fa71e26b8ab7855e2ec7cae6e9b380edff76cd052e07c683a0319d51b3a2</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/cookie-factory@0.3.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://docs.rs/cookie-factory</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-bakery/cookie-factory</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cookie@0.18.1">
      <author>Sergio Benitez &lt;sb@sergio.bz&gt;, Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>cookie</name>
      <version>0.18.1</version>
      <description>HTTP cookie parsing and cookie jar management. Supports signed and private (encrypted, authenticated) jars. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4ddef33a339a91ea89fb53151bd0a4689cfce27055c291dfa69945475d22c747</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cookie@0.18.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cookie</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/SergioBenitez/cookie-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#core-foundation-sys@0.8.7">
      <author>The Servo Project Developers</author>
      <name>core-foundation-sys</name>
      <version>0.8.7</version>
      <description>Bindings to Core Foundation for macOS</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">773648b94d0e5d620f64f280777445740e61fe701025087ec8b57f45c791888b</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/core-foundation-sys@0.8.7</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#core-foundation@0.10.1">
      <author>The Servo Project Developers</author>
      <name>core-foundation</name>
      <version>0.10.1</version>
      <description>Bindings to Core Foundation for macOS</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b2a6cd9ae233e7f62ba4e9353e81a88df7fc8a5987b8d445b4d90c879bd156f6</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/core-foundation@0.10.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#core-foundation@0.9.4">
      <author>The Servo Project Developers</author>
      <name>core-foundation</name>
      <version>0.9.4</version>
      <description>Bindings to Core Foundation for macOS</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">91e195e091a93c46f7102ec7818a2aa394e1e1771c3ab4825963fa03e45afb8f</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/core-foundation@0.9.4</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#core-graphics-types@0.2.0">
      <author>The Servo Project Developers</author>
      <name>core-graphics-types</name>
      <version>0.2.0</version>
      <description>Bindings for some fundamental Core Graphics types</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3d44a101f213f6c4cdc1853d4b78aef6db6bdfa3468798cc1d9912f4735013eb</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/core-graphics-types@0.2.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#core-graphics@0.24.0">
      <author>The Servo Project Developers</author>
      <name>core-graphics</name>
      <version>0.24.0</version>
      <description>Bindings to Core Graphics for macOS</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">fa95a34622365fa5bbf40b20b75dba8dfa8c94c734aea8ac9a5ca38af14316f1</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/core-graphics@0.24.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/core-foundation-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#core_maths@0.1.1">
      <author>Robert Bastian &lt;me@robertbastian.dev</author>
      <name>core_maths</name>
      <version>0.1.1</version>
      <description>Extension trait for full float functionality in `#[no_std]` backed by `libm`.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">77745e017f5edba1a9c1d854f6f3a52dac8a12dd5af5d2f54aecf61e43d80d30</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/core_maths@0.1.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/robertbastian/core_maths</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cow-utils@0.1.3">
      <author>Ingvar Stepanyan &lt;me@rreverser.com&gt;</author>
      <name>cow-utils</name>
      <version>0.1.3</version>
      <description>Copy-on-write string utilities for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">417bef24afe1460300965a25ff4a24b8b45ad011948302ec221e8a0a81eb2c79</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/cow-utils@0.1.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/RReverser/cow-utils-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cpio-archive@0.9.0">
      <author>Gregory Szorc &lt;gregory.szorc@gmail.com&gt;</author>
      <name>cpio-archive</name>
      <version>0.9.0</version>
      <description>cpio archive reading and writing</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">63d5133d716d3d82da8c76367ddb0ab1733e2629f1462e4f39947e13b8b4b741</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cpio-archive@0.9.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/indygreg/apple-platform-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/indygreg/apple-platform-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cpufeatures@0.2.17">
      <author>RustCrypto Developers</author>
      <name>cpufeatures</name>
      <version>0.2.17</version>
      <description>Lightweight runtime CPU feature detection for aarch64, loongarch64, and x86/x86_64 targets,  with no_std support and support for mobile targets including Android and iOS </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">59ed5838eebb26a2bb2e58f6d5b5316989ae9d08bab10e0e6d103e656d1b0280</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cpufeatures@0.2.17</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cpufeatures</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/utils</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#crc32fast@1.5.0">
      <author>Sam Rijs &lt;srijs@airpost.net&gt;, Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>crc32fast</name>
      <version>1.5.0</version>
      <description>Fast, SIMD-accelerated CRC32 (IEEE) checksum computation</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9481c1c90cbf2ac953f07c8d4a58aa3945c425b7185c9154d67a65e4230da511</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/crc32fast@1.5.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/srijs/rust-crc32fast</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#crossbeam-channel@0.5.15">
      <name>crossbeam-channel</name>
      <version>0.5.15</version>
      <description>Multi-producer multi-consumer channels for message passing</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">82b8f8f868b36967f9606790d1903570de9ceaf870a7bf9fbbd3016d636a2cb2</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/crossbeam-channel@0.5.15</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-channel</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/crossbeam-rs/crossbeam</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#crossbeam-deque@0.8.6">
      <name>crossbeam-deque</name>
      <version>0.8.6</version>
      <description>Concurrent work-stealing deque</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9dd111b7b7f7d55b72c0a6ae361660ee5853c9af73f70c3c2ef6858b950e2e51</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/crossbeam-deque@0.8.6</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-deque</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/crossbeam-rs/crossbeam</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#crossbeam-epoch@0.9.18">
      <name>crossbeam-epoch</name>
      <version>0.9.18</version>
      <description>Epoch-based garbage collection</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5b82ac4a3c2ca9c3460964f020e1402edd5753411d7737aa39c3714ad1b5420e</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/crossbeam-epoch@0.9.18</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-epoch</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/crossbeam-rs/crossbeam</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#crossbeam-utils@0.8.21">
      <name>crossbeam-utils</name>
      <version>0.8.21</version>
      <description>Utilities for concurrent programming</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d0a5c400df2834b80a4c3327b3aad3a4c4cd4de0629063962b03235697506a28</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/crossbeam-utils@0.8.21</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/crossbeam-rs/crossbeam/tree/master/crossbeam-utils</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/crossbeam-rs/crossbeam</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#crypto-bigint@0.5.5">
      <author>RustCrypto Developers</author>
      <name>crypto-bigint</name>
      <version>0.5.5</version>
      <description>Pure Rust implementation of a big integer library which has been designed from the ground-up for use in cryptographic applications. Provides constant-time, no_std-friendly implementations of modern formulas using const generics. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0dc92fb57ca44df6db8059111ab3af99a63d5d0f8375d9972e319a379c6bab76</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/crypto-bigint@0.5.5</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/crypto-bigint</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#crypto-common@0.1.6">
      <author>RustCrypto Developers</author>
      <name>crypto-common</name>
      <version>0.1.6</version>
      <description>Common cryptographic traits</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1bfb12502f3fc46cca1bb51ac28df9d618d813cdc3d2f25b9fe775a34af26bb3</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/crypto-common@0.1.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/crypto-common</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/traits</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cryptographic-message-syntax@0.26.0">
      <author>Gregory Szorc &lt;gregory.szorc@gmail.com&gt;</author>
      <name>cryptographic-message-syntax</name>
      <version>0.26.0</version>
      <description>A pure Rust implementation of Crypographic Message Syntax (RFC 5652)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">43c324ba1028cef7e3a71a00cbf585637bb0215dec2f6a2b566d094190a1309b</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cryptographic-message-syntax@0.26.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/indygreg/cryptography-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/indygreg/cryptography-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#css-color@0.2.8">
      <author>Kal Conley &lt;kcconley@gmail.com&gt;</author>
      <name>css-color</name>
      <version>0.2.8</version>
      <description>Rust library for CSS color strings</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">42aaeae719fd78ce501d77c6cdf01f7e96f26bcd5617a4903a1c2b97e388543a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/css-color@0.2.8</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/kalcutter/rust-css-color</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cssparser-macros@0.6.1">
      <author>Simon Sapin &lt;simon.sapin@exyr.org&gt;</author>
      <name>cssparser-macros</name>
      <version>0.6.1</version>
      <description>Procedural macros for cssparser</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">13b588ba4ac1a99f7f2964d24b3d896ddc6bf847ee3855dbd4366f058cfcd331</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cssparser-macros@0.6.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cssparser-macros/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/rust-cssparser</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#cssparser@0.29.6">
      <author>Simon Sapin &lt;simon.sapin@exyr.org&gt;</author>
      <name>cssparser</name>
      <version>0.29.6</version>
      <description>Rust implementation of CSS Syntax Level 3</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f93d03419cb5950ccfd3daf3ff1c7a36ace64609a1a8746d493df1ca0afde0fa</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/cssparser@0.29.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/cssparser/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/rust-cssparser</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ctor@0.2.9">
      <author>Matt Mastracci &lt;matthew@mastracci.com&gt;</author>
      <name>ctor</name>
      <version>0.2.9</version>
      <description>__attribute__((constructor)) for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">32a2785755761f3ddc1492979ce1e48d2c00d09311c39e4466429188f3dd6501</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/ctor@0.2.9</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/mmastrac/rust-ctor</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ctr@0.9.2">
      <author>RustCrypto Developers</author>
      <name>ctr</name>
      <version>0.9.2</version>
      <description>CTR block modes of operation</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0369ee1ad671834580515889b80f2ea915f23b8be8d0daa4bbaf2ac5c7590835</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/ctr@0.9.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/ctr</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/block-modes</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ctrlc@3.5.0">
      <author>Antti Keränen &lt;detegr@gmail.com&gt;</author>
      <name>ctrlc</name>
      <version>3.5.0</version>
      <description>Easy Ctrl-C handler for Rust projects</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">881c5d0a13b2f1498e2306e82cbada78390e152d4b1378fb28a84f4dcd0dc4f3</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/ctrlc@3.5.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://detegr.github.io/doc/ctrlc</url>
        </reference>
        <reference type="website">
          <url>https://github.com/Detegr/rust-ctrlc</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/Detegr/rust-ctrlc.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#curve25519-dalek-derive@0.1.1">
      <name>curve25519-dalek-derive</name>
      <version>0.1.1</version>
      <description>curve25519-dalek Derives</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f46882e17999c6cc590af592290432be3bce0428cb0d5f8b6715e4dc7b383eb3</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/curve25519-dalek-derive@0.1.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/curve25519-dalek-derive</url>
        </reference>
        <reference type="website">
          <url>https://github.com/dalek-cryptography/curve25519-dalek</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dalek-cryptography/curve25519-dalek</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#curve25519-dalek@4.1.3">
      <author>Isis Lovecruft &lt;isis@patternsinthevoid.net&gt;, Henry de Valence &lt;hdevalence@hdevalence.ca&gt;</author>
      <name>curve25519-dalek</name>
      <version>4.1.3</version>
      <description>A pure-Rust implementation of group operations on ristretto255 and Curve25519</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">97fb8b7c4503de7d6ae7b42ab72a5a59857b4c937ec27a3d4539dba95b5ab2be</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/curve25519-dalek@4.1.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/curve25519-dalek</url>
        </reference>
        <reference type="website">
          <url>https://github.com/dalek-cryptography/curve25519-dalek</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dalek-cryptography/curve25519-dalek/tree/main/curve25519-dalek</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#darling@0.20.11">
      <author>Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>darling</name>
      <version>0.20.11</version>
      <description>A proc-macro library for reading attributes into structs when implementing custom derives. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">fc7f46116c46ff9ab3eb1597a45688b6715c6e628b5c133e288e709a29bcb4ee</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/darling@0.20.11</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/darling/0.20.11</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/TedDriggs/darling</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#darling@0.21.3">
      <author>Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>darling</name>
      <version>0.21.3</version>
      <description>A proc-macro library for reading attributes into structs when implementing custom derives. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9cdf337090841a411e2a7f3deb9187445851f91b309c0c0a29e05f74a00a48c0</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/darling@0.21.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/darling/0.21.3</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/TedDriggs/darling</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#darling_core@0.20.11">
      <author>Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>darling_core</name>
      <version>0.20.11</version>
      <description>Helper crate for proc-macro library for reading attributes into structs when implementing custom derives. Use https://crates.io/crates/darling in your code. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0d00b9596d185e565c2207a0b01f8bd1a135483d02d9b7b0a54b11da8d53412e</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/darling_core@0.20.11</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/TedDriggs/darling</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#darling_core@0.21.3">
      <author>Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>darling_core</name>
      <version>0.21.3</version>
      <description>Helper crate for proc-macro library for reading attributes into structs when implementing custom derives. Use https://crates.io/crates/darling in your code. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1247195ecd7e3c85f83c8d2a366e4210d588e802133e1e355180a9870b517ea4</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/darling_core@0.21.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/TedDriggs/darling</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#darling_macro@0.20.11">
      <author>Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>darling_macro</name>
      <version>0.20.11</version>
      <description>Internal support for a proc-macro library for reading attributes into structs when implementing custom derives. Use https://crates.io/crates/darling in your code. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">fc34b93ccb385b40dc71c6fceac4b2ad23662c7eeb248cf10d529b7e055b6ead</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/darling_macro@0.20.11</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/TedDriggs/darling</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#darling_macro@0.21.3">
      <author>Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>darling_macro</name>
      <version>0.21.3</version>
      <description>Internal support for a proc-macro library for reading attributes into structs when implementing custom derives. Use https://crates.io/crates/darling in your code. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d38308df82d1080de0afee5d069fa14b0326a88c14f15c5ccda35b4a6c414c81</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/darling_macro@0.21.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/TedDriggs/darling</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dashmap@6.1.0">
      <author>Acrimon &lt;joel.wejdenstal@gmail.com&gt;</author>
      <name>dashmap</name>
      <version>6.1.0</version>
      <description>Blazing fast concurrent HashMap for Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5041cc499144891f3790297212f32a74fb938e5136a14943f338ef9e0ae276cf</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/dashmap@6.1.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/dashmap</url>
        </reference>
        <reference type="website">
          <url>https://github.com/xacrimon/dashmap</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/xacrimon/dashmap</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#data-encoding@2.9.0">
      <author>Julien Cretin &lt;git@ia0.eu&gt;</author>
      <name>data-encoding</name>
      <version>2.9.0</version>
      <description>Efficient and customizable data-encoding functions like base64, base32, and hex</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2a2330da5de22e8a3cb63252ce2abb30116bf5265e89c0e01bc17015ce30a476</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/data-encoding@2.9.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/data-encoding</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/ia0/data-encoding</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#data-url@0.3.2">
      <author>Simon Sapin &lt;simon.sapin@exyr.org&gt;</author>
      <name>data-url</name>
      <version>0.3.2</version>
      <description>Processing of data: URL according to WHATWG’s Fetch Standard</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">be1e0bca6c3637f992fc1cc7cbc52a78c1ef6db076dbf1059c4323d6a2048376</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/data-url@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/servo/rust-url</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#der@0.7.10">
      <author>RustCrypto Developers</author>
      <name>der</name>
      <version>0.7.10</version>
      <description>Pure Rust embedded-friendly implementation of the Distinguished Encoding Rules (DER) for Abstract Syntax Notation One (ASN.1) as described in ITU X.690 with full support for heapless no_std targets </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e7c1832837b905bbfb5101e07cc24c8deddf52f93225eee6ead5f4d63d53ddcb</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/der@0.7.10</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/formats/tree/master/der</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#deranged@0.5.4">
      <author>Jacob Pratt &lt;jacob@jhpratt.dev&gt;</author>
      <name>deranged</name>
      <version>0.5.4</version>
      <description>Ranged integers</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">a41953f86f8a05768a6cda24def994fd2f424b04ec5c719cf89989779f199071</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/deranged@0.5.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/jhpratt/deranged</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#derive_builder@0.20.2">
      <author>Colin Kiegel &lt;kiegel@gmx.de&gt;, Pascal Hertleif &lt;killercup@gmail.com&gt;, Jan-Erik Rediger &lt;janerik@fnordig.de&gt;, Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>derive_builder</name>
      <version>0.20.2</version>
      <description>Rust macro to automatically implement the builder pattern for arbitrary structs.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">507dfb09ea8b7fa618fcf76e953f4f5e192547945816d5358edffe39f6f94947</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/derive_builder@0.20.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/derive_builder/0.20.2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/colin-kiegel/rust-derive-builder</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#derive_builder_core@0.20.2">
      <author>Colin Kiegel &lt;kiegel@gmx.de&gt;, Pascal Hertleif &lt;killercup@gmail.com&gt;, Jan-Erik Rediger &lt;janerik@fnordig.de&gt;, Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>derive_builder_core</name>
      <version>0.20.2</version>
      <description>Internal helper library for the derive_builder crate.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2d5bcf7b024d6835cfb3d473887cd966994907effbe9227e8c8219824d06c4e8</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/derive_builder_core@0.20.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/derive_builder_core</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/colin-kiegel/rust-derive-builder</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#derive_builder_macro@0.20.2">
      <author>Colin Kiegel &lt;kiegel@gmx.de&gt;, Pascal Hertleif &lt;killercup@gmail.com&gt;, Jan-Erik Rediger &lt;janerik@fnordig.de&gt;, Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>derive_builder_macro</name>
      <version>0.20.2</version>
      <description>Rust macro to automatically implement the builder pattern for arbitrary structs.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ab63b0e2bf4d5928aff72e83a7dace85d7bba5fe12dcc3c5a572d78caffd3f3c</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/derive_builder_macro@0.20.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/derive_builder_macro/0.20.2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/colin-kiegel/rust-derive-builder</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#derive_more@0.99.20">
      <author>Jelte Fennema &lt;github-tech@jeltef.nl&gt;</author>
      <name>derive_more</name>
      <version>0.99.20</version>
      <description>Adds #[derive(x)] macros for more traits</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6edb4b64a43d977b8e99788fe3a04d483834fba1215a7e02caa415b626497f7f</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/derive_more@0.99.20</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://jeltef.github.io/derive_more/derive_more/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/JelteF/derive_more</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#des@0.8.1">
      <author>RustCrypto Developers</author>
      <name>des</name>
      <version>0.8.1</version>
      <description>DES and Triple DES (3DES, TDES) block ciphers implementation</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ffdd80ce8ce993de27e9f063a444a4d53ce8e8db4c1f00cc03af5ad5a9867a1e</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/des@0.8.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/des</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/block-ciphers</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#deunicode@1.6.2">
      <author>Kornel Lesinski &lt;kornel@geekhood.net&gt;, Amit Chowdhury &lt;amitc97@gmail.com&gt;</author>
      <name>deunicode</name>
      <version>1.6.2</version>
      <description>Convert Unicode strings to pure ASCII by intelligently transliterating them. Suppors Emoji and Chinese.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">abd57806937c9cc163efc8ea3910e00a62e2aeb0b8119f1793a978088f8f6b04</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/deunicode@1.6.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/deunicode</url>
        </reference>
        <reference type="website">
          <url>https://lib.rs/crates/deunicode</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/kornelski/deunicode/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dialoguer@0.11.0">
      <author>Armin Ronacher &lt;armin.ronacher@active-4.com&gt;, Pavan Kumar Sunkara &lt;pavan.sss1991@gmail.com&gt;</author>
      <name>dialoguer</name>
      <version>0.11.0</version>
      <description>A command line prompting library.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">658bce805d770f407bc62102fca7c2c64ceef2fbcb2b8bd19d2765ce093980de</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/dialoguer@0.11.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/dialoguer</url>
        </reference>
        <reference type="website">
          <url>https://github.com/console-rs/dialoguer</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/console-rs/dialoguer</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#difference@2.0.0">
      <author>Johann Hofmann &lt;mail@johann-hofmann.com&gt;</author>
      <name>difference</name>
      <version>2.0.0</version>
      <description>A Rust text diffing and assertion library.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">524cbf6897b527295dff137cec09ecf3a05f4fddffd7dfcd1585403449e74198</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/difference@2.0.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://johannhof.github.io/difference.rs/difference/index.html</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/johannhof/difference.rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#digest@0.10.7">
      <author>RustCrypto Developers</author>
      <name>digest</name>
      <version>0.10.7</version>
      <description>Traits for cryptographic hash functions and message authentication codes</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9ed9a281f7bc9b7576e61468ba615a66a5c8cfdff42420a70aa82701a3b1e292</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/digest@0.10.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/digest</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/traits</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dirs-sys@0.4.1">
      <author>Simon Ochsenreither &lt;simon@ochsenreither.de&gt;</author>
      <name>dirs-sys</name>
      <version>0.4.1</version>
      <description>System-level helper functions for the dirs and directories crates.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">520f05a5cbd335fae5a99ff7a6ab8627577660ee5cfd6a94a6a929b52ff0321c</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/dirs-sys@0.4.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/dirs-dev/dirs-sys-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dirs-sys@0.5.0">
      <author>Simon Ochsenreither &lt;simon@ochsenreither.de&gt;</author>
      <name>dirs-sys</name>
      <version>0.5.0</version>
      <description>System-level helper functions for the dirs and directories crates.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e01a3366d27ee9890022452ee61b2b63a67e6f13f58900b651ff5665f0bb1fab</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/dirs-sys@0.5.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/dirs-dev/dirs-sys-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dirs@5.0.1">
      <author>Simon Ochsenreither &lt;simon@ochsenreither.de&gt;</author>
      <name>dirs</name>
      <version>5.0.1</version>
      <description>A tiny low-level library that provides platform-specific standard locations of directories for config, cache and other data on Linux, Windows, macOS and Redox by leveraging the mechanisms defined by the XDG base/user directory specifications on Linux, the Known Folder API on Windows, and the Standard Directory guidelines on macOS.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">44c45a9d03d6676652bcb5e724c7e988de1acad23a711b5217ab9cbecbec2225</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/dirs@5.0.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/soc/dirs-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dirs@6.0.0">
      <author>Simon Ochsenreither &lt;simon@ochsenreither.de&gt;</author>
      <name>dirs</name>
      <version>6.0.0</version>
      <description>A tiny low-level library that provides platform-specific standard locations of directories for config, cache and other data on Linux, Windows, macOS and Redox by leveraging the mechanisms defined by the XDG base/user directory specifications on Linux, the Known Folder API on Windows, and the Standard Directory guidelines on macOS.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c3e8aa94d75141228480295a7d0e7feb620b1a5ad9f12bc40be62411e38cce4e</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/dirs@6.0.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/soc/dirs-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dispatch2@0.3.0">
      <author>Mads Marquart &lt;mads@marquart.dk&gt;, Mary &lt;mary@mary.zone&gt;</author>
      <name>dispatch2</name>
      <version>0.3.0</version>
      <description>Bindings and wrappers for Apple's Grand Central Dispatch (GCD)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">89a09f22a6c6069a18470eb92d2298acf25463f14256d24778e1230d789a2aec</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/dispatch2@0.3.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dispatch@0.2.0">
      <author>Steven Sheldon</author>
      <name>dispatch</name>
      <version>0.2.0</version>
      <description>Rust wrapper for Apple's Grand Central Dispatch.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bd0c93bb4b0c6d9b77f4435b0ae98c24d17f1c45b2ff844c6151a07256ca923b</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/dispatch@0.2.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://ssheldon.github.io/rust-objc/dispatch/</url>
        </reference>
        <reference type="vcs">
          <url>http://github.com/SSheldon/rust-dispatch</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#displaydoc@0.2.5">
      <author>Jane Lusby &lt;jlusby@yaah.dev&gt;</author>
      <name>displaydoc</name>
      <version>0.2.5</version>
      <description>A derive macro for implementing the display Trait via a doc comment and string interpolation </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">97369cbbc041bc366949bc74d34658d6cda5621039731c6310521892a3a20ae0</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/displaydoc@0.2.5</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/displaydoc</url>
        </reference>
        <reference type="website">
          <url>https://github.com/yaahc/displaydoc</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/yaahc/displaydoc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#doc-comment@0.3.3">
      <author>Guillaume Gomez &lt;guillaume1.gomez@gmail.com&gt;</author>
      <name>doc-comment</name>
      <version>0.3.3</version>
      <description>Macro to generate doc comments</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">fea41bba32d969b513997752735605054bc0dfa92b4c56bf1189f2e174be7a10</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/doc-comment@0.3.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://docs.rs/crate/doc-comment</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/GuillaumeGomez/doc-comment</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#downcast@0.11.0">
      <author>Felix Köpge &lt;fkoep@mailbox.org&gt;</author>
      <name>downcast</name>
      <version>0.11.0</version>
      <description>Trait for downcasting trait objects back to their original types.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1435fa1053d8b2fbbe9be7e97eca7f33d37b28409959813daefc1446a14247f1</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/downcast@0.11.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/downcast</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/fkoep/downcast-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dpi@0.1.2">
      <name>dpi</name>
      <version>0.1.2</version>
      <description>Types for handling UI scaling</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d8b14ccef22fc6f5a8f4d7d768562a182c04ce9a3b3157b91390b52ddfdf1a76</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 AND MIT</expression>
      </licenses>
      <purl>pkg:cargo/dpi@0.1.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-windowing/winit</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dtoa-short@0.3.5">
      <author>Xidorn Quan &lt;me@upsuper.org&gt;</author>
      <name>dtoa-short</name>
      <version>0.3.5</version>
      <description>Serialize float number and truncate to certain precision</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">cd1511a7b6a56299bd043a9c167a6d2bfb37bf84a6dfceaba651168adfb43c87</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/dtoa-short@0.3.5</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/upsuper/dtoa-short</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dtoa@1.0.10">
      <author>David Tolnay &lt;dtolnay@gmail.com&gt;</author>
      <name>dtoa</name>
      <version>1.0.10</version>
      <description>Fast floating point primitive to string conversion</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d6add3b8cff394282be81f3fc1a0605db594ed69890078ca6e2cab1c408bcf04</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/dtoa@1.0.10</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/dtoa</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dtolnay/dtoa</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#duct@1.1.0">
      <author>oconnor663@gmail.com</author>
      <name>duct</name>
      <version>1.1.0</version>
      <description>a library for running child processes</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d7478638a31d1f1f3d6c9f5e57c76b906a04ac4879d6fd0fb6245bc88f73fd0b</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/duct@1.1.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/duct</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oconnor663/duct.rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dunce@1.0.5">
      <author>Kornel &lt;kornel@geekhood.net&gt;</author>
      <name>dunce</name>
      <version>1.0.5</version>
      <description>Normalize Windows paths to the most compatible format, avoiding UNC where possible</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">92773504d58c093f6de2459af4af33faa518c13451eb8f2b5698ed3d36e7c813</hash>
      </hashes>
      <licenses>
        <expression>CC0-1.0 OR MIT-0 OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/dunce@1.0.5</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/dunce</url>
        </reference>
        <reference type="website">
          <url>https://lib.rs/crates/dunce</url>
        </reference>
        <reference type="vcs">
          <url>https://gitlab.com/kornelski/dunce</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#dyn-clone@1.0.20">
      <author>David Tolnay &lt;dtolnay@gmail.com&gt;</author>
      <name>dyn-clone</name>
      <version>1.0.20</version>
      <description>Clone trait that is dyn-compatible</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d0881ea181b1df73ff77ffaaf9c7544ecc11e82fba9b5f27b262a3c73a332555</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/dyn-clone@1.0.20</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/dyn-clone</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dtolnay/dyn-clone</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ecdsa@0.16.9">
      <author>RustCrypto Developers</author>
      <name>ecdsa</name>
      <version>0.16.9</version>
      <description>Pure Rust implementation of the Elliptic Curve Digital Signature Algorithm (ECDSA) as specified in FIPS 186-4 (Digital Signature Standard), providing RFC6979 deterministic signatures as well as support for added entropy </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ee27f32b5c5292967d2d4a9d7f1e0b0aed2c15daded5a60300e4abb9d8020bca</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/ecdsa@0.16.9</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/signatures/tree/master/ecdsa</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#either@1.15.0">
      <author>bluss</author>
      <name>either</name>
      <version>1.15.0</version>
      <description>The enum `Either` with variants `Left` and `Right` is a general purpose sum type with two cases. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">48c757948c5ede0e46177b7add2e67155f70e33c07fea8284df6576da70b3719</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/either@1.15.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/either/1/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rayon-rs/either</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#elf@0.7.4">
      <author>Christopher Cole &lt;chris.cole.09@gmail.com&gt;</author>
      <name>elf</name>
      <version>0.7.4</version>
      <description>A pure-rust library for parsing ELF files</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4445909572dbd556c457c849c4ca58623d84b27c8fff1e74b0b4227d8b90d17b</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/elf@0.7.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/elf/latest/elf/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/cole14/rust-elf/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#elliptic-curve@0.13.8">
      <author>RustCrypto Developers</author>
      <name>elliptic-curve</name>
      <version>0.13.8</version>
      <description>General purpose Elliptic Curve Cryptography (ECC) support, including types and traits for representing various elliptic curve forms, scalars, points, and public/secret keys composed thereof. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b5e6043086bf7973472e0c7dff2142ea0b680d30e18d9cc40f267efbf222bd47</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/elliptic-curve@0.13.8</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/traits/tree/master/elliptic-curve</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#email_address@0.2.9">
      <author>Simon Johnston &lt;johnstonskj@gmail.com&gt;</author>
      <name>email_address</name>
      <version>0.2.9</version>
      <description>A Rust crate providing an implementation of an RFC-compliant `EmailAddress` newtype. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e079f19b08ca6239f47f8ba8509c11cf3ea30095831f7fed61441475edd8c449</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/email_address@0.2.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/email_address/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/johnstonskj/rust-email_address.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#embed-resource@3.0.6">
      <author>наб &lt;nabijaczleweli@nabijaczleweli.xyz&gt;, Cat Plus Plus &lt;piotrlegnica@piotrl.pl&gt;, Liigo &lt;liigo@qq.com&gt;, azyobuzin &lt;azyobuzin@users.sourceforge.jp&gt;, Peter Atashian &lt;retep998@gmail.com&gt;, pravic &lt;ehysta@gmail.com&gt;, Gabriel Majeri &lt;gabriel.majeri6@gmail.com&gt;, SonnyX, Johan Andersson &lt;repi@repi.se&gt;, Jordan Poles &lt;jpdev.noreply@gmail.com&gt;, MSxDOS &lt;melcodos@gmail.com&gt;, Jim McGrath &lt;jimmc2@gmail.com&gt;, roblabla &lt;unfiltered@roblab.la&gt;, Jasper Bekkers &lt;jasper@traverseresearch.nl&gt;, Richard Markiewicz &lt;rmarkiewicz@devolutions.net&gt;, Emerson de Freitas Barcelos &lt;emersonfxbx@gmail.com&gt;, Li Keqing &lt;me@kaze.ai&gt;, Alexis Bourget &lt;alexis.bourget@gmail.com&gt;, Michael Farrell &lt;micolous+git@gmail.com&gt;, Jacob Okamoto &lt;oko@oko.io&gt;, Marijn Suijten &lt;marijn@traverseresearch.nl&gt;, Lucas Nogueira &lt;lucas@tauri.app&gt;, CharlesChen0823 &lt;yongchen0823@gmail.com&gt;, Daniel Schaefer &lt;dhs@frame.work&gt;, Rene Leonhardt, ssrlive</author>
      <name>embed-resource</name>
      <version>3.0.6</version>
      <description>A Cargo library to handle compilation and inclusion of Windows resources in the most resilient fashion imaginable</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">55a075fc573c64510038d7ee9abc7990635863992f83ebc52c8b433b8411a02e</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/embed-resource@3.0.6</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/nabijaczleweli/rust-embed-resource</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#embed_plist@1.2.2">
      <author>Nikolai Vazquez &lt;hello@nikolaivazquez.com&gt;</author>
      <name>embed_plist</name>
      <version>1.2.2</version>
      <description>Embed property list files like Info.plist directly in your executable binary.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4ef6b89e5b37196644d8796de5268852ff179b44e96276cf4290264843743bb7</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/embed_plist@1.2.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/embed_plist</url>
        </reference>
        <reference type="website">
          <url>https://github.com/nvzqz/embed-plist-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/nvzqz/embed-plist-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#encoding_rs@0.8.35">
      <author>Henri Sivonen &lt;hsivonen@hsivonen.fi&gt;</author>
      <name>encoding_rs</name>
      <version>0.8.35</version>
      <description>A Gecko-oriented implementation of the Encoding Standard</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">75030f3c4f45dafd7586dd6780965a8c7e8e285a5ecb86713e63a79c5b2766f3</hash>
      </hashes>
      <licenses>
        <expression>(Apache-2.0 OR MIT) AND BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/encoding_rs@0.8.35</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/encoding_rs/</url>
        </reference>
        <reference type="website">
          <url>https://docs.rs/encoding_rs/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hsivonen/encoding_rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#english-numbers@0.3.3">
      <author>Matthew Maclean</author>
      <name>english-numbers</name>
      <version>0.3.3</version>
      <description>Convert integers to written English number format</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4e4f5d6e192964d498b45abee72ca445e91909094bc8e8791259e82c2a0d1aa6</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
        <license>
          <name>Unknown</name>
          <text encoding="base64">TUlUIExpY2Vuc2UNCg0KQ29weXJpZ2h0IChjKSAyMDE3IE1hdHRoZXcgTWFjbGVhbg0KDQpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5DQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbA0KaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cw0KdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbA0KY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzDQpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOg0KDQpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwNCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuDQoNClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SDQpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwNCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQ0KQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUg0KTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwNCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFDQpTT0ZUV0FSRS4NCg==</text>
        </license>
      </licenses>
      <purl>pkg:cargo/english-numbers@0.3.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/english-numbers</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/Matthew-Maclean/english-numbers</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#env_filter@0.1.3">
      <name>env_filter</name>
      <version>0.1.3</version>
      <description>Filter log events using environment variables </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">186e05a59d4c50738528153b83b0b0194d3a29507dfec16eccd4b342903397d0</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/env_filter@0.1.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-cli/env_logger</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#env_home@0.1.0">
      <author>Peter Tripp &lt;peter.tripp@gmail.com&gt;</author>
      <name>env_home</name>
      <version>0.1.0</version>
      <description>Get the user home directory in a cross-platform way.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c7f84e12ccf0a7ddc17a6c41c93326024c42920d7ee630d04950e6926645c0fe</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/env_home@0.1.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/notpeter/env-home</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/notpeter/env-home</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#env_logger@0.10.2">
      <name>env_logger</name>
      <version>0.10.2</version>
      <description>A logging implementation for `log` which is configured via an environment variable. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4cd405aab171cb85d6735e5c8d9db038c17d3ca007a4d2c25f337935c3d90580</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/env_logger@0.10.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-cli/env_logger</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#env_logger@0.11.8">
      <name>env_logger</name>
      <version>0.11.8</version>
      <description>A logging implementation for `log` which is configured via an environment variable. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">13c863f0904021b108aa8b2f55046443e6b1ebde8fd4a15c399893aae4fa069f</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/env_logger@0.11.8</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-cli/env_logger</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#equator-macro@0.4.2">
      <author>sarah &lt;&gt;</author>
      <name>equator-macro</name>
      <version>0.4.2</version>
      <description>Composable assertion library</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">44f23cf4b44bfce11a86ace86f8a73ffdec849c9fd00a386a53d278bd9e81fb3</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/equator-macro@0.4.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sarah-ek/equator/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#equator@0.4.2">
      <author>sarah &lt;&gt;</author>
      <name>equator</name>
      <version>0.4.2</version>
      <description>Composable assertion library</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4711b213838dfee0117e3be6ac926007d7f433d7bbe33595975d4190cb07e6fc</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/equator@0.4.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sarah-ek/equator/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#equivalent@1.0.2">
      <name>equivalent</name>
      <version>1.0.2</version>
      <description>Traits for key comparison in maps.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">877a4ace8713b0bcf2a4e7eec82529c029f1d0619886d18145fea96c3ffe5c0f</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/equivalent@1.0.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/indexmap-rs/equivalent</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#erased-serde@0.4.8">
      <author>David Tolnay &lt;dtolnay@gmail.com&gt;</author>
      <name>erased-serde</name>
      <version>0.4.8</version>
      <description>Type-erased Serialize and Serializer traits</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">259d404d09818dec19332e31d94558aeb442fea04c817006456c24b5460bbd4b</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/erased-serde@0.4.8</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/erased-serde</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dtolnay/erased-serde</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#errno@0.3.14">
      <author>Chris Wong &lt;lambda.fairy@gmail.com&gt;, Dan Gohman &lt;dev@sunfishcode.online&gt;</author>
      <name>errno</name>
      <version>0.3.14</version>
      <description>Cross-platform interface to the `errno` variable.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">39cab71617ae0d63f51a36d69f866391735b51691dbda63cf6f96d042b63efeb</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/errno@0.3.14</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/errno</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/lambda-fairy/rust-errno</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#euclid@0.22.11">
      <author>The Servo Project Developers</author>
      <name>euclid</name>
      <version>0.22.11</version>
      <description>Geometry primitives</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ad9cdb4b747e485a12abb0e6566612956c7a1bafa3bdb8d682c5b6d403589e48</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/euclid@0.22.11</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/euclid/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/euclid</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#exr@1.73.0">
      <author>johannesvollmer &lt;johannes596@t-online.de&gt;</author>
      <name>exr</name>
      <version>1.73.0</version>
      <description>Read and write OpenEXR files without any unsafe code</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f83197f59927b46c04a183a619b7c29df34e63e63c7869320862268c0ef687e0</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/exr@1.73.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/johannesvollmer/exrs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fancy-regex@0.16.2">
      <author>Raph Levien &lt;raph@google.com&gt;, Robin Stocker &lt;robin@nibor.org&gt;, Keith Hall &lt;keith.hall@available.systems&gt;</author>
      <name>fancy-regex</name>
      <version>0.16.2</version>
      <description>An implementation of regexes, supporting a relatively rich set of features, including backreferences and look-around.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">998b056554fbe42e03ae0e152895cd1a7e1002aec800fdc6635d20270260c46f</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/fancy-regex@0.16.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/fancy-regex</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/fancy-regex/fancy-regex</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fastrand@2.3.0">
      <author>Stjepan Glavina &lt;stjepang@gmail.com&gt;</author>
      <name>fastrand</name>
      <version>2.3.0</version>
      <description>A simple and fast random number generator</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">37909eebbb50d72f9059c3b6d82c0463f2ff062c9e95845c43a6c9c0355411be</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/fastrand@2.3.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/smol-rs/fastrand</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fax@0.2.6">
      <author>Sebastian K &lt;s3bk@protonmail.com&gt;</author>
      <name>fax</name>
      <version>0.2.6</version>
      <description>Decoder and Encoder for CCITT Group 3 and 4 bi-level image encodings used by fax machines TIFF and PDF.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f05de7d48f37cd6730705cbca900770cab77a89f413d23e100ad7fad7795a0ab</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/fax@0.2.6</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/pdf-rs/fax</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fax_derive@0.2.0">
      <author>Sebastian K &lt;s3bk@protonmail.com&gt;</author>
      <name>fax_derive</name>
      <version>0.2.0</version>
      <description>Bitstream matcher for the fax crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">a0aca10fb742cb43f9e7bb8467c91aa9bcb8e3ffbc6a6f7389bb93ffc920577d</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/fax_derive@0.2.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/pdf-rs/fax</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fdeflate@0.3.7">
      <author>The image-rs Developers</author>
      <name>fdeflate</name>
      <version>0.3.7</version>
      <description>Fast specialized deflate implementation</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1e6853b52649d4ac5c0bd02320cddc5ba956bdb407c4b75a2c6b75bf51500f8c</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/fdeflate@0.3.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/fdeflate</url>
        </reference>
        <reference type="website">
          <url>https://github.com/image-rs/fdeflate</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/image-rs/fdeflate</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fern@0.7.1">
      <author>David Ross &lt;daboross@daboross.net&gt;</author>
      <name>fern</name>
      <version>0.7.1</version>
      <description>Simple, efficient logging</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4316185f709b23713e41e3195f90edef7fb00c3ed4adc79769cf09cc762a3b29</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/fern@0.7.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/fern/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/daboross/fern</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ff@0.13.1">
      <author>Sean Bowe &lt;ewillbefull@gmail.com&gt;, Jack Grigg &lt;thestr4d@gmail.com&gt;</author>
      <name>ff</name>
      <version>0.13.1</version>
      <description>Library for building and interfacing with finite fields</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c0b50bfb653653f9ca9095b427bed08ab8d75a137839d9ad64eb11810d5b6393</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/ff@0.13.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/ff/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/zkcrypto/ff</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/zkcrypto/ff</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#figment@0.10.19">
      <author>Sergio Benitez &lt;sb@sergio.bz&gt;</author>
      <name>figment</name>
      <version>0.10.19</version>
      <description>A configuration library so con-free, it's unreal.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">8cb01cd46b0cf372153850f4c6c272d9cbea2da513e07538405148f95bd789f3</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/figment@0.10.19</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/figment/0.10</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/SergioBenitez/Figment</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#file-id@0.2.3">
      <author>Daniel Faust &lt;hessijames@gmail.com&gt;</author>
      <name>file-id</name>
      <version>0.2.3</version>
      <description>Utility for reading inode numbers (Linux, MacOS) and file IDs (Windows)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e1fc6a637b6dc58414714eddd9170ff187ecb0933d4c7024d1abbd23a3cc26e9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/file-id@0.2.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/notify</url>
        </reference>
        <reference type="website">
          <url>https://github.com/notify-rs/notify</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/notify-rs/notify.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#filetime@0.2.26">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>filetime</name>
      <version>0.2.26</version>
      <description>Platform-agnostic accessors of timestamps in File metadata </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bc0505cd1b6fa6580283f6bdf70a73fcf4aba1184038c90902b92b3dd0df63ed</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/filetime@0.2.26</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/filetime</url>
        </reference>
        <reference type="website">
          <url>https://github.com/alexcrichton/filetime</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/alexcrichton/filetime</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#find-msvc-tools@0.1.3">
      <name>find-msvc-tools</name>
      <version>0.1.3</version>
      <description>Find windows-specific tools, read MSVC versions from the registry and from COM interfaces</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0399f9d26e5191ce32c498bebd31e7a3ceabc2745f0ac54af3f335126c3f24b3</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/find-msvc-tools@0.1.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/find-msvc-tools</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/cc-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#flate2@1.1.4">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;, Josh Triplett &lt;josh@joshtriplett.org&gt;</author>
      <name>flate2</name>
      <version>1.1.4</version>
      <description>DEFLATE compression and decompression exposed as Read/BufRead/Write streams. Supports miniz_oxide and multiple zlib implementations. Supports zlib, gzip, and raw deflate streams. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">dc5a4e564e38c699f2880d3fda590bedc2e69f3f84cd48b457bd892ce61d0aa9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/flate2@1.1.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/flate2</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-lang/flate2-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/flate2-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#float-cmp@0.9.0">
      <author>Mike Dilger &lt;mike@mikedilger.com&gt;</author>
      <name>float-cmp</name>
      <version>0.9.0</version>
      <description>Floating point approximate comparison traits</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">98de4bbd547a563b716d8dfa9aad1cb19bfab00f4fa09a6a4ed21dbcf44ce9c4</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/float-cmp@0.9.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/float-cmp</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/mikedilger/float-cmp</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fluent-uri@0.3.2">
      <author>Scallop Ye &lt;yescallop@gmail.com&gt;</author>
      <name>fluent-uri</name>
      <version>0.3.2</version>
      <description>A generic URI/IRI handling library compliant with RFC 3986/3987.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1918b65d96df47d3591bed19c5cca17e3fa5d0707318e4b5ef2eae01764df7e5</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/fluent-uri@0.3.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/fluent-uri</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/yescallop/fluent-uri-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fnv@1.0.7">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>fnv</name>
      <version>1.0.7</version>
      <description>Fowler–Noll–Vo hash function</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3f9eec918d3f24069decb9af1554cad7c880e2da24a9afd88aca000531ab82c1</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0  OR  MIT</expression>
      </licenses>
      <purl>pkg:cargo/fnv@1.0.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://doc.servo.org/fnv/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/rust-fnv</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fontdb@0.23.0">
      <author>Yevhenii Reizner &lt;razrfalcon@gmail.com&gt;</author>
      <name>fontdb</name>
      <version>0.23.0</version>
      <description>A simple, in-memory font database with CSS-like queries.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">457e789b3d1202543297a350643cf459f836cade38934e7a4cf6a39e7cde2905</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/fontdb@0.23.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/fontdb/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RazrFalcon/fontdb</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#foreign-types-macros@0.2.3">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>foreign-types-macros</name>
      <version>0.2.3</version>
      <description>An internal crate used by foreign-types</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1a5c6c585bc94aaf2c7b51dd4c2ba22680844aba4c687be581871a6f518c5742</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/foreign-types-macros@0.2.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/foreign-types</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#foreign-types-shared@0.1.1">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>foreign-types-shared</name>
      <version>0.1.1</version>
      <description>An internal crate used by foreign-types</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">00b0228411908ca8685dba7fc2cdd70ec9990a6e753e89b6ac91a84c40fbaf4b</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/foreign-types-shared@0.1.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/foreign-types</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#foreign-types-shared@0.3.1">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>foreign-types-shared</name>
      <version>0.3.1</version>
      <description>An internal crate used by foreign-types</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">aa9a19cbb55df58761df49b23516a86d432839add4af60fc256da840f66ed35b</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/foreign-types-shared@0.3.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/foreign-types</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#foreign-types@0.3.2">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>foreign-types</name>
      <version>0.3.2</version>
      <description>A framework for Rust wrappers over C APIs</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f6f339eb8adc052cd2ca78910fda869aefa38d22d5cb648e6485e4d3fc06f3b1</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/foreign-types@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/foreign-types</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#foreign-types@0.5.0">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>foreign-types</name>
      <version>0.5.0</version>
      <description>A framework for Rust wrappers over C APIs</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d737d9aa519fb7b749cbc3b962edcf310a8dd1f4b67c91c4f83975dbdd17d965</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/foreign-types@0.5.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/foreign-types</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#form_urlencoded@1.2.2">
      <author>The rust-url developers</author>
      <name>form_urlencoded</name>
      <version>1.2.2</version>
      <description>Parser and serializer for the application/x-www-form-urlencoded syntax, as used by HTML forms.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">cb4cb245038516f5f85277875cdaa4f7d2c9a0fa0468de06ed190163b1581fcf</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/form_urlencoded@1.2.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/servo/rust-url</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fraction@0.15.3">
      <author>dnsl48 &lt;dnsl48@gmail.com&gt;</author>
      <name>fraction</name>
      <version>0.15.3</version>
      <description>Lossless fractions and decimals; drop-in float replacement</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0f158e3ff0a1b334408dc9fb811cd99b446986f4d8b741bb08f9df1604085ae7</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/fraction@0.15.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/fraction/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/dnsl48/fraction.git</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dnsl48/fraction.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fragile@2.0.1">
      <author>Armin Ronacher &lt;armin.ronacher@active-4.com&gt;</author>
      <name>fragile</name>
      <version>2.0.1</version>
      <description>Provides wrapper types for sending non-send values to other threads.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">28dd6caf6059519a65843af8fe2a3ae298b14b80179855aeb4adc2c1934ee619</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/fragile@2.0.1</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/mitsuhiko/fragile</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/mitsuhiko/fragile</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fs2@0.4.3">
      <author>Dan Burkert &lt;dan@danburkert.com&gt;</author>
      <name>fs2</name>
      <version>0.4.3</version>
      <description>Cross-platform file locks and file duplication.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9564fc758e15025b46aa6643b1b77d047d1a56a1aea6e01002ac0c7026876213</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/fs2@0.4.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/fs2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/danburkert/fs2-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fsevent-sys@4.1.0">
      <author>Pierre Baillet &lt;pierre@baillet.name&gt;</author>
      <name>fsevent-sys</name>
      <version>4.1.0</version>
      <description>Rust bindings to the fsevent macOS API for file changes notifications</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">76ee7a02da4d231650c7cea31349b889be2f45ddb3ef3032d2ec8185f6313fd2</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/fsevent-sys@4.1.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/octplane/fsevent-rust/tree/master/fsevent-sys</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#funty@2.0.0">
      <author>myrrlyn &lt;self@myrrlyn.dev&gt;</author>
      <name>funty</name>
      <version>2.0.0</version>
      <description>Trait generalization over the primitive types</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e6d5a32815ae3f33302d95fdcb2ce17862f8c65363dcfd29360480ba1001fc9c</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/funty@2.0.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/funty</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/myrrlyn/funty</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futf@0.1.5">
      <author>Keegan McAllister &lt;kmcallister@mozilla.com&gt;</author>
      <name>futf</name>
      <version>0.1.5</version>
      <description>Handling fragments of UTF-8</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">df420e2e84819663797d1ec6544b13c5be84629e7bb00dc960d6917db2987843</hash>
      </hashes>
      <licenses>
        <expression>MIT  OR  Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futf@0.1.5</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/servo/futf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-channel@0.3.31">
      <name>futures-channel</name>
      <version>0.3.31</version>
      <description>Channels for asynchronous communication using futures-rs. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2dff15bf788c671c1934e366d07e30c1814a8ef514e1af724a602e8a2fbe1b10</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-channel@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-core@0.3.31">
      <name>futures-core</name>
      <version>0.3.31</version>
      <description>The core traits and types in for the `futures` library. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">05f29059c0c2090612e8d742178b0580d2dc940c837851ad723096f87af6663e</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-core@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-executor@0.3.31">
      <name>futures-executor</name>
      <version>0.3.31</version>
      <description>Executors for asynchronous tasks based on the futures-rs library. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1e28d1d997f585e54aebc3f97d39e72338912123a67330d723fdbb564d646c9f</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-executor@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-io@0.3.31">
      <name>futures-io</name>
      <version>0.3.31</version>
      <description>The `AsyncRead`, `AsyncWrite`, `AsyncSeek`, and `AsyncBufRead` traits for the futures-rs library. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9e5c1b78ca4aae1ac06c48a526a655760685149f0d465d21f37abfe57ce075c6</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-io@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-macro@0.3.31">
      <name>futures-macro</name>
      <version>0.3.31</version>
      <description>The futures-rs procedural macro implementations. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">162ee34ebcb7c64a8abebc059ce0fee27c2262618d7b60ed8faf72fef13c3650</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-macro@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-sink@0.3.31">
      <name>futures-sink</name>
      <version>0.3.31</version>
      <description>The asynchronous `Sink` trait for the futures-rs library. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e575fab7d1e0dcb8d0c7bcf9a63ee213816ab51902e6d244a95819acacf1d4f7</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-sink@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-task@0.3.31">
      <name>futures-task</name>
      <version>0.3.31</version>
      <description>Tools for working with tasks. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f90f7dce0722e95104fcb095585910c0977252f286e354b5e3bd38902cd99988</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-task@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-timer@3.0.3">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>futures-timer</name>
      <version>3.0.3</version>
      <description>Timeouts for futures. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f288b0a4f20f9a56b5d1da57e2227c661b7b16168e2f72365f57b63326e29b24</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-timer@3.0.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/futures-timer</url>
        </reference>
        <reference type="website">
          <url>https://github.com/async-rs/futures-timer</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/async-rs/futures-timer</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures-util@0.3.31">
      <name>futures-util</name>
      <version>0.3.31</version>
      <description>Common utilities and extension traits for the futures-rs library. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9fa08315bb612088cc391249efdc3bc77536f16c91f6cf495e6fbe85b20a4a81</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures-util@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#futures@0.3.31">
      <name>futures</name>
      <version>0.3.31</version>
      <description>An implementation of futures and streams featuring zero allocations, composability, and iterator-like interfaces. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">65bc07b1a8bc7c85c5f2e110c476c7389b4554ba72af57d8445ea63a576b0876</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/futures@0.3.31</purl>
      <externalReferences>
        <reference type="website">
          <url>https://rust-lang.github.io/futures-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/futures-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#fxhash@0.2.1">
      <author>cbreeden &lt;github@u.breeden.cc&gt;</author>
      <name>fxhash</name>
      <version>0.2.1</version>
      <description>A fast, non-secure, hashing algorithm derived from an internal hasher used in FireFox and Rustc.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c31b6d751ae2c7f11320402d34e41349dd1016f8d5d45e48c4312bc8625af50c</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/fxhash@0.2.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/fxhash</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/cbreeden/fxhash</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#generic-array@0.14.7">
      <author>Bartłomiej Kamiński &lt;fizyk20@gmail.com&gt;, Aaron Trent &lt;novacrazy@gmail.com&gt;</author>
      <name>generic-array</name>
      <version>0.14.7</version>
      <description>Generic types implementing functionality of arrays</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">85649ca51fd72272d7821adaf274ad91c288277713d9c18820d8499a7ff69e9a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/generic-array@0.14.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://fizyk20.github.io/generic-array/generic_array/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/fizyk20/generic-array.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#getrandom@0.1.16">
      <author>The Rand Project Developers</author>
      <name>getrandom</name>
      <version>0.1.16</version>
      <description>A small cross-platform library for retrieving random data from system source</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">8fc3cb4d91f53b50155bdcfd23f6a4c39ae1969c2ae85982b135750cccaf5fce</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/getrandom@0.1.16</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/getrandom</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-random/getrandom</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#getrandom@0.2.16">
      <author>The Rand Project Developers</author>
      <name>getrandom</name>
      <version>0.2.16</version>
      <description>A small cross-platform library for retrieving random data from system source</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">335ff9f135e4384c8150d6f27c6daed433577f86b4750418338c01a1a2528592</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/getrandom@0.2.16</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/getrandom</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-random/getrandom</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#getrandom@0.3.3">
      <author>The Rand Project Developers</author>
      <name>getrandom</name>
      <version>0.3.3</version>
      <description>A small cross-platform library for retrieving random data from system source</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">26145e563e54f2cadc477553f1ec5ee650b00862f0a58bcd12cbdc5f0ea2d2f4</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/getrandom@0.3.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/getrandom</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-random/getrandom</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ghash@0.5.1">
      <author>RustCrypto Developers</author>
      <name>ghash</name>
      <version>0.5.1</version>
      <description>Universal hash over GF(2^128) useful for constructing a Message Authentication Code (MAC), as in the AES-GCM authenticated encryption cipher. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f0d8a4362ccb29cb0b265253fb0a2728f592895ee6854fd9bc13f2ffda266ff1</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/ghash@0.5.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/ghash</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/universal-hashes</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#gif@0.13.3">
      <author>The image-rs Developers</author>
      <name>gif</name>
      <version>0.13.3</version>
      <description>GIF de- and encoder</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4ae047235e33e2829703574b54fdec96bfbad892062d97fed2f76022287de61b</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/gif@0.13.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/gif</url>
        </reference>
        <reference type="website">
          <url>https://github.com/image-rs/image-gif</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/image-rs/image-gif</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#gimli@0.32.3">
      <name>gimli</name>
      <version>0.32.3</version>
      <description>A library for reading and writing the DWARF debugging format.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e629b9b98ef3dd8afe6ca2bd0f89306cec16d43d907889945bc5d6687f2f13c7</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/gimli@0.32.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/gimli</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/gimli-rs/gimli</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#glob@0.3.3">
      <author>The Rust Project Developers</author>
      <name>glob</name>
      <version>0.3.3</version>
      <description>Support for matching file paths against Unix shell style patterns. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0cc23270f6e1808e30a928bdc84dea0b9b4136a8bc82338574f23baf47bbd280</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/glob@0.3.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/glob</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-lang/glob</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/glob</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#globset@0.4.16">
      <author>Andrew Gallant &lt;jamslam@gmail.com&gt;</author>
      <name>globset</name>
      <version>0.4.16</version>
      <description>Cross platform single glob and glob set matching. Glob set matching is the process of matching one or more glob patterns against a single candidate path simultaneously, and returning all of the globs that matched. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">54a1028dfc5f5df5da8a56a73e6c153c9a9708ec57232470703592a3f18e49f5</hash>
      </hashes>
      <licenses>
        <expression>Unlicense OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/globset@0.4.16</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/globset</url>
        </reference>
        <reference type="website">
          <url>https://github.com/BurntSushi/ripgrep/tree/master/crates/globset</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/BurntSushi/ripgrep/tree/master/crates/globset</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#goblin@0.8.2">
      <author>m4b &lt;m4b.github.io@gmail.com&gt;, seu &lt;seu@panopticon.re&gt;, Will Glynn &lt;will@willglynn.com&gt;, Philip Craig &lt;philipjcraig@gmail.com&gt;, Lzu Tao &lt;taolzu@gmail.com&gt;</author>
      <name>goblin</name>
      <version>0.8.2</version>
      <description>An impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1b363a30c165f666402fe6a3024d3bec7ebc898f96a4a23bd1c99f8dbf3f4f47</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/goblin@0.8.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/goblin</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/m4b/goblin</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#goblin@0.9.3">
      <author>m4b &lt;m4b.github.io@gmail.com&gt;, seu &lt;seu@panopticon.re&gt;, Will Glynn &lt;will@willglynn.com&gt;, Philip Craig &lt;philipjcraig@gmail.com&gt;, Lzu Tao &lt;taolzu@gmail.com&gt;</author>
      <name>goblin</name>
      <version>0.9.3</version>
      <description>An impish, cross-platform, ELF, Mach-o, and PE binary parsing and loading crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">daa0a64d21a7eb230583b4c5f4e23b7e4e57974f96620f42a7e75e08ae66d745</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/goblin@0.9.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/goblin</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/m4b/goblin</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#group@0.13.0">
      <author>Sean Bowe &lt;ewillbefull@gmail.com&gt;, Jack Grigg &lt;jack@z.cash&gt;</author>
      <name>group</name>
      <version>0.13.0</version>
      <description>Elliptic curve group traits and utilities</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f0f9ef7462f7c099f518d754361858f86d8a07af53ba9af0fe635bbccb151a63</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/group@0.13.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/group/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/zkcrypto/group</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/zkcrypto/group</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#h2@0.3.27">
      <author>Carl Lerche &lt;me@carllerche.com&gt;, Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>h2</name>
      <version>0.3.27</version>
      <description>An HTTP/2 client and server</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0beca50380b1fc32983fc1cb4587bfa4bb9e78fc259aad4a0032d2080309222d</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/h2@0.3.27</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/h2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/h2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#h2@0.4.12">
      <author>Carl Lerche &lt;me@carllerche.com&gt;, Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>h2</name>
      <version>0.4.12</version>
      <description>An HTTP/2 client and server</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f3c0b69cfcb4e1b9f1bf2f53f95f766e4661169728ec61cd3fe5a0166f2d1386</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/h2@0.4.12</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/h2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/h2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#half@2.6.0">
      <author>Kathryn Long &lt;squeeself@gmail.com&gt;</author>
      <name>half</name>
      <version>2.6.0</version>
      <description>Half-precision floating point f16 and bf16 types for Rust implementing the IEEE 754-2008 standard binary16 and bfloat16 types.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">459196ed295495a68f7d7fe1d84f6c4b7ff0e21fe3017b2f283c6fac3ad803c9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/half@2.6.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/VoidStarKat/half-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#handlebars@6.3.2">
      <author>Ning Sun &lt;sunng@pm.me&gt;</author>
      <name>handlebars</name>
      <version>6.3.2</version>
      <description>Handlebars templating implemented in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">759e2d5aea3287cb1190c8ec394f42866cb5bf74fcbf213f354e3c856ea26098</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/handlebars@6.3.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/crate/handlebars/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/sunng87/handlebars-rust</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/sunng87/handlebars-rust</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hashbrown@0.12.3">
      <author>Amanieu d'Antras &lt;amanieu@gmail.com&gt;</author>
      <name>hashbrown</name>
      <version>0.12.3</version>
      <description>A Rust port of Google's SwissTable hash map</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">8a9ee70c43aaf417c914396645a0fa852624801b24ebb7ae78fe8272889ac888</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/hashbrown@0.12.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-lang/hashbrown</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hashbrown@0.14.5">
      <author>Amanieu d'Antras &lt;amanieu@gmail.com&gt;</author>
      <name>hashbrown</name>
      <version>0.14.5</version>
      <description>A Rust port of Google's SwissTable hash map</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e5274423e17b7c9fc20b6e7e208532f9b19825d82dfd615708b70edd83df41f1</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/hashbrown@0.14.5</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-lang/hashbrown</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hashbrown@0.16.0">
      <author>Amanieu d'Antras &lt;amanieu@gmail.com&gt;</author>
      <name>hashbrown</name>
      <version>0.16.0</version>
      <description>A Rust port of Google's SwissTable hash map</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5419bdc4f6a9207fbeba6d11b604d481addf78ecd10c11ad51e76c2f6482748d</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/hashbrown@0.16.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-lang/hashbrown</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#heck@0.4.1">
      <author>Without Boats &lt;woboats@gmail.com&gt;</author>
      <name>heck</name>
      <version>0.4.1</version>
      <description>heck is a case conversion library.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">95505c38b4572b2d910cecb0281560f54b440a19336cbbcb27bf6ce6adc6f5a8</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/heck@0.4.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/heck</url>
        </reference>
        <reference type="website">
          <url>https://github.com/withoutboats/heck</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/withoutboats/heck</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#heck@0.5.0">
      <name>heck</name>
      <version>0.5.0</version>
      <description>heck is a case conversion library.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2304e00983f87ffb38b55b444b5e3b60a884b5d30c0fca7d82fe33449bbe55ea</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/heck@0.5.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/withoutboats/heck</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hex@0.4.3">
      <author>KokaKiwi &lt;kokakiwi@kokakiwi.net&gt;</author>
      <name>hex</name>
      <version>0.4.3</version>
      <description>Encoding and decoding data into/from hexadecimal representation.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7f24254aa9a54b5c858eaee2f5bccdb46aaf0e486a595ed5fd8f86ba55232a70</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/hex@0.4.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/hex/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/KokaKiwi/rust-hex</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hkdf@0.12.4">
      <author>RustCrypto Developers</author>
      <name>hkdf</name>
      <version>0.12.4</version>
      <description>HMAC-based Extract-and-Expand Key Derivation Function (HKDF)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7b5f8eb2ad728638ea2c7d47a21db23b7b58a72ed6a38256b8a1849f15fbbdf7</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/hkdf@0.12.4</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/RustCrypto/KDFs/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/KDFs/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hmac@0.12.1">
      <author>RustCrypto Developers</author>
      <name>hmac</name>
      <version>0.12.1</version>
      <description>Generic implementation of Hash-based Message Authentication Code (HMAC)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6c49c37c09c17a53d937dfbb742eb3a961d65a994e6bcdcf37e7399d0cc8ab5e</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/hmac@0.12.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/hmac</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/MACs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#home@0.5.11">
      <author>Brian Anderson &lt;andersrb@gmail.com&gt;</author>
      <name>home</name>
      <version>0.5.11</version>
      <description>Shared definitions of home directories.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">589533453244b0995c858700322199b2becb13b627df2851f64a2775d024abcf</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/home@0.5.11</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/home</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-lang/cargo</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/cargo</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#html5ever@0.29.1">
      <author>The html5ever Project Developers</author>
      <name>html5ever</name>
      <version>0.29.1</version>
      <description>High-performance browser-grade HTML5 parser</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3b7410cae13cbc75623c98ac4cbfd1f0bedddf3227afc24f370cf0f50a44a11c</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/html5ever@0.29.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/html5ever</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/html5ever</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#http-body-util@0.1.3">
      <author>Carl Lerche &lt;me@carllerche.com&gt;, Lucio Franco &lt;luciofranco14@gmail.com&gt;, Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>http-body-util</name>
      <version>0.1.3</version>
      <description>Combinators and adapters for HTTP request or response bodies. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b021d93e26becf5dc7e1b75b1bed1fd93124b374ceb73f43d4d4eafec896a64a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/http-body-util@0.1.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/http-body-util</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/http-body</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#http-body@0.4.6">
      <author>Carl Lerche &lt;me@carllerche.com&gt;, Lucio Franco &lt;luciofranco14@gmail.com&gt;, Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>http-body</name>
      <version>0.4.6</version>
      <description>Trait representing an asynchronous, streaming, HTTP request or response body. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7ceab25649e9960c0311ea418d17bee82c0dcec1bd053b5f9a66e265a693bed2</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/http-body@0.4.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/http-body</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/http-body</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#http-body@1.0.1">
      <author>Carl Lerche &lt;me@carllerche.com&gt;, Lucio Franco &lt;luciofranco14@gmail.com&gt;, Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>http-body</name>
      <version>1.0.1</version>
      <description>Trait representing an asynchronous, streaming, HTTP request or response body. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1efedce1fb8e6913f23e0c92de8e62cd5b772a67e7b3946df930a62566c93184</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/http-body@1.0.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/http-body</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/http-body</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#http@0.2.12">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;, Carl Lerche &lt;me@carllerche.com&gt;, Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>http</name>
      <version>0.2.12</version>
      <description>A set of types for representing HTTP requests and responses. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">601cbb57e577e2f5ef5be8e7b83f0f63994f25aa94d673e54a92d5c516d101f1</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/http@0.2.12</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/http</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/http</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#http@1.3.1">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;, Carl Lerche &lt;me@carllerche.com&gt;, Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>http</name>
      <version>1.3.1</version>
      <description>A set of types for representing HTTP requests and responses. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f4a85d31aea989eead29a3aaf9e1115a180df8282431156e533de47660892565</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/http@1.3.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/http</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/http</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#httparse@1.10.1">
      <author>Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>httparse</name>
      <version>1.10.1</version>
      <description>A tiny, safe, speedy, zero-copy HTTP/1.x parser.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6dbf3de79e51f3d586ab4cb9d5c3e2c14aa28ed23d180cf89b4df0454a69cc87</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/httparse@1.10.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/httparse</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/seanmonstar/httparse</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#httpdate@1.0.3">
      <author>Pyfisch &lt;pyfisch@posteo.org&gt;</author>
      <name>httpdate</name>
      <version>1.0.3</version>
      <description>HTTP date parsing and formatting</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">df3b46402a9d5adb4c86a0cf463f42e19994e3ee891101b1841f30a545cb49a9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/httpdate@1.0.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/pyfisch/httpdate</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#humantime@2.3.0">
      <name>humantime</name>
      <version>2.3.0</version>
      <description>A parser and formatter for std::time::{Duration, SystemTime}</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">135b12329e5e3ce057a9f972339ea52bc954fe1e9358ef27f95e89716fbc5424</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/humantime@2.3.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/humantime</url>
        </reference>
        <reference type="website">
          <url>https://github.com/chronotope/humantime</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/chronotope/humantime</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hyper-rustls@0.24.2">
      <name>hyper-rustls</name>
      <version>0.24.2</version>
      <description>Rustls+hyper integration for pure rust HTTPS</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ec3efd23720e2049821a693cbc7e65ea87c72f1c58ff2f9522ff332b1491e590</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR ISC OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/hyper-rustls@0.24.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/hyper-rustls/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rustls/hyper-rustls</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rustls/hyper-rustls</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hyper-rustls@0.27.7">
      <name>hyper-rustls</name>
      <version>0.27.7</version>
      <description>Rustls+hyper integration for pure rust HTTPS</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e3c93eb611681b207e1fe55d5a71ecf91572ec8a6705cdb6857f7d8d5242cf58</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR ISC OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/hyper-rustls@0.27.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/hyper-rustls/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rustls/hyper-rustls</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rustls/hyper-rustls</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hyper-tls@0.6.0">
      <author>Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>hyper-tls</name>
      <version>0.6.0</version>
      <description>Default TLS implementation for use with hyper</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">70206fc6890eaca9fde8a0bf71caa2ddfc9fe045ac9e5c70df101a7dbde866e0</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/hyper-tls@0.6.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/hyper-tls</url>
        </reference>
        <reference type="website">
          <url>https://hyper.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/hyper-tls</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hyper-util@0.1.17">
      <author>Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>hyper-util</name>
      <version>0.1.17</version>
      <description>hyper utilities</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3c6995591a8f1380fcb4ba966a252a4b29188d51d2b89e3a252f5305be65aea8</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/hyper-util@0.1.17</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/hyper-util</url>
        </reference>
        <reference type="website">
          <url>https://hyper.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/hyper-util</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hyper@0.14.32">
      <author>Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>hyper</name>
      <version>0.14.32</version>
      <description>A fast and correct HTTP library.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">41dfc780fdec9373c01bae43289ea34c972e40ee3c9f6b3c8801a35f35586ce7</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/hyper@0.14.32</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/hyper</url>
        </reference>
        <reference type="website">
          <url>https://hyper.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/hyper</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#hyper@1.7.0">
      <author>Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>hyper</name>
      <version>1.7.0</version>
      <description>A protective and efficient HTTP library for all.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">eb3aa54a13a0dfe7fbe3a59e0c76093041720fdc77b110cc0fc260fafb4dc51e</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/hyper@1.7.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/hyper</url>
        </reference>
        <reference type="website">
          <url>https://hyper.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/hyper</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#iana-time-zone@0.1.64">
      <author>Andrew Straw &lt;strawman@astraw.com&gt;, René Kijewski &lt;rene.kijewski@fu-berlin.de&gt;, Ryan Lopopolo &lt;rjl@hyperbo.la&gt;</author>
      <name>iana-time-zone</name>
      <version>0.1.64</version>
      <description>get the IANA time zone for the current system</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">33e57f83510bb73707521ebaffa789ec8caf86f9657cad665b092b581d40e9fb</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/iana-time-zone@0.1.64</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/strawlab/iana-time-zone</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ico@0.4.0">
      <author>Matthew D. Steele &lt;mdsteele@alum.mit.edu&gt;</author>
      <name>ico</name>
      <version>0.4.0</version>
      <description>A library for encoding/decoding ICO image files</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">cc50b891e4acf8fe0e71ef88ec43ad82ee07b3810ad09de10f1d01f072ed4b98</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/ico@0.4.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/mdsteele/rust-ico</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#icu_collections@2.0.0">
      <author>The ICU4X Project Developers</author>
      <name>icu_collections</name>
      <version>2.0.0</version>
      <description>Collection of API for use in ICU libraries.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">200072f5d0e3614556f94a9930d5dc3e0662a652823904c3a75dc3b0af7fee47</hash>
      </hashes>
      <licenses>
        <expression>Unicode-3.0</expression>
      </licenses>
      <purl>pkg:cargo/icu_collections@2.0.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://icu4x.unicode.org</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/unicode-org/icu4x</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#icu_locale_core@2.0.0">
      <author>The ICU4X Project Developers</author>
      <name>icu_locale_core</name>
      <version>2.0.0</version>
      <description>API for managing Unicode Language and Locale Identifiers</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0cde2700ccaed3872079a65fb1a78f6c0a36c91570f28755dda67bc8f7d9f00a</hash>
      </hashes>
      <licenses>
        <expression>Unicode-3.0</expression>
      </licenses>
      <purl>pkg:cargo/icu_locale_core@2.0.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://icu4x.unicode.org</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/unicode-org/icu4x</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#icu_normalizer@2.0.0">
      <author>The ICU4X Project Developers</author>
      <name>icu_normalizer</name>
      <version>2.0.0</version>
      <description>API for normalizing text into Unicode Normalization Forms</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">436880e8e18df4d7bbc06d58432329d6458cc84531f7ac5f024e93deadb37979</hash>
      </hashes>
      <licenses>
        <expression>Unicode-3.0</expression>
      </licenses>
      <purl>pkg:cargo/icu_normalizer@2.0.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://icu4x.unicode.org</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/unicode-org/icu4x</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#icu_normalizer_data@2.0.0">
      <author>The ICU4X Project Developers</author>
      <name>icu_normalizer_data</name>
      <version>2.0.0</version>
      <description>Data for the icu_normalizer crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">00210d6893afc98edb752b664b8890f0ef174c8adbb8d0be9710fa66fbbf72d3</hash>
      </hashes>
      <licenses>
        <expression>Unicode-3.0</expression>
      </licenses>
      <purl>pkg:cargo/icu_normalizer_data@2.0.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://icu4x.unicode.org</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/unicode-org/icu4x</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#icu_properties@2.0.1">
      <author>The ICU4X Project Developers</author>
      <name>icu_properties</name>
      <version>2.0.1</version>
      <description>Definitions for Unicode properties</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">016c619c1eeb94efb86809b015c58f479963de65bdb6253345c1a1276f22e32b</hash>
      </hashes>
      <licenses>
        <expression>Unicode-3.0</expression>
      </licenses>
      <purl>pkg:cargo/icu_properties@2.0.1</purl>
      <externalReferences>
        <reference type="website">
          <url>https://icu4x.unicode.org</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/unicode-org/icu4x</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#icu_properties_data@2.0.1">
      <author>The ICU4X Project Developers</author>
      <name>icu_properties_data</name>
      <version>2.0.1</version>
      <description>Data for the icu_properties crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">298459143998310acd25ffe6810ed544932242d3f07083eee1084d83a71bd632</hash>
      </hashes>
      <licenses>
        <expression>Unicode-3.0</expression>
      </licenses>
      <purl>pkg:cargo/icu_properties_data@2.0.1</purl>
      <externalReferences>
        <reference type="website">
          <url>https://icu4x.unicode.org</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/unicode-org/icu4x</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#icu_provider@2.0.0">
      <author>The ICU4X Project Developers</author>
      <name>icu_provider</name>
      <version>2.0.0</version>
      <description>Trait and struct definitions for the ICU data provider</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">03c80da27b5f4187909049ee2d72f276f0d9f99a42c306bd0131ecfe04d8e5af</hash>
      </hashes>
      <licenses>
        <expression>Unicode-3.0</expression>
      </licenses>
      <purl>pkg:cargo/icu_provider@2.0.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://icu4x.unicode.org</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/unicode-org/icu4x</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ident_case@1.0.1">
      <author>Ted Driggs &lt;ted.driggs@outlook.com&gt;</author>
      <name>ident_case</name>
      <version>1.0.1</version>
      <description>Utility for applying case rules to Rust identifiers.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b9e0384b61958566e926dc50660321d12159025e767c18e043daf26b70104c39</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/ident_case@1.0.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/ident_case/1.0.1</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/TedDriggs/ident_case</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#idna@1.1.0">
      <author>The rust-url developers</author>
      <name>idna</name>
      <version>1.1.0</version>
      <description>IDNA (Internationalizing Domain Names in Applications) and Punycode.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3b0875f23caa03898994f6ddc501886a45c7d3d62d04d2d90788d47be1b1e4de</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/idna@1.1.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/servo/rust-url/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#idna_adapter@1.2.1">
      <author>The rust-url developers</author>
      <name>idna_adapter</name>
      <version>1.2.1</version>
      <description>Back end adapter for idna</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3acae9609540aa318d1bc588455225fb2085b9ed0c4f6bd0d9d5bcd86f1a0344</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/idna_adapter@1.2.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/idna_adapter/latest/idna_adapter/</url>
        </reference>
        <reference type="website">
          <url>https://docs.rs/crate/idna_adapter/latest</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hsivonen/idna_adapter</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ignore@0.4.23">
      <author>Andrew Gallant &lt;jamslam@gmail.com&gt;</author>
      <name>ignore</name>
      <version>0.4.23</version>
      <description>A fast library for efficiently matching ignore files such as `.gitignore` against file paths. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6d89fd380afde86567dfba715db065673989d6253f42b88179abd3eae47bda4b</hash>
      </hashes>
      <licenses>
        <expression>Unlicense OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/ignore@0.4.23</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/ignore</url>
        </reference>
        <reference type="website">
          <url>https://github.com/BurntSushi/ripgrep/tree/master/crates/ignore</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/BurntSushi/ripgrep/tree/master/crates/ignore</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#image-webp@0.2.4">
      <name>image-webp</name>
      <version>0.2.4</version>
      <description>WebP encoding and decoding in pure Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">525e9ff3e1a4be2fbea1fdf0e98686a6d98b4d8f937e1bf7402245af1909e8c3</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/image-webp@0.2.4</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/image-rs/image-webp</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/image-rs/image-webp</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#image@0.25.8">
      <author>The image-rs Developers</author>
      <name>image</name>
      <version>0.25.8</version>
      <description>Imaging library. Provides basic image processing and encoders/decoders for common image formats.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">529feb3e6769d234375c4cf1ee2ce713682b8e76538cb13f9fc23e1400a591e7</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/image@0.25.8</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/image</url>
        </reference>
        <reference type="website">
          <url>https://github.com/image-rs/image</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/image-rs/image</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#imagesize@0.13.0">
      <author>Maid Dog &lt;maiddogsrl@gmail.com&gt;</author>
      <name>imagesize</name>
      <version>0.13.0</version>
      <description>Quick probing of image dimensions without loading the entire file.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">edcd27d72f2f071c64249075f42e205ff93c9a4c5f6c6da53e79ed9f9832c285</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/imagesize@0.13.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/imagesize</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/Roughsketch/imagesize</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#imgref@1.12.0">
      <author>Kornel Lesiński &lt;kornel@geekhood.net&gt;</author>
      <name>imgref</name>
      <version>1.12.0</version>
      <description>A basic 2-dimensional slice for safe and convenient handling of pixel buffers with width, height &amp; stride</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e7c5cedc30da3a610cac6b4ba17597bdf7152cf974e8aab3afb3d54455e371c8</hash>
      </hashes>
      <licenses>
        <expression>CC0-1.0 OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/imgref@1.12.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/imgref/</url>
        </reference>
        <reference type="website">
          <url>https://lib.rs/crates/imgref</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/kornelski/imgref</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#include_dir@0.7.4">
      <author>Michael Bryan &lt;michaelfbryan@gmail.com&gt;</author>
      <name>include_dir</name>
      <version>0.7.4</version>
      <description>Embed the contents of a directory in your binary</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">923d117408f1e49d914f1a379a309cffe4f18c05cf4e3d12e613a15fc81bd0dd</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/include_dir@0.7.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Michael-F-Bryan/include_dir</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#include_dir_macros@0.7.4">
      <author>Michael Bryan &lt;michaelfbryan@gmail.com&gt;</author>
      <name>include_dir_macros</name>
      <version>0.7.4</version>
      <description>The procedural macro used by include_dir</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7cab85a7ed0bd5f0e76d93846e0147172bed2e2d3f859bcc33a8d9699cad1a75</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/include_dir_macros@0.7.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Michael-F-Bryan/include_dir</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#indexmap@1.9.3">
      <name>indexmap</name>
      <version>1.9.3</version>
      <description>A hash table with consistent order and fast iteration.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bd070e393353796e801d209ad339e89596eb4c8d430d18ede6a1cced8fafbd99</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/indexmap@1.9.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/indexmap/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/bluss/indexmap</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#indexmap@2.11.4">
      <name>indexmap</name>
      <version>2.11.4</version>
      <description>A hash table with consistent order and fast iteration.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4b0f83760fb341a774ed326568e19f5a863af4a952def8c39f9ab92fd95b88e5</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/indexmap@2.11.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/indexmap/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/indexmap-rs/indexmap</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#infer@0.19.0">
      <author>Bojan &lt;dbojan@gmail.com&gt;</author>
      <name>infer</name>
      <version>0.19.0</version>
      <description>Small crate to infer file type based on magic number signatures</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">a588916bfdfd92e71cacef98a63d9b1f0d74d6599980d11894290e7ddefffcf7</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/infer@0.19.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/infer</url>
        </reference>
        <reference type="website">
          <url>https://github.com/bojand/infer</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/bojand/infer</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#inlinable_string@0.1.15">
      <author>Nick Fitzgerald &lt;fitzgen@gmail.com&gt;</author>
      <name>inlinable_string</name>
      <version>0.1.15</version>
      <description>The `inlinable_string` crate provides the `InlinableString` type -- an owned, grow-able UTF-8 string that stores small strings inline and avoids heap-allocation -- and the `StringExt` trait which abstracts string operations over both `std::string::String` and `InlinableString` (or even your own custom string type).</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c8fae54786f62fb2918dcfae3d568594e50eb9b5c25bf04371af6fe7516452fb</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/inlinable_string@0.1.15</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://fitzgen.github.io/inlinable_string/inlinable_string/index.html</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/fitzgen/inlinable_string</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#inout@0.1.4">
      <author>RustCrypto Developers</author>
      <name>inout</name>
      <version>0.1.4</version>
      <description>Custom reference types for code generic over in-place and buffer-to-buffer modes of operation.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">879f10e63c20629ecabbb64a8010319738c66a5cd0c29b02d63d272b03751d01</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/inout@0.1.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/inout</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/utils</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ipnet@2.11.0">
      <author>Kris Price &lt;kris@krisprice.nz&gt;</author>
      <name>ipnet</name>
      <version>2.11.0</version>
      <description>Provides types and useful methods for working with IPv4 and IPv6 network addresses, commonly called IP prefixes. The new `IpNet`, `Ipv4Net`, and `Ipv6Net` types build on the existing `IpAddr`, `Ipv4Addr`, and `Ipv6Addr` types already provided in Rust's standard library and align to their design to stay consistent. The module also provides useful traits that extend `Ipv4Addr` and `Ipv6Addr` with methods for `Add`, `Sub`, `BitAnd`, and `BitOr` operations. The module only uses stable feature so it is guaranteed to compile using the stable toolchain.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">469fb0b9cefa57e3ef31275ee7cacb78f2fdca44e4765491884a2b119d4eb130</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/ipnet@2.11.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/ipnet</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/krisprice/ipnet</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#iri-string@0.7.8">
      <author>YOSHIOKA Takuma &lt;nop_thread@nops.red&gt;</author>
      <name>iri-string</name>
      <version>0.7.8</version>
      <description>IRI as string types</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">dbc5ebe9c3a1a7a5127f920a418f7585e9e758e911d0466ed004f393b0e380b2</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/iri-string@0.7.8</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/lo48576/iri-string</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#is-terminal@0.4.16">
      <author>softprops &lt;d.tangren@gmail.com&gt;, Dan Gohman &lt;dev@sunfishcode.online&gt;</author>
      <name>is-terminal</name>
      <version>0.4.16</version>
      <description>Test whether a given stream is a terminal</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e04d7f318608d35d4b61ddd75cbdaee86b023ebe2bd5a66ee0915f0bf93095a9</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/is-terminal@0.4.16</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/is-terminal</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/sunfishcode/is-terminal</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#is_executable@1.0.5">
      <author>Nick Fitzgerald &lt;fitzgen@gmail.com&gt;</author>
      <name>is_executable</name>
      <version>1.0.5</version>
      <description>Is there an executable file at the given path?</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">baabb8b4867b26294d818bf3f651a454b6901431711abb96e296245888d6e8c4</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/is_executable@1.0.5</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/is_executable</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/fitzgen/is_executable</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#is_terminal_polyfill@1.70.1">
      <name>is_terminal_polyfill</name>
      <version>1.70.1</version>
      <description>Polyfill for `is_terminal` stdlib feature for use with older MSRVs</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7943c866cc5cd64cbc25b2e01621d07fa8eb2a1a23160ee81ce38704e97b8ecf</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/is_terminal_polyfill@1.70.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/polyfill-rs/is_terminal_polyfill</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#itertools@0.10.5">
      <author>bluss</author>
      <name>itertools</name>
      <version>0.10.5</version>
      <description>Extra iterator adaptors, iterator methods, free functions, and macros.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b0fd2260e829bddf4cb6ea802289de2f86d6a7a690192fbe91b3f46e0f2c8473</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/itertools@0.10.5</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/itertools/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-itertools/itertools</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#itertools@0.12.1">
      <author>bluss</author>
      <name>itertools</name>
      <version>0.12.1</version>
      <description>Extra iterator adaptors, iterator methods, free functions, and macros.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ba291022dbbd398a455acf126c1e341954079855bc60dfdda641363bd6922569</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/itertools@0.12.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/itertools/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-itertools/itertools</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#itertools@0.13.0">
      <author>bluss</author>
      <name>itertools</name>
      <version>0.13.0</version>
      <description>Extra iterator adaptors, iterator methods, free functions, and macros.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">413ee7dfc52ee1a4949ceeb7dbc8a33f2d6c088194d9f922fb8318faf1f01186</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/itertools@0.13.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/itertools/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-itertools/itertools</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#itoa@1.0.15">
      <author>David Tolnay &lt;dtolnay@gmail.com&gt;</author>
      <name>itoa</name>
      <version>1.0.15</version>
      <description>Fast integer primitive to string conversion</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4a5f13b858c8d314ee3e8f639011f7ccefe71f97f96e50151fb991f267928e2c</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/itoa@1.0.15</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/itoa</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dtolnay/itoa</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#java-properties@2.0.0">
      <author>Adam Crume &lt;adamcrume@gmail.com&gt;</author>
      <name>java-properties</name>
      <version>2.0.0</version>
      <description>A library for reading and writing Java properties files in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">37bf6f484471c451f2b51eabd9e66b3fa7274550c5ec4b6c3d6070840945117f</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/java-properties@2.0.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://adamcrume.github.io/java-properties</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/adamcrume/java-properties</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jiff@0.2.15">
      <author>Andrew Gallant &lt;jamslam@gmail.com&gt;</author>
      <name>jiff</name>
      <version>0.2.15</version>
      <description>A date-time library that encourages you to jump into the pit of success.  This library is heavily inspired by the Temporal project. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">be1f93b8b1eb69c77f24bbb0afdf66f54b632ee39af40ca21c4365a1d7347e49</hash>
      </hashes>
      <licenses>
        <expression>Unlicense OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/jiff@0.2.15</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jiff</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/BurntSushi/jiff</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jobserver@0.1.34">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>jobserver</name>
      <version>0.1.34</version>
      <description>An implementation of the GNU Make jobserver for Rust. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9afb3de4395d6b3e67a780b6de64b51c978ecf11cb9a462c66be7d4ca9039d33</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/jobserver@0.1.34</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jobserver</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-lang/jobserver-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/jobserver-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#json-patch@3.0.1">
      <author>Ivan Dubrov &lt;dubrov.ivan@gmail.com&gt;</author>
      <name>json-patch</name>
      <version>3.0.1</version>
      <description>RFC 6902, JavaScript Object Notation (JSON) Patch</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">863726d7afb6bc2590eeff7135d923545e5e964f004c2ccf8716c25e70a86f08</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/json-patch@3.0.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/idubrov/json-patch</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#json5@0.4.1">
      <author>Callum Oakley &lt;hello@callumoakley.net&gt;</author>
      <name>json5</name>
      <version>0.4.1</version>
      <description>A Rust JSON5 serializer and deserializer which speaks Serde.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">96b0db21af676c1ce64250b5f40f3ce2cf27e4e47cb91ed91eb6fe9350b430c1</hash>
      </hashes>
      <licenses>
        <expression>ISC</expression>
      </licenses>
      <purl>pkg:cargo/json5@0.4.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/callum-oakley/json5-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jsonptr@0.6.3">
      <author>chance dinkins, André Sá de Mello &lt;codasm@pm.me&gt;</author>
      <name>jsonptr</name>
      <version>0.6.3</version>
      <description>Data structures and logic for resolving, assigning, and deleting by JSON Pointers (RFC 6901)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5dea2b27dd239b2556ed7a25ba842fe47fd602e7fc7433c2a8d6106d4d9edd70</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/jsonptr@0.6.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jsonptr</url>
        </reference>
        <reference type="website">
          <url>https://github.com/chanced/jsonptr</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/chanced/jsonptr</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jsonrpsee-client-transport@0.24.9">
      <author>Parity Technologies &lt;admin@parity.io&gt;, Pierre Krieger &lt;pierre.krieger1708@gmail.com&gt;</author>
      <name>jsonrpsee-client-transport</name>
      <version>0.24.9</version>
      <description>JSON-RPC client transports</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bacb85abf4117092455e1573625e21b8f8ef4dec8aff13361140b2dc266cdff2</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/jsonrpsee-client-transport@0.24.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jsonrpsee</url>
        </reference>
        <reference type="website">
          <url>https://www.parity.io/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/paritytech/jsonrpsee</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jsonrpsee-core@0.24.9">
      <author>Parity Technologies &lt;admin@parity.io&gt;, Pierre Krieger &lt;pierre.krieger1708@gmail.com&gt;</author>
      <name>jsonrpsee-core</name>
      <version>0.24.9</version>
      <description>Utilities for jsonrpsee</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">456196007ca3a14db478346f58c7238028d55ee15c1df15115596e411ff27925</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/jsonrpsee-core@0.24.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jsonrpsee</url>
        </reference>
        <reference type="website">
          <url>https://www.parity.io/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/paritytech/jsonrpsee</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jsonrpsee-server@0.24.9">
      <author>Parity Technologies &lt;admin@parity.io&gt;, Pierre Krieger &lt;pierre.krieger1708@gmail.com&gt;</author>
      <name>jsonrpsee-server</name>
      <version>0.24.9</version>
      <description>JSON-RPC server that supports HTTP and WebSocket transports</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">55e363146da18e50ad2b51a0a7925fc423137a0b1371af8235b1c231a0647328</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/jsonrpsee-server@0.24.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jsonrpsee</url>
        </reference>
        <reference type="website">
          <url>https://www.parity.io/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/paritytech/jsonrpsee</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jsonrpsee-types@0.24.9">
      <author>Parity Technologies &lt;admin@parity.io&gt;, Pierre Krieger &lt;pierre.krieger1708@gmail.com&gt;</author>
      <name>jsonrpsee-types</name>
      <version>0.24.9</version>
      <description>JSON-RPC v2 specific types</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">08a8e70baf945b6b5752fc8eb38c918a48f1234daf11355e07106d963f860089</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/jsonrpsee-types@0.24.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jsonrpsee</url>
        </reference>
        <reference type="website">
          <url>https://www.parity.io/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/paritytech/jsonrpsee</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jsonrpsee-ws-client@0.24.9">
      <author>Parity Technologies &lt;admin@parity.io&gt;, Pierre Krieger &lt;pierre.krieger1708@gmail.com&gt;</author>
      <name>jsonrpsee-ws-client</name>
      <version>0.24.9</version>
      <description>JSON-RPC websocket client</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">01b3323d890aa384f12148e8d2a1fd18eb66e9e7e825f9de4fa53bcc19b93eef</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/jsonrpsee-ws-client@0.24.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jsonrpsee</url>
        </reference>
        <reference type="website">
          <url>https://www.parity.io/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/paritytech/jsonrpsee</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jsonrpsee@0.24.9">
      <author>Parity Technologies &lt;admin@parity.io&gt;, Pierre Krieger &lt;pierre.krieger1708@gmail.com&gt;</author>
      <name>jsonrpsee</name>
      <version>0.24.9</version>
      <description>JSON-RPC client/server framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">37b26c20e2178756451cfeb0661fb74c47dd5988cb7e3939de7e9241fd604d42</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/jsonrpsee@0.24.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jsonrpsee</url>
        </reference>
        <reference type="website">
          <url>https://www.parity.io/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/paritytech/jsonrpsee</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jsonschema@0.33.0">
      <author>Dmitry Dygalo &lt;dmitry@dygalo.dev&gt;</author>
      <name>jsonschema</name>
      <version>0.33.0</version>
      <description>JSON schema validaton library</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d46662859bc5f60a145b75f4632fbadc84e829e45df6c5de74cfc8e05acb96b5</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/jsonschema@0.33.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Stranger6667/jsonschema</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#jzon@0.12.5">
      <author>Sandro-Alessio Gierens &lt;sandro@gierens.de&gt;, Maciej Hirsz &lt;hello@maciej.codes&gt;</author>
      <name>jzon</name>
      <version>0.12.5</version>
      <description>Continuation of json-rust, a JSON implementation in Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">17ab85f84ca42c5ec520e6f3c9966ba1fd62909ce260f8837e248857d2560509</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/jzon@0.12.5</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/jzon/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rustadopt/jzon-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#keyboard-types@0.7.0">
      <author>Pyfisch &lt;pyfisch@posteo.org&gt;</author>
      <name>keyboard-types</name>
      <version>0.7.0</version>
      <description>Contains types to define keyboard related events.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b750dcadc39a09dbadd74e118f6dd6598df77fa01df0cfcdc52c28dece74528a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/keyboard-types@0.7.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/pyfisch/keyboard-types</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#konst@0.3.16">
      <author>rodrimati1992 &lt;rodrimatt1985@gmail.com&gt;</author>
      <name>konst</name>
      <version>0.3.16</version>
      <description>Const equivalents of std functions, compile-time comparison, and parsing</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4381b9b00c55f251f2ebe9473aef7c117e96828def1a7cb3bd3f0f903c6894e9</hash>
      </hashes>
      <licenses>
        <expression>Zlib</expression>
      </licenses>
      <purl>pkg:cargo/konst@0.3.16</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/konst/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rodrimati1992/konst/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#konst_kernel@0.3.15">
      <author>rodrimati1992 &lt;rodrimatt1985@gmail.com&gt;</author>
      <name>konst_kernel</name>
      <version>0.3.15</version>
      <description>Foundational const functionality shared between konst and const_panic</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e4b1eb7788f3824c629b1116a7a9060d6e898c358ebff59070093d51103dcc3c</hash>
      </hashes>
      <licenses>
        <expression>Zlib</expression>
      </licenses>
      <purl>pkg:cargo/konst_kernel@0.3.15</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/konst/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rodrimati1992/konst/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#kuchikiki@0.8.8-speedreader">
      <author>Brave Authors, Ralph Giles &lt;rgiles@brave.com&gt;, Simon Sapin &lt;simon.sapin@exyr.org&gt;</author>
      <name>kuchikiki</name>
      <version>0.8.8-speedreader</version>
      <description>(口利き) HTML tree manipulation library</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">02cb977175687f33fa4afa0c95c112b987ea1443e5a51c8f8ff27dc618270cc2</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/kuchikiki@0.8.8-speedreader</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/brave/kuchikiki</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#kurbo@0.11.3">
      <author>Raph Levien &lt;raph.levien@gmail.com&gt;</author>
      <name>kurbo</name>
      <version>0.11.3</version>
      <description>A 2D curves library</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c62026ae44756f8a599ba21140f350303d4f08dcdcc71b5ad9c9bb8128c13c62</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/kurbo@0.11.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/linebender/kurbo</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#lazy_static@1.5.0">
      <author>Marvin Löbel &lt;loebel.marvin@gmail.com&gt;</author>
      <name>lazy_static</name>
      <version>1.5.0</version>
      <description>A macro for declaring lazily evaluated statics in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bbd2bcb4c963f2ddae06a2efc7e9f3591312473c50c6685e1f298068316e66fe</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/lazy_static@1.5.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/lazy_static</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang-nursery/lazy-static.rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#lebe@0.5.3">
      <author>johannesvollmer &lt;contact@johannesvollmer.com&gt;</author>
      <name>lebe</name>
      <version>0.5.3</version>
      <description>Tiny, dead simple, high performance endianness conversions with a generic API</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7a79a3332a6609480d7d0c9eab957bca6b455b91bb84e66d19f5ff66294b85b8</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/lebe@0.5.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/crate/lebe/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/johannesvollmer/lebe</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#libc@0.2.176">
      <author>The Rust Project Developers</author>
      <name>libc</name>
      <version>0.2.176</version>
      <description>Raw FFI bindings to platform libraries like libc.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">58f929b4d672ea937a23a1ab494143d968337a5f47e56d0815df1e0890ddf174</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/libc@0.2.176</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-lang/libc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#libm@0.2.15">
      <author>Jorge Aparicio &lt;jorge@japaric.io&gt;</author>
      <name>libm</name>
      <version>0.2.15</version>
      <description>libm in pure Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f9fbbcab51052fe104eb5e5d351cf728d30a5be1fe14d9be8a3b097481fb97de</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/libm@0.2.15</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/libm</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/compiler-builtins</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#libz-rs-sys@0.5.2">
      <name>libz-rs-sys</name>
      <version>0.5.2</version>
      <description>A memory-safe zlib implementation written in rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">840db8cf39d9ec4dd794376f38acc40d0fc65eec2a8f484f7fd375b84602becd</hash>
      </hashes>
      <licenses>
        <expression>Zlib</expression>
      </licenses>
      <purl>pkg:cargo/libz-rs-sys@0.5.2</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/trifectatechfoundation/zlib-rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/trifectatechfoundation/zlib-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#litemap@0.8.0">
      <author>The ICU4X Project Developers</author>
      <name>litemap</name>
      <version>0.8.0</version>
      <description>A key-value Map implementation based on a flat, sorted Vec.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">241eaef5fd12c88705a01fc1066c48c4b36e0dd4377dcdc7ec3942cea7a69956</hash>
      </hashes>
      <licenses>
        <expression>Unicode-3.0</expression>
      </licenses>
      <purl>pkg:cargo/litemap@0.8.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/litemap</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/unicode-org/icu4x</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#local-ip-address@0.6.5">
      <author>Leo Borai &lt;estebanborai@gmail.com&gt;</author>
      <name>local-ip-address</name>
      <version>0.6.5</version>
      <description>Retrieve system's local IP address and Network Interfaces/Adapters on Linux, macOS and Windows.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">656b3b27f8893f7bbf9485148ff9a65f019e3f33bd5cdc87c83cab16b3fd9ec8</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/local-ip-address@0.6.5</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/LeoBorai/local-ip-address</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/LeoBorai/local-ip-address</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#lock_api@0.4.14">
      <author>Amanieu d'Antras &lt;amanieu@gmail.com&gt;</author>
      <name>lock_api</name>
      <version>0.4.14</version>
      <description>Wrappers to create fully-featured Mutex and RwLock types. Compatible with no_std.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">224399e74b87b5f3557511d98dff8b14089b3dadafcab6bb93eab67d3aace965</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/lock_api@0.4.14</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Amanieu/parking_lot</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#log@0.4.28">
      <author>The Rust Project Developers</author>
      <name>log</name>
      <version>0.4.28</version>
      <description>A lightweight logging facade for Rust </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">34080505efa8e45a4b816c349525ebe327ceaa8559756f0356cba97ef3bf7432</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/log@0.4.28</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/log</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-lang/log</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#loop9@0.1.5">
      <author>Kornel &lt;kornel@geekhood.net&gt;</author>
      <name>loop9</name>
      <version>0.1.5</version>
      <description>Tiny helper function to visit every pixel in the image together with its neighboring pixels. Duplicates pixels on the edges.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0fae87c125b03c1d2c0150c90365d7d6bcc53fb73a9acaef207d2d065860f062</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/loop9@0.1.5</purl>
      <externalReferences>
        <reference type="website">
          <url>https://lib.rs/crates/loop9</url>
        </reference>
        <reference type="vcs">
          <url>https://gitlab.com/kornelski/loop9.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#lru-slab@0.1.2">
      <author>Benjamin Saunders &lt;ben.e.saunders@gmail.com&gt;</author>
      <name>lru-slab</name>
      <version>0.1.2</version>
      <description>Pre-allocated storage with constant-time LRU tracking</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">112b39cec0b298b6c1999fee3e31427f74f676e4cb9879ed1a121b43661a4154</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0 OR Zlib</expression>
      </licenses>
      <purl>pkg:cargo/lru-slab@0.1.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Ralith/lru-slab</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#lzma-sys@0.1.20">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;</author>
      <name>lzma-sys</name>
      <version>0.1.20</version>
      <description>Raw bindings to liblzma which contains an implementation of LZMA and xz stream encoding/decoding.  High level Rust bindings are available in the `xz2` crate. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5fda04ab3764e6cde78b9974eec4f779acaba7c4e84b36eca3cf77c581b85d27</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/lzma-sys@0.1.20</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/lzma-sys</url>
        </reference>
        <reference type="website">
          <url>https://github.com/alexcrichton/xz2-rs</url>
        </reference>
        <reference type="other">
          <url>lzma</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/alexcrichton/xz2-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#mac@0.1.1">
      <author>Jonathan Reem &lt;jonathan.reem@gmail.com&gt;</author>
      <name>mac</name>
      <version>0.1.1</version>
      <description>A collection of great and ubiqutitous macros.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c41e0c4fef86961ac6d6f8a82609f55f31b05e4fce149ac5710e439df7619ba4</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/mac@0.1.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/reem/rust-mac.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#magic_string@0.3.4">
      <author>h-a-n-a &lt;andywangsy@gmail.com&gt;</author>
      <name>magic_string</name>
      <version>0.3.4</version>
      <description>magic string</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6c8033ce8c43f7ccb207e4699f30eed50d7526379ee08fab47159f80b7934e18</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/magic_string@0.3.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/h-a-n-a/magic-string-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#malloc_buf@0.0.6">
      <author>Steven Sheldon</author>
      <name>malloc_buf</name>
      <version>0.0.6</version>
      <description>Structs for handling malloc'd memory passed to Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">62bb907fe88d54d8d9ce32a3cceab4218ed2f6b7d35617cafe9adf84e43919cb</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/malloc_buf@0.0.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://ssheldon.github.io/malloc_buf/malloc_buf/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/SSheldon/malloc_buf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#markup5ever@0.14.1">
      <author>The html5ever Project Developers</author>
      <name>markup5ever</name>
      <version>0.14.1</version>
      <description>Common code for xml5ever and html5ever</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c7a7213d12e1864c0f002f52c2923d4556935a43dec5e71355c2760e0f6e7a18</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/markup5ever@0.14.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/markup5ever</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/servo/html5ever</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#match_token@0.1.0">
      <name>match_token</name>
      <version>0.1.0</version>
      <description>Procedural macro for html5ever.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">88a9689d8d44bf9964484516275f5cd4c9b59457a6940c1d5d0ecbb94510a36b</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/match_token@0.1.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/servo/html5ever</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#matches@0.1.10">
      <name>matches</name>
      <version>0.1.10</version>
      <description>A macro to evaluate, as a boolean, whether an expression matches a pattern.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2532096657941c2fea9c289d370a250971c689d4f143798ff67113ec042024a5</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/matches@0.1.10</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/matches/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/SimonSapin/rust-std-candidates</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#matchit@0.8.4">
      <author>Ibraheem Ahmed &lt;ibraheem@ibraheem.ca&gt;</author>
      <name>matchit</name>
      <version>0.8.4</version>
      <description>A high performance, zero-copy URL router.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">47e1ffaa40ddd1f3ed91f717a33c8c0ee23fff369e3aa8772b9605cc1d22f4c3</hash>
      </hashes>
      <licenses>
        <expression>MIT AND BSD-3-Clause</expression>
      </licenses>
      <purl>pkg:cargo/matchit@0.8.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/ibraheemdev/matchit</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#maybe-rayon@0.1.1">
      <name>maybe-rayon</name>
      <version>0.1.1</version>
      <description>Either acts as rayon or creates a single-threaded facade</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">8ea1f30cedd69f0a2954655f7188c6a834246d2bcf1e315e2ac40c4b24dc9519</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/maybe-rayon@0.1.1</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/shssoichiro/maybe-rayon</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/shssoichiro/maybe-rayon</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#md-5@0.10.6">
      <author>RustCrypto Developers</author>
      <name>md-5</name>
      <version>0.10.6</version>
      <description>MD5 hash function</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d89e7ee0cfbedfc4da3340218492196241d89eefb6dab27de5df917a6d2e78cf</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/md-5@0.10.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/md-5</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/hashes</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#memchr@2.7.6">
      <author>Andrew Gallant &lt;jamslam@gmail.com&gt;, bluss</author>
      <name>memchr</name>
      <version>2.7.6</version>
      <description>Provides extremely fast (uses SIMD on x86_64, aarch64 and wasm32) routines for 1, 2 or 3 byte search and single substring search. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f52b00d39961fc5b2736ea853c9cc86238e165017a493d1d5c8eac6bdc4cc273</hash>
      </hashes>
      <licenses>
        <expression>Unlicense OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/memchr@2.7.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/memchr/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/BurntSushi/memchr</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/BurntSushi/memchr</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#memmap2@0.9.8">
      <author>Dan Burkert &lt;dan@danburkert.com&gt;, Yevhenii Reizner &lt;razrfalcon@gmail.com&gt;</author>
      <name>memmap2</name>
      <version>0.9.8</version>
      <description>Cross-platform Rust API for memory-mapped file IO</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">843a98750cd611cc2965a8213b53b43e715f13c37a9e096c6408e69990961db7</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/memmap2@0.9.8</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/memmap2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RazrFalcon/memmap2-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#memoffset@0.9.1">
      <author>Gilad Naaman &lt;gilad.naaman@gmail.com&gt;</author>
      <name>memoffset</name>
      <version>0.9.1</version>
      <description>offset_of functionality for Rust structs.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">488016bfae457b036d996092f6cb448677611ce4449e970ceaf42695203f218a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/memoffset@0.9.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Gilnaa/memoffset</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#mime@0.3.17">
      <author>Sean McArthur &lt;sean@seanmonstar.com&gt;</author>
      <name>mime</name>
      <version>0.3.17</version>
      <description>Strongly Typed Mimes</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6877bb514081ee2a7ff5ef9de3281f14a4dd4bceac4c09388074a6b5df8a139a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/mime@0.3.17</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/mime</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hyperium/mime</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#minicbor-derive@0.13.0">
      <author>Toralf Wittner &lt;tw@dtex.org&gt;</author>
      <name>minicbor-derive</name>
      <version>0.13.0</version>
      <description>Derive minicbor `Decode` and `Encode` traits.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1154809406efdb7982841adb6311b3d095b46f78342dd646736122fe6b19e267</hash>
      </hashes>
      <licenses>
        <expression>BlueOak-1.0.0</expression>
      </licenses>
      <purl>pkg:cargo/minicbor-derive@0.13.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://twittner.gitlab.io/minicbor/minicbor_derive/</url>
        </reference>
        <reference type="vcs">
          <url>https://gitlab.com/twittner/minicbor</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#minicbor@0.20.0">
      <author>Toralf Wittner &lt;tw@dtex.org&gt;</author>
      <name>minicbor</name>
      <version>0.20.0</version>
      <description>A small CBOR codec suitable for no_std environments.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9d15f4203d71fdf90903c2696e55426ac97a363c67b218488a73b534ce7aca10</hash>
      </hashes>
      <licenses>
        <expression>BlueOak-1.0.0</expression>
      </licenses>
      <purl>pkg:cargo/minicbor@0.20.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://twittner.gitlab.io/minicbor/minicbor/</url>
        </reference>
        <reference type="vcs">
          <url>https://gitlab.com/twittner/minicbor</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#minimal-lexical@0.2.1">
      <author>Alex Huszagh &lt;ahuszagh@gmail.com&gt;</author>
      <name>minimal-lexical</name>
      <version>0.2.1</version>
      <description>Fast float parsing conversion routines.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">68354c5c6bd36d73ff3feceb05efa59b6acb7626617f4962be322a825e61f79a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/minimal-lexical@0.2.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/minimal-lexical</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/Alexhuszagh/minimal-lexical</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#minisign-verify@0.2.4">
      <author>Frank Denis &lt;github@pureftpd.org&gt;</author>
      <name>minisign-verify</name>
      <version>0.2.4</version>
      <description>A small, zero-dependencies crate to verify Minisign signatures.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e856fdd13623a2f5f2f54676a4ee49502a96a80ef4a62bcedd23d52427c44d43</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/minisign-verify@0.2.4</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/jedisct1/rust-minisign-verify</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/jedisct1/rust-minisign-verify</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#minisign@0.7.3">
      <author>Frank Denis &lt;github@pureftpd.org&gt;, Daniel Rangel &lt;daniel@rangel.in&gt;</author>
      <name>minisign</name>
      <version>0.7.3</version>
      <description>A crate to sign files and verify signatures.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b23ef13ff1d745b1e52397daaa247e333c607f3cff96d4df2b798dc252db974b</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/minisign@0.7.3</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/jedisct1/rust-minisign</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/jedisct1/rust-minisign</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#miniz_oxide@0.8.9">
      <author>Frommi &lt;daniil.liferenko@gmail.com&gt;, oyvindln &lt;oyvindln@users.noreply.github.com&gt;, Rich Geldreich richgel99@gmail.com</author>
      <name>miniz_oxide</name>
      <version>0.8.9</version>
      <description>DEFLATE compression and decompression library rewritten in Rust based on miniz</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1fa76a2c86f704bdb222d66965fb3d63269ce38518b83cb0575fca855ebb6316</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Zlib OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/miniz_oxide@0.8.9</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/miniz_oxide</url>
        </reference>
        <reference type="website">
          <url>https://github.com/Frommi/miniz_oxide/tree/master/miniz_oxide</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/Frommi/miniz_oxide/tree/master/miniz_oxide</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#mio@1.0.4">
      <author>Carl Lerche &lt;me@carllerche.com&gt;, Thomas de Zeeuw &lt;thomasdezeeuw@gmail.com&gt;, Tokio Contributors &lt;team@tokio.rs&gt;</author>
      <name>mio</name>
      <version>1.0.4</version>
      <description>Lightweight non-blocking I/O.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">78bed444cc8a2160f01cbcf811ef18cac863ad68ae8ca62092e8db51d51c761c</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/mio@1.0.4</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/tokio-rs/mio</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/tokio-rs/mio</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#mockall@0.13.1">
      <author>Alan Somers &lt;asomers@gmail.com&gt;</author>
      <name>mockall</name>
      <version>0.13.1</version>
      <description>A powerful mock object library for Rust. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">39a6bfcc6c8c7eed5ee98b9c3e33adc726054389233e201c95dab2d41a3839d2</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/mockall@0.13.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/mockall</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/asomers/mockall</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#mockall_derive@0.13.1">
      <author>Alan Somers &lt;asomers@gmail.com&gt;</author>
      <name>mockall_derive</name>
      <version>0.13.1</version>
      <description>Procedural macros for Mockall </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">25ca3004c2efe9011bd4e461bd8256445052b9615405b4f7ea43fc8ca5c20898</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/mockall_derive@0.13.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/mockall_derive</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/asomers/mockall</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#moxcms@0.7.6">
      <author>Radzivon Bartoshyk</author>
      <name>moxcms</name>
      <version>0.7.6</version>
      <description>Simple Color Management in Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1cc7d85f3d741164e8972ad355e26ac6e51b20fcae5f911c7da8f2d8bbbb3f33</hash>
      </hashes>
      <licenses>
        <expression>BSD-3-Clause OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/moxcms@0.7.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://github.com/awxkee/moxcms</url>
        </reference>
        <reference type="website">
          <url>https://github.com/awxkee/moxcms</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/awxkee/moxcms.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#muda@0.17.1">
      <name>muda</name>
      <version>0.17.1</version>
      <description>Menu Utilities for Desktop Applications</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">01c1738382f66ed56b3b9c8119e794a2e23148ac8ea214eda86622d4cb9d415a</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/muda@0.17.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/muda</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/amrbashir/muda</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#native-tls@0.2.14">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>native-tls</name>
      <version>0.2.14</version>
      <description>A wrapper over a platform's native TLS implementation</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">87de3442987e9dbec73158d5c715e7ad9072fda936bb03d19d7fa10e00520f0e</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/native-tls@0.2.14</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-native-tls</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#new_debug_unreachable@1.0.6">
      <author>Matt Brubeck &lt;mbrubeck@limpet.net&gt;, Jonathan Reem &lt;jonathan.reem@gmail.com&gt;</author>
      <name>new_debug_unreachable</name>
      <version>1.0.6</version>
      <description>panic in debug, intrinsics::unreachable() in release (fork of debug_unreachable)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">650eef8c711430f1a879fdd01d4745a7deea475becfb90269c06775983bbf086</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/new_debug_unreachable@1.0.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/new_debug_unreachable</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/mbrubeck/rust-debug-unreachable</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#nix@0.30.1">
      <author>The nix-rust Project Developers</author>
      <name>nix</name>
      <version>0.30.1</version>
      <description>Rust friendly bindings to *nix APIs</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">74523f3a35e05aba87a1d978330aef40f67b0304ac79c1c00b294c9830543db6</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/nix@0.30.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/nix-rust/nix</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#nodrop@0.1.14">
      <author>bluss</author>
      <name>nodrop</name>
      <version>0.1.14</version>
      <description>A wrapper type to inhibit drop (destructor).  ***Deprecated: Use ManuallyDrop or MaybeUninit instead!*** </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">72ef4a56884ca558e5ddb05a1d1e7e1bfd9a68d9ed024c21704cc98872dae1bb</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/nodrop@0.1.14</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/nodrop/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/bluss/arrayvec</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#nom@7.1.3">
      <author>contact@geoffroycouprie.com</author>
      <name>nom</name>
      <version>7.1.3</version>
      <description>A byte-oriented, zero-copy, parser combinators library</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d273983c5a657a70a3e8f2a01329822f3b8c8172b73826411a55751e404a0a4a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/nom@7.1.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/nom</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/Geal/nom</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#nonmax@0.5.5">
      <author>Lucien Greathouse &lt;me@lpghatguy.com&gt;</author>
      <name>nonmax</name>
      <version>0.5.5</version>
      <description>Numeric types that cannot hold maximum values</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">610a5acd306ec67f907abe5567859a3c693fb9886eb1f012ab8f2a47bef3db51</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/nonmax@0.5.5</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/nonmax</url>
        </reference>
        <reference type="website">
          <url>https://github.com/LPGhatguy/nonmax</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/LPGhatguy/nonmax</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#noop_proc_macro@0.3.0">
      <author>Luca Barbato &lt;lu_zero@gentoo.org&gt;</author>
      <name>noop_proc_macro</name>
      <version>0.3.0</version>
      <description>No-op proc_macro, literally does nothing</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0676bb32a98c1a483ce53e500a81ad9c3d5b3f7c920c28c24e9cb0980d0b5bc8</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/noop_proc_macro@0.3.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/lu-zero/noop_proc_macro</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#notify-debouncer-full@0.6.0">
      <author>Daniel Faust &lt;hessijames@gmail.com&gt;</author>
      <name>notify-debouncer-full</name>
      <version>0.6.0</version>
      <description>notify event debouncer optimized for ease of use</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">375bd3a138be7bfeff3480e4a623df4cbfb55b79df617c055cd810ba466fa078</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/notify-debouncer-full@0.6.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/notify-debouncer-full</url>
        </reference>
        <reference type="website">
          <url>https://github.com/notify-rs/notify</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/notify-rs/notify.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#notify-types@2.0.0">
      <author>Daniel Faust &lt;hessijames@gmail.com&gt;</author>
      <name>notify-types</name>
      <version>2.0.0</version>
      <description>Types used by the notify crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5e0826a989adedc2a244799e823aece04662b66609d96af8dff7ac6df9a8925d</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/notify-types@2.0.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/notify-types</url>
        </reference>
        <reference type="website">
          <url>https://github.com/notify-rs/notify</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/notify-rs/notify.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#notify@8.2.0">
      <author>Félix Saparelli &lt;me@passcod.name&gt;, Daniel Faust &lt;hessijames@gmail.com&gt;, Aron Heinecke &lt;Ox0p54r36@t-online.de&gt;</author>
      <name>notify</name>
      <version>8.2.0</version>
      <description>Cross-platform filesystem notification library</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4d3d07927151ff8575b7087f245456e549fea62edf0ec4e565a5ee50c8402bc3</hash>
      </hashes>
      <licenses>
        <expression>CC0-1.0</expression>
      </licenses>
      <purl>pkg:cargo/notify@8.2.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/notify</url>
        </reference>
        <reference type="website">
          <url>https://github.com/notify-rs/notify</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/notify-rs/notify.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-bigint-dig@0.8.4">
      <author>dignifiedquire &lt;dignifiedquire@gmail.com&gt;, The Rust Project Developers</author>
      <name>num-bigint-dig</name>
      <version>0.8.4</version>
      <description>Big integer implementation for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">dc84195820f291c7697304f3cbdadd1cb7199c0efc917ff5eafd71225c136151</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-bigint-dig@0.8.4</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-bigint-dig</url>
        </reference>
        <reference type="website">
          <url>https://github.com/dignifiedquire/num-bigint</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dignifiedquire/num-bigint</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-bigint@0.4.6">
      <author>The Rust Project Developers</author>
      <name>num-bigint</name>
      <version>0.4.6</version>
      <description>Big integer implementation for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">a5e44f723f1133c9deac646763579fdb3ac745e418f2a7af9cd0c431da1f20b9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-bigint@0.4.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-bigint</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-num/num-bigint</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-num/num-bigint</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-cmp@0.1.0">
      <author>Kang Seonghoon &lt;public+git@mearie.org&gt;</author>
      <name>num-cmp</name>
      <version>0.1.0</version>
      <description>Comparison between differently typed numbers</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">63335b2e2c34fae2fb0aa2cecfd9f0832a1e24b3b32ecec612c3426d46dc8aaa</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-cmp@0.1.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-cmp/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/lifthrasiir/num-cmp</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/lifthrasiir/num-cmp</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-complex@0.4.6">
      <author>The Rust Project Developers</author>
      <name>num-complex</name>
      <version>0.4.6</version>
      <description>Complex numbers implementation for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">73f88a1307638156682bada9d7604135552957b7818057dcef22705b4d509495</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-complex@0.4.6</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-complex</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-num/num-complex</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-num/num-complex</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-conv@0.1.0">
      <author>Jacob Pratt &lt;jacob@jhpratt.dev&gt;</author>
      <name>num-conv</name>
      <version>0.1.0</version>
      <description>`num_conv` is a crate to convert between integer types without using `as` casts. This provides better certainty when refactoring, makes the exact behavior of code more explicit, and allows using turbofish syntax. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">51d515d32fb182ee37cda2ccdcb92950d6a3c2893aa280e540671c2cd0f3b1d9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-conv@0.1.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/jhpratt/num-conv</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-derive@0.4.2">
      <author>The Rust Project Developers</author>
      <name>num-derive</name>
      <version>0.4.2</version>
      <description>Numeric syntax extensions</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ed3955f1a9c7c0c15e092f9c887db08b1fc683305fdf6eb6684f22555355e202</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-derive@0.4.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-derive</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-num/num-derive</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-num/num-derive</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-integer@0.1.46">
      <author>The Rust Project Developers</author>
      <name>num-integer</name>
      <version>0.1.46</version>
      <description>Integer traits and functions</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7969661fd2958a5cb096e56c8e1ad0444ac2bbcd0061bd28660485a44879858f</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-integer@0.1.46</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-integer</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-num/num-integer</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-num/num-integer</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-iter@0.1.45">
      <author>The Rust Project Developers</author>
      <name>num-iter</name>
      <version>0.1.45</version>
      <description>External iterators for generic mathematics</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1429034a0490724d0075ebb2bc9e875d6503c3cf69e235a8941aa757d83ef5bf</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-iter@0.1.45</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-iter</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-num/num-iter</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-num/num-iter</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-modular@0.6.1">
      <name>num-modular</name>
      <version>0.6.1</version>
      <description>Implementation of efficient integer division and modular arithmetic operations with generic number types. Supports various backends including num-bigint, etc.. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">17bb261bf36fa7d83f4c294f834e91256769097b3cb505d44831e0a179ac647f</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-modular@0.6.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-modular</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/cmpute/num-modular</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-order@1.2.0">
      <name>num-order</name>
      <version>1.2.0</version>
      <description>Numerically consistent `Eq`, `Ord` and `Hash` implementations for various `num` types (`u32`, `f64`, `num_bigint::BigInt`, etc.)</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">537b596b97c40fcf8056d153049eb22f481c17ebce72a513ec9286e4986d1bb6</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-order@1.2.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-order</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/cmpute/num-order</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-rational@0.4.2">
      <author>The Rust Project Developers</author>
      <name>num-rational</name>
      <version>0.4.2</version>
      <description>Rational numbers implementation for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f83d14da390562dca69fc84082e73e548e1ad308d24accdedd2720017cb37824</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-rational@0.4.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-rational</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-num/num-rational</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-num/num-rational</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num-traits@0.2.19">
      <author>The Rust Project Developers</author>
      <name>num-traits</name>
      <version>0.2.19</version>
      <description>Numeric traits for generic mathematics</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">071dfc062690e90b734c0b2273ce72ad0ffa95f0c74596bc250dcfd960262841</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num-traits@0.2.19</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num-traits</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-num/num-traits</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-num/num-traits</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num@0.4.3">
      <author>The Rust Project Developers</author>
      <name>num</name>
      <version>0.4.3</version>
      <description>A collection of numeric types and traits for Rust, including bigint, complex, rational, range iterators, generic integers, and more! </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">35bd024e8b2ff75562e5f34e7f4905839deb4b22955ef5e73d2fea1b9813cb23</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num@0.4.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/num</url>
        </reference>
        <reference type="website">
          <url>https://github.com/rust-num/num</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rust-num/num</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#num_threads@0.1.7">
      <author>Jacob Pratt &lt;open-source@jhpratt.dev&gt;</author>
      <name>num_threads</name>
      <version>0.1.7</version>
      <description>A minimal library that determines the number of running threads for the current process.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5c7398b9c8b70908f6371f47ed36737907c87c52af34c268fed0bf0ceb92ead9</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/num_threads@0.1.7</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/jhpratt/num_threads</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc-sys@0.3.5">
      <author>Mads Marquart &lt;mads@marquart.dk&gt;</author>
      <name>objc-sys</name>
      <version>0.3.5</version>
      <description>Raw bindings to the Objective-C runtime and ABI</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">cdb91bdd390c7ce1a8607f35f3ca7151b65afc0ff5ff3b34fa350f7d7c7e4310</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc-sys@0.3.5</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/objc-sys/</url>
        </reference>
        <reference type="other">
          <url>objc_0_3</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-app-kit@0.3.2">
      <name>objc2-app-kit</name>
      <version>0.3.2</version>
      <description>Bindings to the AppKit framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d49e936b501e5c5bf01fda3a9452ff86dc3ea98ad5f283e1455153142d97518c</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-app-kit@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-cloud-kit@0.3.2">
      <name>objc2-cloud-kit</name>
      <version>0.3.2</version>
      <description>Bindings to the CloudKit framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">73ad74d880bb43877038da939b7427bba67e9dd42004a18b809ba7d87cee241c</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-cloud-kit@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-core-data@0.3.2">
      <name>objc2-core-data</name>
      <version>0.3.2</version>
      <description>Bindings to the CoreData framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0b402a653efbb5e82ce4df10683b6b28027616a2715e90009947d50b8dd298fa</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-core-data@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-core-foundation@0.3.2">
      <name>objc2-core-foundation</name>
      <version>0.3.2</version>
      <description>Bindings to the CoreFoundation framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2a180dd8642fa45cdb7dd721cd4c11b1cadd4929ce112ebd8b9f5803cc79d536</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-core-foundation@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-core-graphics@0.3.2">
      <name>objc2-core-graphics</name>
      <version>0.3.2</version>
      <description>Bindings to the CoreGraphics framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e022c9d066895efa1345f8e33e584b9f958da2fd4cd116792e15e07e4720a807</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-core-graphics@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-core-image@0.3.2">
      <name>objc2-core-image</name>
      <version>0.3.2</version>
      <description>Bindings to the CoreImage framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e5d563b38d2b97209f8e861173de434bd0214cf020e3423a52624cd1d989f006</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-core-image@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-core-text@0.3.2">
      <name>objc2-core-text</name>
      <version>0.3.2</version>
      <description>Bindings to the CoreText framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0cde0dfb48d25d2b4862161a4d5fcc0e3c24367869ad306b0c9ec0073bfed92d</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-core-text@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-core-video@0.3.2">
      <name>objc2-core-video</name>
      <version>0.3.2</version>
      <description>Bindings to the CoreVideo framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d425caf1df73233f29fd8a5c3e5edbc30d2d4307870f802d18f00d83dc5141a6</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-core-video@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-encode@4.1.0">
      <author>Mads Marquart &lt;mads@marquart.dk&gt;</author>
      <name>objc2-encode</name>
      <version>4.1.0</version>
      <description>Objective-C type-encoding representation and parsing</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ef25abbcd74fb2609453eb695bd2f860d389e457f67dc17cafc8b8cbc89d0c33</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-encode@4.1.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-exception-helper@0.1.1">
      <author>Mads Marquart &lt;mads@marquart.dk&gt;</author>
      <name>objc2-exception-helper</name>
      <version>0.1.1</version>
      <description>External helper function for catching Objective-C exceptions</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c7a1c5fbb72d7735b076bb47b578523aedc40f3c439bea6dfd595c089d79d98a</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-exception-helper@0.1.1</purl>
      <externalReferences>
        <reference type="other">
          <url>objc2_exception_helper_0_1</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-foundation@0.2.2">
      <name>objc2-foundation</name>
      <version>0.2.2</version>
      <description>Bindings to the Foundation framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0ee638a5da3799329310ad4cfa62fbf045d5f56e3ef5ba4149e7452dcf89d5a8</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-foundation@0.2.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-foundation@0.3.2">
      <name>objc2-foundation</name>
      <version>0.3.2</version>
      <description>Bindings to the Foundation framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e3e0adef53c21f888deb4fa59fc59f7eb17404926ee8a6f59f5df0fd7f9f3272</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-foundation@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-io-surface@0.3.2">
      <name>objc2-io-surface</name>
      <version>0.3.2</version>
      <description>Bindings to the IOSurface framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">180788110936d59bab6bd83b6060ffdfffb3b922ba1396b312ae795e1de9d81d</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-io-surface@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-javascript-core@0.3.2">
      <name>objc2-javascript-core</name>
      <version>0.3.2</version>
      <description>Bindings to the JavaScriptCore framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2a1e6550c4caed348956ce3370c9ffeca70bb1dbed4fa96112e7c6170e074586</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-javascript-core@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-osa-kit@0.3.2">
      <name>objc2-osa-kit</name>
      <version>0.3.2</version>
      <description>Bindings to the OSAKit framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f112d1746737b0da274ef79a23aac283376f335f4095a083a267a082f21db0c0</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-osa-kit@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-quartz-core@0.3.2">
      <name>objc2-quartz-core</name>
      <version>0.3.2</version>
      <description>Bindings to the QuartzCore/CoreAnimation framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">96c1358452b371bf9f104e21ec536d37a650eb10f7ee379fff67d2e08d537f1f</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-quartz-core@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-security@0.3.2">
      <name>objc2-security</name>
      <version>0.3.2</version>
      <description>Bindings to the Security framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">709fe137109bd1e8b5a99390f77a7d8b2961dafc1a1c5db8f2e60329ad6d895a</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-security@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2-web-kit@0.3.2">
      <name>objc2-web-kit</name>
      <version>0.3.2</version>
      <description>Bindings to the WebKit framework</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b2e5aaab980c433cf470df9d7af96a7b46a9d892d521a2cbbb2f8a4c16751e7f</hash>
      </hashes>
      <licenses>
        <expression>Zlib OR Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2-web-kit@0.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2@0.5.2">
      <author>Steven Sheldon, Mads Marquart &lt;mads@marquart.dk&gt;</author>
      <name>objc2</name>
      <version>0.5.2</version>
      <description>Objective-C interface and runtime bindings</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">46a785d4eeff09c14c487497c162e92766fbb3e4059a71840cecc03d9a50b804</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2@0.5.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/objc2/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc2@0.6.3">
      <author>Mads Marquart &lt;mads@marquart.dk&gt;</author>
      <name>objc2</name>
      <version>0.6.3</version>
      <description>Objective-C interface and runtime bindings</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b7c2599ce0ec54857b29ce62166b0ed9b4f6f1a70ccc9a71165b6154caca8c05</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc2@0.6.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/madsmtm/objc2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc@0.2.7">
      <author>Steven Sheldon</author>
      <name>objc</name>
      <version>0.2.7</version>
      <description>Objective-C Runtime bindings and wrapper for Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">915b1b472bc21c53464d6c8461c9d3af805ba1ef837e1cac254428f4a77177b1</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc@0.2.7</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://ssheldon.github.io/rust-objc/objc/</url>
        </reference>
        <reference type="vcs">
          <url>http://github.com/SSheldon/rust-objc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#objc_exception@0.1.2">
      <author>Steven Sheldon</author>
      <name>objc_exception</name>
      <version>0.1.2</version>
      <description>Rust interface for Objective-C's throw and try/catch statements.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ad970fb455818ad6cba4c122ad012fae53ae8b4795f86378bce65e4f6bab2ca4</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/objc_exception@0.1.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>http://ssheldon.github.io/rust-objc/objc_exception/</url>
        </reference>
        <reference type="vcs">
          <url>http://github.com/SSheldon/rust-objc-exception</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#object@0.32.2">
      <name>object</name>
      <version>0.32.2</version>
      <description>A unified interface for reading and writing object file formats.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">a6a622008b6e321afc04970976f62ee297fdbaa6f95318ca343e3eebb9648441</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/object@0.32.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/gimli-rs/object</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#object@0.36.7">
      <name>object</name>
      <version>0.36.7</version>
      <description>A unified interface for reading and writing object file formats.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">62948e14d923ea95ea2c7c86c71013138b66525b86bdc08d2dcc262bdb497b87</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/object@0.36.7</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/gimli-rs/object</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#object@0.37.3">
      <name>object</name>
      <version>0.37.3</version>
      <description>A unified interface for reading and writing object file formats.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ff76201f031d8863c38aa7f905eca4f53abbfa15f609db4277d44cd8938f33fe</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/object@0.37.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/gimli-rs/object</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oid-registry@0.6.1">
      <author>Pierre Chifflier &lt;chifflier@wzdftpd.net&gt;</author>
      <name>oid-registry</name>
      <version>0.6.1</version>
      <description>Object Identifier (OID) database</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9bedf36ffb6ba96c2eb7144ef6270557b52e54b20c0a8e1eb2ff99a6c6959bff</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/oid-registry@0.6.1</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/rusticata/oid-registry</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/rusticata/oid-registry.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#once-cell-regex@0.2.1">
      <author>Francesca Lovebloom &lt;francesca@brainiumstudios.com&gt;</author>
      <name>once-cell-regex</name>
      <version>0.2.1</version>
      <description>This crate just gives you the `regex` macro from the `once_cell` docs!</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b3de7e389a5043420c8f2b95ed03f3f104ad6f4c41f7d7e27298f033abc253e8</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/once-cell-regex@0.2.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/once-cell-regex</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/francesca64/once-cell-regex</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#once_cell@1.21.3">
      <author>Aleksey Kladov &lt;aleksey.kladov@gmail.com&gt;</author>
      <name>once_cell</name>
      <version>1.21.3</version>
      <description>Single assignment cells and lazy values.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">42f5e15c9953c5e4ccceeb2e7382a716482c34515315f7b03532b8b4e8393d2d</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/once_cell@1.21.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/once_cell</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/matklad/once_cell</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#opaque-debug@0.3.1">
      <author>RustCrypto Developers</author>
      <name>opaque-debug</name>
      <version>0.3.1</version>
      <description>Macro for opaque Debug trait implementation</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c08d65885ee38876c4f86fa503fb49d7b507c2b62552df7c70b2fce627e06381</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/opaque-debug@0.3.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/opaque-debug</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/utils</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#open@5.3.2">
      <author>Sebastian Thiel &lt;byronimo@gmail.com&gt;</author>
      <name>open</name>
      <version>5.3.2</version>
      <description>Open a path or URL using the program configured on the system</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e2483562e62ea94312f3576a7aca397306df7990b8d89033e18766744377ef95</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/open@5.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Byron/open-rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#openssl-macros@0.1.1">
      <name>openssl-macros</name>
      <version>0.1.1</version>
      <description>Internal macros used by the openssl crate.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">a948666b637a0f465e8564c73e89d4dde00d72d4d473cc972f390fc3dcee7d9c</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/openssl-macros@0.1.1</purl>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#openssl-sys@0.9.109">
      <author>Alex Crichton &lt;alex@alexcrichton.com&gt;, Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>openssl-sys</name>
      <version>0.9.109</version>
      <description>FFI bindings to OpenSSL</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">90096e2e47630d78b7d1c20952dc621f957103f8bc2c8359ec81290d75238571</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/openssl-sys@0.9.109</purl>
      <externalReferences>
        <reference type="other">
          <url>openssl</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-openssl</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#openssl@0.10.73">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>openssl</name>
      <version>0.10.73</version>
      <description>OpenSSL bindings</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">8505734d46c8ab1e19a1dce3aef597ad87dcb4c37e7188231769bd6bd51cebf8</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/openssl@0.10.73</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-openssl</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#option-ext@0.2.0">
      <author>Simon Ochsenreither &lt;simon@ochsenreither.de&gt;</author>
      <name>option-ext</name>
      <version>0.2.0</version>
      <description>Extends `Option` with additional operations</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">04744f49eae99ab78e0d5c0b603ab218f515ea8cfe5a456d7629ad883a3b6e7d</hash>
      </hashes>
      <licenses>
        <expression>MPL-2.0</expression>
      </licenses>
      <purl>pkg:cargo/option-ext@0.2.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/option-ext/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/soc/option-ext</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/soc/option-ext.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#ordered-float@2.10.1">
      <author>Jonathan Reem &lt;jonathan.reem@gmail.com&gt;, Matt Brubeck &lt;mbrubeck@limpet.net&gt;</author>
      <name>ordered-float</name>
      <version>2.10.1</version>
      <description>Wrappers for total ordering on floats</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">68f19d67e5a2795c94e73e0bb1cc1a7edeb2e28efd39e2e1c9b7a40c1108b11c</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/ordered-float@2.10.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/reem/rust-ordered-float</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#os_info@3.12.0">
      <author>Jan Schulte &lt;hello@unexpected-co.de&gt;, Stanislav Tkach &lt;stanislav.tkach@gmail.com&gt;</author>
      <name>os_info</name>
      <version>3.12.0</version>
      <description>Detect the operating system type and version.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d0e1ac5fde8d43c34139135df8ea9ee9465394b2d8d20f032d38998f64afffc3</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/os_info@3.12.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/os_info</url>
        </reference>
        <reference type="website">
          <url>https://github.com/stanislav-tkach/os_info</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/stanislav-tkach/os_info</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#os_pipe@1.2.2">
      <author>Jack O'Connor</author>
      <name>os_pipe</name>
      <version>1.2.2</version>
      <description>a cross-platform library for opening OS pipes</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">db335f4760b14ead6290116f2427bf33a14d4f0617d49f78a246de10c1831224</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/os_pipe@1.2.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/os_pipe</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oconnor663/os_pipe.rs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#osakit@0.3.1">
      <author>Marat Dulin &lt;mdevils@gmail.com&gt;</author>
      <name>osakit</name>
      <version>0.3.1</version>
      <description>OSAKit macOS Framework adapted for Rust</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">732c71caeaa72c065bb69d7ea08717bd3f4863a4f451402fc9513e29dbd5261b</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/osakit@0.3.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/osakit/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/mdevils/rust-osakit</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/mdevils/rust-osakit</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#outref@0.5.2">
      <name>outref</name>
      <version>0.5.2</version>
      <description>Out reference</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1a80800c0488c3a21695ea981a54918fbb37abf04f4d0720c453632255e2ff0e</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/outref@0.5.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Nugine/outref</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#owo-colors@4.2.3">
      <author>jam1garner &lt;8260240+jam1garner@users.noreply.github.com&gt;</author>
      <name>owo-colors</name>
      <version>4.2.3</version>
      <description>Zero-allocation terminal colors that'll make people go owo</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9c6901729fa79e91a0913333229e9ca5dc725089d1c363b2f4b4760709dc4a52</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/owo-colors@4.2.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/owo-colors</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/owo-colors/owo-colors</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc-miette-derive@1.0.2">
      <author>Boshen, Kat Marchán &lt;kzm@zkat.tech&gt;</author>
      <name>oxc-miette-derive</name>
      <version>1.0.2</version>
      <description>Derive macros for miette. Like `thiserror` for Diagnostics.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e21f680e8c5f1900297d394627d495351b9e37761f7bbf90116bd5eeb6e80967</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/oxc-miette-derive@1.0.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/zkat/miette</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc-miette@1.0.2">
      <author>Boshen, Kat Marchán &lt;kzm@zkat.tech&gt;</author>
      <name>oxc-miette</name>
      <version>1.0.2</version>
      <description>Fancy diagnostic reporting library and protocol for us mere mortals who aren't compiler hackers.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e03e63fd113c068b82d07c9c614b0b146c08a3ac0a4dface3ea1d1a9d14d549e</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/oxc-miette@1.0.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/miette</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/zkat/miette</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_allocator@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_allocator</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">931f734a61f63a0571163b160b764d90d83077c4d2631d15b26fe1b66763dad8</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_allocator@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_ast@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_ast</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b9a771175e84c2324c841fe7ca3ddacb5df8102f043e2fc3e96d0bfee039c13d</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_ast@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_ast_macros@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_ast_macros</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ed71131e79889e226fb6510b90fa1a4a7495c8fdac43a4f505334fb0f1324e3e</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_ast_macros@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_diagnostics@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_diagnostics</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">e37049d46eb02a97e4cc0900672a921666393c642c1ad419a20d483285f5b590</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_diagnostics@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_estree@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_estree</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">7fa45c638ccfd88b5c26147b0a98e1e8dd49542327dda94445b940ef91920d6a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_estree@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_index@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_index</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">ae76739229d0cc5e834e0e3b9e8c4078a86828ff47f5bc71138e4571ce528f83</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_index@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_parser@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_parser</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">0106e10cd67a59d91a75232d4c40f188b8532efea9b9bbed110bce157e7d3b9a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_parser@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_regular_expression@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_regular_expression</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f1bd0d5b1b943173378a5f61d6a4c49edc7e8c9157241e9bbba54594d7449b4c</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_regular_expression@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_span@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_span</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c7b5d7caf8a20611f34c5c9ebdf232b6b42498e5424d02ef1e2dffe31553b49f</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_span@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#oxc_syntax@0.36.0">
      <author>Boshen &lt;boshenc@gmail.com&gt;, Oxc contributors</author>
      <name>oxc_syntax</name>
      <version>0.36.0</version>
      <description>A collection of JavaScript tools written in Rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3135d5ddd0dc8ca535c0ac517a526ace8cac2699bb1345064c9fe046ca761dfa</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/oxc_syntax@0.36.0</purl>
      <externalReferences>
        <reference type="website">
          <url>https://oxc.rs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/oxc-project/oxc</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#p12@0.6.3">
      <author>hjiayz &lt;hjiayz@gmail.com&gt;, Marc-Antoine Perennou &lt;Marc-Antoine@Perennou.com&gt;</author>
      <name>p12</name>
      <version>0.6.3</version>
      <description>pure rust pkcs12 tool</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">d4873306de53fe82e7e484df31e1e947d61514b6ea2ed6cd7b45d63006fd9224</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/p12@0.6.3</purl>
      <externalReferences>
        <reference type="website">
          <url>https://github.com/hjiayz/p12</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/hjiayz/p12</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#p256@0.13.2">
      <author>RustCrypto Developers</author>
      <name>p256</name>
      <version>0.13.2</version>
      <description>Pure Rust implementation of the NIST P-256 (a.k.a. secp256r1, prime256v1) elliptic curve as defined in SP 800-186, with support for ECDH, ECDSA signing/verification, and general purpose curve arithmetic </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c9863ad85fa8f4460f9c48cb909d38a0d689dba1f6f6988a5e3e0d31071bcd4b</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/p256@0.13.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/p256</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/elliptic-curves/tree/master/p256</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#parking_lot@0.12.5">
      <author>Amanieu d'Antras &lt;amanieu@gmail.com&gt;</author>
      <name>parking_lot</name>
      <version>0.12.5</version>
      <description>More compact and efficient implementations of the standard synchronization primitives.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">93857453250e3077bd71ff98b6a65ea6621a19bb0f559a85248955ac12c45a1a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/parking_lot@0.12.5</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Amanieu/parking_lot</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#parking_lot_core@0.9.12">
      <author>Amanieu d'Antras &lt;amanieu@gmail.com&gt;</author>
      <name>parking_lot_core</name>
      <version>0.9.12</version>
      <description>An advanced API for creating custom synchronization primitives.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">2621685985a2ebf1c516881c026032ac7deafcda1a2c9b7850dc81e3dfcb64c1</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/parking_lot_core@0.9.12</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/Amanieu/parking_lot</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#paste@1.0.15">
      <author>David Tolnay &lt;dtolnay@gmail.com&gt;</author>
      <name>paste</name>
      <version>1.0.15</version>
      <description>Macros for all your token pasting needs</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">57c0d7b74b563b49d38dae00a0c37d4d6de9b432382b2892f0574ddcae73fd0a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/paste@1.0.15</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/paste</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/dtolnay/paste</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#path_abs@0.5.1">
      <author>Rett Berg &lt;googberg@gmail.com&gt;</author>
      <name>path_abs</name>
      <version>0.5.1</version>
      <description>Ergonomic paths and files in rust.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">05ef02f6342ac01d8a93b65f96db53fe68a92a15f41144f97fb00a9e669633c3</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/path_abs@0.5.1</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/path_abs</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/vitiral/path_abs</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pathdiff@0.2.3">
      <author>Manish Goregaokar &lt;manishsmail@gmail.com&gt;</author>
      <name>pathdiff</name>
      <version>0.2.3</version>
      <description>Library for diffing paths to obtain relative paths</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">df94ce210e5bc13cb6651479fa48d14f601d9858cfe0467f43ae157023b938d3</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/pathdiff@0.2.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/pathdiff/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/Manishearth/pathdiff</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pbkdf2@0.12.2">
      <author>RustCrypto Developers</author>
      <name>pbkdf2</name>
      <version>0.12.2</version>
      <description>Generic implementation of PBKDF2</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f8ed6a7761f76e3b9f92dfb0a60a6a6477c61024b775147ff0973a02653abaf2</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/pbkdf2@0.12.2</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/pbkdf2</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/password-hashes/tree/master/pbkdf2</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pear@0.2.9">
      <author>Sergio Benitez &lt;sb@sergio.bz&gt;</author>
      <name>pear</name>
      <version>0.2.9</version>
      <description>A pear is a fruit.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">bdeeaa00ce488657faba8ebf44ab9361f9365a97bd39ffb8a60663f57ff4b467</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/pear@0.2.9</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/SergioBenitez/Pear</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pear_codegen@0.2.9">
      <author>Sergio Benitez &lt;sb@sergio.bz&gt;</author>
      <name>pear_codegen</name>
      <version>0.2.9</version>
      <description>A (codegen) pear is a fruit.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">4bab5b985dc082b345f812b7df84e1bef27e7207b39e448439ba8bd69c93f147</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/pear_codegen@0.2.9</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/SergioBenitez/Pear</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pem-rfc7468@0.7.0">
      <author>RustCrypto Developers</author>
      <name>pem-rfc7468</name>
      <version>0.7.0</version>
      <description>PEM Encoding (RFC 7468) for PKIX, PKCS, and CMS Structures, implementing a strict subset of the original Privacy-Enhanced Mail encoding intended specifically for use with cryptographic keys, certificates, and other messages. Provides a no_std-friendly, constant-time implementation suitable for use with cryptographic private keys. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">88b39c9bfcfc231068454382784bb460aae594343fb030d46e9f50a645418412</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/pem-rfc7468@0.7.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/RustCrypto/formats/tree/master/pem-rfc7468</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pem@3.0.5">
      <author>Jonathan Creekmore &lt;jonathan@thecreekmores.org&gt;</author>
      <name>pem</name>
      <version>3.0.5</version>
      <description>Parse and encode PEM-encoded data.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">38af38e8470ac9dee3ce1bae1af9c1671fffc44ddfd8bd1d0a3445bf349a8ef3</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/pem@3.0.5</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/pem/</url>
        </reference>
        <reference type="website">
          <url>https://github.com/jcreekmore/pem-rs.git</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/jcreekmore/pem-rs.git</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#percent-encoding@2.3.2">
      <author>The rust-url developers</author>
      <name>percent-encoding</name>
      <version>2.3.2</version>
      <description>Percent encoding and decoding</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">9b4f627cb1b25917193a259e49bdad08f671f8d9708acfd5fe0a8c1455d87220</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/percent-encoding@2.3.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/servo/rust-url/</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pest@2.8.3">
      <author>Dragoș Tiselice &lt;dragostiselice@gmail.com&gt;</author>
      <name>pest</name>
      <version>2.8.3</version>
      <description>The Elegant Parser</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">989e7521a040efde50c3ab6bbadafbe15ab6dc042686926be59ac35d74607df4</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/pest@2.8.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/pest</url>
        </reference>
        <reference type="website">
          <url>https://pest.rs/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/pest-parser/pest</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pest_derive@2.8.3">
      <author>Dragoș Tiselice &lt;dragostiselice@gmail.com&gt;</author>
      <name>pest_derive</name>
      <version>2.8.3</version>
      <description>pest's derive macro</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">187da9a3030dbafabbbfb20cb323b976dc7b7ce91fcd84f2f74d6e31d378e2de</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/pest_derive@2.8.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/pest</url>
        </reference>
        <reference type="website">
          <url>https://pest.rs/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/pest-parser/pest</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pest_generator@2.8.3">
      <author>Dragoș Tiselice &lt;dragostiselice@gmail.com&gt;</author>
      <name>pest_generator</name>
      <version>2.8.3</version>
      <description>pest code generator</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">49b401d98f5757ebe97a26085998d6c0eecec4995cad6ab7fc30ffdf4b052843</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/pest_generator@2.8.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/pest</url>
        </reference>
        <reference type="website">
          <url>https://pest.rs/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/pest-parser/pest</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pest_meta@2.8.3">
      <author>Dragoș Tiselice &lt;dragostiselice@gmail.com&gt;</author>
      <name>pest_meta</name>
      <version>2.8.3</version>
      <description>pest meta language parser and validator</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">72f27a2cfee9f9039c4d86faa5af122a0ac3851441a34865b8a043b46be0065a</hash>
      </hashes>
      <licenses>
        <expression>MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:cargo/pest_meta@2.8.3</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/pest</url>
        </reference>
        <reference type="website">
          <url>https://pest.rs/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/pest-parser/pest</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf@0.10.1">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf</name>
      <version>0.10.1</version>
      <description>Runtime support for perfect hash function data structures</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">fabbf1ead8a5bcbc20f5f8b939ee3f5b0f6f281b6ad3468b84656b658b455259</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf@0.10.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf@0.11.3">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf</name>
      <version>0.11.3</version>
      <description>Runtime support for perfect hash function data structures</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">1fd6780a80ae0c52cc120a26a1a42c1ae51b247a253e4e06113d23d2c2edd078</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf@0.11.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-phf/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf@0.8.0">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf</name>
      <version>0.8.0</version>
      <description>Runtime support for perfect hash function data structures</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3dfb61232e34fcb633f43d12c58f83c1df82962dcdfa565a4e866ffc17dafe12</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf@0.8.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_codegen@0.11.3">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_codegen</name>
      <version>0.11.3</version>
      <description>Codegen library for PHF types</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">aef8048c789fa5e851558d709946d6d79a8ff88c0440c587967f8e94bfb1216a</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_codegen@0.11.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-phf/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_codegen@0.8.0">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_codegen</name>
      <version>0.8.0</version>
      <description>Codegen library for PHF types</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">cbffee61585b0411840d3ece935cce9cb6321f01c45477d30066498cd5e1a815</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_codegen@0.8.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_generator@0.10.0">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_generator</name>
      <version>0.10.0</version>
      <description>PHF generation logic</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5d5285893bb5eb82e6aaf5d59ee909a06a16737a8970984dd7746ba9283498d6</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_generator@0.10.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_generator@0.11.3">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_generator</name>
      <version>0.11.3</version>
      <description>PHF generation logic</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3c80231409c20246a13fddb31776fb942c38553c51e871f8cbd687a4cfb5843d</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_generator@0.11.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-phf/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_generator@0.8.0">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_generator</name>
      <version>0.8.0</version>
      <description>PHF generation logic</description>
      <scope>excluded</scope>
      <hashes>
        <hash alg="SHA-256">17367f0cc86f2d25802b2c26ee58a7b23faeccf78a396094c13dced0d0182526</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_generator@0.8.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_macros@0.10.0">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_macros</name>
      <version>0.10.0</version>
      <description>Macros to generate types in the phf crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">58fdf3184dd560f160dd73922bea2d5cd6e8f064bf4b13110abd81b03697b4e0</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_macros@0.10.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_macros@0.11.3">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_macros</name>
      <version>0.11.3</version>
      <description>Macros to generate types in the phf crate</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">f84ac04429c13a7ff43785d75ad27569f2951ce0ffd30a3321230db2fc727216</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_macros@0.11.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-phf/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_shared@0.10.0">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_shared</name>
      <version>0.10.0</version>
      <description>Support code shared by PHF libraries</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">b6796ad771acdc0123d2a88dc428b5e38ef24456743ddb1744ed628f9815c096</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_shared@0.10.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_shared@0.11.3">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_shared</name>
      <version>0.11.3</version>
      <description>Support code shared by PHF libraries</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">67eabc2ef2a60eb7faa00097bd1ffdb5bd28e62bf39990626a582201b7a754e5</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_shared@0.11.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/rust-phf/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#phf_shared@0.8.0">
      <author>Steven Fackler &lt;sfackler@gmail.com&gt;</author>
      <name>phf_shared</name>
      <version>0.8.0</version>
      <description>Support code shared by PHF libraries</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">c00cf8b9eafe68dde5e9eaa2cef8ee84a9336a47d566ec55ca16589633b65af7</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/phf_shared@0.8.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/sfackler/rust-phf</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pico-args@0.5.0">
      <author>Yevhenii Reizner &lt;razrfalcon@gmail.com&gt;</author>
      <name>pico-args</name>
      <version>0.5.0</version>
      <description>An ultra simple CLI arguments parser.</description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">5be167a7af36ee22fe3115051bc51f6e6c7054c9348e28deb4f49bd6f705a315</hash>
      </hashes>
      <licenses>
        <expression>MIT</expression>
      </licenses>
      <purl>pkg:cargo/pico-args@0.5.0</purl>
      <externalReferences>
        <reference type="documentation">
          <url>https://docs.rs/pico-args/</url>
        </reference>
        <reference type="vcs">
          <url>https://github.com/RazrFalcon/pico-args</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pin-project-internal@1.1.10">
      <name>pin-project-internal</name>
      <version>1.1.10</version>
      <description>Implementation detail of the `pin-project` crate. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">6e918e4ff8c4549eb882f14b3a4bc8c8bc93de829416eacf579f1207a8fbf861</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/pin-project-internal@1.1.10</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/taiki-e/pin-project</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pin-project-lite@0.2.16">
      <name>pin-project-lite</name>
      <version>0.2.16</version>
      <description>A lightweight version of pin-project written with declarative macros. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">3b3cff922bd51709b605d9ead9aa71031d81447142d828eb4a6eba76fe619f9b</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/pin-project-lite@0.2.16</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/taiki-e/pin-project-lite</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pin-project@1.1.10">
      <name>pin-project</name>
      <version>1.1.10</version>
      <description>A crate for safe and ergonomic pin-projection. </description>
      <scope>required</scope>
      <hashes>
        <hash alg="SHA-256">677f1add503faace112b9f1373e43e9e054bfdd22ff1a63c1bc485eaec6a6a8a</hash>
      </hashes>
      <licenses>
        <expression>Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:cargo/pin-project@1.1.10</purl>
      <externalReferences>
        <reference type="vcs">
          <url>https://github.com/taiki-e/pin-project</url>
        </reference>
      </externalReferences>
    </component>
    <component type="library" bom-ref="registry+https://github.com/rust-lang/crates.io-index#pin-utils@0.1.0">
      <author>Josef Brandl &lt;mail@josefbrandl.de&gt;</author>
      <name>pin-utils</name>
      <version>0.1.0</version>
      <description>Utilities for pinning </description>

... (truncated 11940 lines) ...
```

**Note**: Source truncated for display. Full file has 21,940 lines.

---

## High-Level Overview

This is a **text** file named `open-data-platform-SBOM-cargo.cdx.xml`.

This file contains 21940 lines of code/text.


---

## Detailed Analysis

This file contains code or text data. See the original source above for full details.


---

## Related Files

The following files may be related based on imports and references:

*No direct imports detected.*


---

## Performance & Security Notes

No obvious security concerns detected in static analysis.


---

**Generated**: 2025-11-19T02:16:45.148587Z
**Generator**: World's Best Repo Book Generator v1.0
