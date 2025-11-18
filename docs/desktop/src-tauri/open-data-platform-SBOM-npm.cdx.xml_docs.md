# Documentation: desktop/src-tauri/open-data-platform-SBOM-npm.cdx.xml

## File Metadata
- **Path**: `desktop/src-tauri/open-data-platform-SBOM-npm.cdx.xml`
- **Size**: 3,186,539 characters, 35,787 lines
- **Words**: 70,095
- **Extension**: .xml
- **Classification**: Text file

## Original Source

```xml
<?xml version="1.0" encoding="UTF-8"?>
<bom xmlns="http://cyclonedx.org/schema/bom/1.6" version="1" serialNumber="urn:uuid:e7cf01d3-551a-4357-9dff-8669441f0f96">
  <metadata>
    <timestamp>2025-10-22T15:34:01.615Z</timestamp>
    <tools>
      <components>
        <component type="application">
          <name>npm</name>
          <version>11.6.0</version>
        </component>
        <component type="application">
          <author>Jan Kowalleck</author>
          <group>@cyclonedx</group>
          <name>cyclonedx-npm</name>
          <version>4.0.1</version>
          <description>Create CycloneDX Software Bill of Materials (SBOM) from NPM projects.</description>
          <licenses>
            <license>
              <id>Apache-2.0</id>
            </license>
          </licenses>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/CycloneDX/cyclonedx-node-npm.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/CycloneDX/cyclonedx-node-npm#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/CycloneDX/cyclonedx-node-npm/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
          </externalReferences>
        </component>
        <component type="library">
          <author>Jan Kowalleck</author>
          <group>@cyclonedx</group>
          <name>cyclonedx-library</name>
          <version>8.6.0</version>
          <description>Core functionality of CycloneDX for JavaScript (Node.js or WebBrowser).</description>
          <licenses>
            <license>
              <id>Apache-2.0</id>
            </license>
          </licenses>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/CycloneDX/cyclonedx-javascript-library.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/CycloneDX/cyclonedx-javascript-library#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/CycloneDX/cyclonedx-javascript-library/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
          </externalReferences>
        </component>
      </components>
    </tools>
    <component type="application" bom-ref="openbb-platform@1.0.0">
      <name>openbb-platform</name>
      <version>1.0.0</version>
      <licenses>
        <license acknowledgement="declared">
          <id>AGPL-3.0</id>
        </license>
      </licenses>
      <purl>pkg:npm/openbb-platform@1.0.0</purl>
      <properties>
        <property name="cdx:npm:package:private">true</property>
        <property name="cdx:npm:package:path"/>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyNSBPcGVuQkIKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
  </metadata>
  <components>
    <component type="library" bom-ref="openbb-platform@1.0.0|@eslint/js@9.37.0">
      <group>@eslint</group>
      <name>js</name>
      <version>9.37.0</version>
      <description>ESLint JavaScript language implementation</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40eslint/js@9.37.0#packages/js</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/eslint/eslint.git#packages/js</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://eslint.org</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/eslint/eslint/issues/</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@eslint/js/-/js-9.37.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">8da4be349fa1c629acc011baa63357d2e109664ad3d33c29562dc1037bd7db66851a32639a04934a63e964244a9a804be5563f33aa74c6c489c7bae4eeccb982</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@eslint/js</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">Q29weXJpZ2h0IE9wZW5KUyBGb3VuZGF0aW9uIGFuZCBvdGhlciBjb250cmlidXRvcnMsIDx3d3cub3BlbmpzZi5vcmc+CgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCmFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KVEhFIFNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@heroicons/react@2.2.0">
      <group>@heroicons</group>
      <name>react</name>
      <version>2.2.0</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40heroicons/react@2.2.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tailwindlabs/heroicons.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tailwindlabs/heroicons#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tailwindlabs/heroicons/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@heroicons/react/-/react-2.2.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">2cc71ea6f45a4bd2d81c91ac174cf39a02825229bf5f737f0d029ce237a901727b97c4312753e6c49ceaa65176677144e0fa810081b224043fc3807976ca9bb5</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@heroicons/react</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgVGFpbHdpbmQgTGFicywgSW5jLgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@hookform/resolvers@3.10.0">
      <author>bluebill1049</author>
      <group>@hookform</group>
      <name>resolvers</name>
      <version>3.10.0</version>
      <description>React Hook Form validation resolvers: Yup, Joi, Superstruct, Zod, Vest, Class Validator, io-ts, Nope, computed-types, TypeBox, arktype, Typanion, Effect-TS and VineJS</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40hookform/resolvers@3.10.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/react-hook-form/resolvers.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://react-hook-form.com</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/react-hook-form/resolvers/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@hookform/resolvers/-/resolvers-3.10.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">efd0effb798317b8bed9a8e3ed2932a52287865d5c6e59f53866afaabb05ee9ea66d4bf5d71a6aa5a70fb060c24d1bc24a310421ecf679fd4dbde4952f76f402</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@hookform/resolvers</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxOS1wcmVzZW50IEJlaWVyKEJpbGwpIEx1bwoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@openbb/ui-pro@0.6.10">
      <group>@openbb</group>
      <name>ui-pro</name>
      <version>0.6.10</version>
      <purl>pkg:npm/%40openbb/ui-pro@0.6.10</purl>
      <externalReferences>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@openbb/ui-pro/-/ui-pro-0.6.10.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">f5a85e8fef0e758759adb1bb271baa17dee2861b36c4d111b1d0610db0127c0b85bfa2e867b0d8089c52d4fe0c47de910f807000aa8160c128314f2d25d6fee2</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@openbb/ui-pro</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tanstack/react-router@1.132.47">
      <author>Tanner Linsley</author>
      <group>@tanstack</group>
      <name>react-router</name>
      <version>1.132.47</version>
      <description>Modern and scalable routing for React applications</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40tanstack/react-router@1.132.47#packages/react-router</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/TanStack/router.git#packages/react-router</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://tanstack.com/router</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/TanStack/router/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tanstack/react-router/-/react-router-1.132.47.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">9a308dd6e7952c704e2b582a2de69c0ab50f05989eb4c29392bef16650b7d9d0869f87bef37ccc4a54534b64eb125efec041fe6ea8e7a32c7c00b6134a24350a</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tanstack/react-router</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMS1wcmVzZW50IFRhbm5lciBMaW5zbGV5CgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tanstack/router-core@1.132.47">
      <author>Tanner Linsley</author>
      <group>@tanstack</group>
      <name>router-core</name>
      <version>1.132.47</version>
      <description>Modern and scalable routing for React applications</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40tanstack/router-core@1.132.47#packages/router-core</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/TanStack/router.git#packages/router-core</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://tanstack.com/router</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/TanStack/router/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tanstack/router-core/-/router-core-1.132.47.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">f182851e61ba554a97696009cc4aa3c96eb0df5740452d9449dda6b48e5979972286a31bb242b6f0de22a2d057367fac48a2673d18dcec0e234e79c47fc327f1</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tanstack/router-core</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMS1wcmVzZW50IFRhbm5lciBMaW5zbGV5CgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tanstack/router-devtools@1.132.47">
      <author>Tanner Linsley</author>
      <group>@tanstack</group>
      <name>router-devtools</name>
      <version>1.132.47</version>
      <description>Modern and scalable routing for React applications</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40tanstack/router-devtools@1.132.47#packages/router-devtools</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/TanStack/router.git#packages/router-devtools</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://tanstack.com/router</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/TanStack/router/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tanstack/router-devtools/-/router-devtools-1.132.47.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">08b9544fa7dc1ba13bb621bf386e61ef6302fe8c010d29279636cd2bbb05af7b5ab890afe81d59a24e2365d11bf157b13397406b4031dabc9234b1eba4906a8b</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tanstack/router-devtools</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMS1wcmVzZW50IFRhbm5lciBMaW5zbGV5CgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tanstack/router-vite-plugin@1.132.47">
      <author>Tanner Linsley</author>
      <group>@tanstack</group>
      <name>router-vite-plugin</name>
      <version>1.132.47</version>
      <description>Modern and scalable routing for React applications</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40tanstack/router-vite-plugin@1.132.47#packages/router-vite-plugin</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/TanStack/router.git#packages/router-vite-plugin</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://tanstack.com/router</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/TanStack/router/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tanstack/router-vite-plugin/-/router-vite-plugin-1.132.47.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">4c7a7bfe53eb07002c7d9ba2d73f6b436207914741c448155be75a80a3486214e76054010db4a00fa52851f2ec7239e230c133831868d54dc1fc82b6f6f3c20a</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@tanstack/router-vite-plugin</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMS1wcmVzZW50IFRhbm5lciBMaW5zbGV5CgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/api@2.8.0">
      <group>@tauri-apps</group>
      <name>api</name>
      <version>2.8.0</version>
      <description>Tauri API definitions</description>
      <licenses>
        <expression acknowledgement="declared">Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/api@2.8.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/tauri.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/tauri#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/tauri/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/api/-/api-2.8.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">81aef37616d2d865ce313219453d26623289b51f5f8afb17ceccaae54def8c32f4b3a0d33306119b4507363cd3639761e3e2d20baf129bfed61228a66d035897</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/api</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE_MIT</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxNyAtIFByZXNlbnQgVGF1cmkgQXBwcyBDb250cmlidXRvcnMKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/cli@2.8.4">
      <group>@tauri-apps</group>
      <name>cli</name>
      <version>2.8.4</version>
      <description>Command line interface for building Tauri apps</description>
      <licenses>
        <expression acknowledgement="declared">Apache-2.0 OR MIT</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/cli@2.8.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/tauri.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/tauri#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/tauri/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/cli/-/cli-2.8.4.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">7a3519073b9045c8c557ebff81d8ff0dc6f25ffe93e2e9d9423312059c0bccffc2ca612329c736f8573cc533914e179b1c352faa85cc76c099b7cafe872375e6</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/cli</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE_MIT</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxNyAtIFByZXNlbnQgVGF1cmkgQXBwcyBDb250cmlidXRvcnMKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-app@2.0.0-alpha.1">
      <group>@tauri-apps</group>
      <name>plugin-app</name>
      <version>2.0.0-alpha.1</version>
      <licenses>
        <license acknowledgement="declared">
          <name>MIT or APACHE-2.0</name>
        </license>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-app@2.0.0-alpha.1</purl>
      <externalReferences>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-app/-/plugin-app-2.0.0-alpha.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">0ca95b1b8ca6a1af310ca74adfa69d3e5658798f3070341f8bf5c91b8ab184ae980b818baccd6c1b979082354a85e0c8eb00d00b90a2523867bdd75754550f4e</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-app</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-app@2.0.0-alpha.1|@tauri-apps/api@2.0.0-alpha.6">
          <group>@tauri-apps</group>
          <name>api</name>
          <version>2.0.0-alpha.6</version>
          <description>Tauri API definitions</description>
          <licenses>
            <expression acknowledgement="declared">Apache-2.0 OR MIT</expression>
          </licenses>
          <purl>pkg:npm/%40tauri-apps/api@2.0.0-alpha.6</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/tauri-apps/tauri.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/tauri-apps/tauri#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/tauri-apps/tauri/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/@tauri-apps/api/-/api-2.0.0-alpha.6.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">64c39cddebbd6a6c2f902e8cebd877856b78fc4b056805e6b648b0e317762cde7dfe54dbe1942255fab640a95172ed6b8f79ff4dcafb537d19a29bc7c1704622</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-app/node_modules/@tauri-apps/api</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE_MIT</name>
                <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxNyAtIFByZXNlbnQgVGF1cmkgQXBwcyBDb250cmlidXRvcnMKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-dialog@2.4.0">
      <group>@tauri-apps</group>
      <name>plugin-dialog</name>
      <version>2.4.0</version>
      <licenses>
        <expression acknowledgement="declared">MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-dialog@2.4.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/plugins-workspace.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/plugins-workspace#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/plugins-workspace/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-dialog/-/plugin-dialog-2.4.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">3af5e4ac405f5b0b5df2dcd50845c8bd17cd117f3baacda3bfa4aa9953e21dc263061485fc652f8ea50d20398a0726f937c9ef0ea55433bfa0d6c5f0742fd2f7</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-dialog</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-fs@2.4.2">
      <group>@tauri-apps</group>
      <name>plugin-fs</name>
      <version>2.4.2</version>
      <description>Access the file system.</description>
      <licenses>
        <expression acknowledgement="declared">MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-fs@2.4.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/plugins-workspace.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/plugins-workspace#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/plugins-workspace/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-fs/-/plugin-fs-2.4.2.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">60686662e4e05c6b22e808e857ee6687636f89c81605f5491c785eb9c93aa070fe1c2f5b5563da1ef08fd3f030e291c37a3c2bbd3f21137fb36406967fe86b8a</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-fs</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-http@2.5.2">
      <group>@tauri-apps</group>
      <name>plugin-http</name>
      <version>2.5.2</version>
      <licenses>
        <expression acknowledgement="declared">MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-http@2.5.2</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/plugins-workspace.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/plugins-workspace#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/plugins-workspace/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-http/-/plugin-http-2.5.2.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">c7599028748b0e4e264b64bddfc3937b293c2fb4322e90ab2990997239258c6b2f4ef44ca230af23d49e27591ac5ceedf314a29640bb59d21df31111f532062e</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-http</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-log@2.7.0">
      <group>@tauri-apps</group>
      <name>plugin-log</name>
      <version>2.7.0</version>
      <description>Configurable logging for your Tauri app.</description>
      <licenses>
        <expression acknowledgement="declared">MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-log@2.7.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/plugins-workspace.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/plugins-workspace#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/plugins-workspace/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-log/-/plugin-log-2.7.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">f355d0d9ff77c78be6201e4e6345e5600c72eb47077582ecd0a8bc429dfcb4d013462b818adf8eae1ddfae9637a9f6109ea12f615c91b9bed84495a5996d9144</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-log</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-opener@2.5.0">
      <group>@tauri-apps</group>
      <name>plugin-opener</name>
      <version>2.5.0</version>
      <description>Open files and URLs using their default application.</description>
      <licenses>
        <expression acknowledgement="declared">MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-opener@2.5.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/plugins-workspace.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/plugins-workspace#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/plugins-workspace/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-opener/-/plugin-opener-2.5.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">0742d284e61a7b80998cdf257a23436e77e34ab4f0a196a4a8a696a5fa07ea75e2270b7a4608fa4675487df1b70e82622ac7df4613248e6055f557a29526f84c</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-opener</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-process@2.3.0">
      <group>@tauri-apps</group>
      <name>plugin-process</name>
      <version>2.3.0</version>
      <licenses>
        <expression acknowledgement="declared">MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-process@2.3.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/plugins-workspace.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/plugins-workspace#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/plugins-workspace/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-process/-/plugin-process-2.3.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">d03363eaefbd72c383895e2c792c7145b9cba5e1987688e571cb42b8b3828291fd5f7f9c915648123e87eed450ef3a96afb9124c45a7af1b407416f415bb6b99</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-process</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-shell@2.3.1">
      <group>@tauri-apps</group>
      <name>plugin-shell</name>
      <version>2.3.1</version>
      <licenses>
        <expression acknowledgement="declared">MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-shell@2.3.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/plugins-workspace.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/plugins-workspace#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/plugins-workspace/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-shell/-/plugin-shell-2.3.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">8e3b365860ceffdcf6a63365c9d63f179c9884db2c72ff7d2b9942994e6e2a3b15bd0ddd4650e186d558a1ae0e2c39a4b4bb50be0bdb42308589b325ead8067f</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-shell</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-updater@2.9.0">
      <group>@tauri-apps</group>
      <name>plugin-updater</name>
      <version>2.9.0</version>
      <licenses>
        <expression acknowledgement="declared">MIT OR Apache-2.0</expression>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-updater@2.9.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tauri-apps/plugins-workspace.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/tauri-apps/plugins-workspace#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tauri-apps/plugins-workspace/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-updater/-/plugin-updater-2.9.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">8fefac818f17a5e0efcc8993af3580d3c3aaa86aa090dcb17332c3ec58cd249c7fb97c4c645cf99c371f932a08feb0a362e8f6d74d53722febfc71663a6a310a</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-updater</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-window@2.0.0-alpha.1">
      <group>@tauri-apps</group>
      <name>plugin-window</name>
      <version>2.0.0-alpha.1</version>
      <licenses>
        <license acknowledgement="declared">
          <name>MIT or APACHE-2.0</name>
        </license>
      </licenses>
      <purl>pkg:npm/%40tauri-apps/plugin-window@2.0.0-alpha.1</purl>
      <externalReferences>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tauri-apps/plugin-window/-/plugin-window-2.0.0-alpha.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">74538081a97fdd3c73dd243e2cd42ad002b510f0be69c75a165c0f541ffa29751962668595e225ce0c4356824243eff13a1c6f62b7506852de7e1d08fca95d6e</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-window</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|@tauri-apps/plugin-window@2.0.0-alpha.1|@tauri-apps/api@2.0.0-alpha.6">
          <group>@tauri-apps</group>
          <name>api</name>
          <version>2.0.0-alpha.6</version>
          <description>Tauri API definitions</description>
          <licenses>
            <expression acknowledgement="declared">Apache-2.0 OR MIT</expression>
          </licenses>
          <purl>pkg:npm/%40tauri-apps/api@2.0.0-alpha.6</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/tauri-apps/tauri.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/tauri-apps/tauri#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/tauri-apps/tauri/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/@tauri-apps/api/-/api-2.0.0-alpha.6.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">64c39cddebbd6a6c2f902e8cebd877856b78fc4b056805e6b648b0e317762cde7dfe54dbe1942255fab640a95172ed6b8f79ff4dcafb537d19a29bc7c1704622</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/@tauri-apps/plugin-window/node_modules/@tauri-apps/api</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE_MIT</name>
                <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxNyAtIFByZXNlbnQgVGF1cmkgQXBwcyBDb250cmlidXRvcnMKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@testing-library/jest-dom@6.9.1">
      <author>Ernesto Garcia</author>
      <group>@testing-library</group>
      <name>jest-dom</name>
      <version>6.9.1</version>
      <description>Custom jest matchers to test the state of the DOM</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40testing-library/jest-dom@6.9.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/testing-library/jest-dom.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/testing-library/jest-dom#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/testing-library/jest-dom/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@testing-library/jest-dom/-/jest-dom-6.9.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">cc870e35afa156d55249ea7d513de3679ae2ce8d81b318320d853b5850f978808113b9e8dfcf351c679bfd09067ec26ce894e4635690853eeb20f0bb7bed279c</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@testing-library/jest-dom</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|@testing-library/jest-dom@6.9.1|dom-accessibility-api@0.6.3">
          <name>dom-accessibility-api</name>
          <version>0.6.3</version>
          <description>Implements https://w3c.github.io/accname/</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/dom-accessibility-api@0.6.3</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/eps1lon/dom-accessibility-api.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/eps1lon/dom-accessibility-api#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/eps1lon/dom-accessibility-api/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/dom-accessibility-api/-/dom-accessibility-api-0.6.3.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">ed982881e4e78ee1dba3e72dd741bd15fa749a27f5ee2762d08c9635503fc1cc1c9bb34f383fd610754fde7ee7dcc857ab1a08626f1de8cb99a21616219e13df</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/@testing-library/jest-dom/node_modules/dom-accessibility-api</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE.md</name>
                <text content-type="text/markdown" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMCBTZWJhc3RpYW4gU2lsYmVybWFubgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCkNvcHlyaWdodCAoYykgMjAxNyBLZW50IEMuIERvZGRzCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@testing-library/react@16.3.0">
      <author>Kent C. Dodds</author>
      <group>@testing-library</group>
      <name>react</name>
      <version>16.3.0</version>
      <description>Simple and complete React DOM testing utilities that encourage good testing practices.</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40testing-library/react@16.3.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/testing-library/react-testing-library.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/testing-library/react-testing-library#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/testing-library/react-testing-library/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@testing-library/react/-/react-16.3.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">9054b2c62103c2fd562e5d9f82cabaa4f05bc396962abb18dbf9e88b521dd132b450f6ab485eb6a054051875c8c9a1b8a69dad12e6ff6657a5f9f8e36482c3b3</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@testing-library/react</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCkNvcHlyaWdodCAoYykgMjAxNy1QcmVzZW50IEtlbnQgQy4gRG9kZHMKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@types/node@20.19.19">
      <group>@types</group>
      <name>node</name>
      <version>20.19.19</version>
      <description>TypeScript definitions for node</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40types/node@20.19.19#types/node</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/DefinitelyTyped/DefinitelyTyped.git#types/node</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/node</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/DefinitelyTyped/DefinitelyTyped/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@types/node/-/node-20.19.19.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">a5bd54aa3e5624fef0adc6cb53b46ee10b40d3ede4017ae4bad1a20f6eb050acd232034d68f0114d40d09849545e9eb8921ddc59da2edd0d02eeac30c6a4859a</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@types/node</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">ICAgIE1JVCBMaWNlbnNlCgogICAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uCgogICAgUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQogICAgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKICAgIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKICAgIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKICAgIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwogICAgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKCiAgICBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKICAgIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgogICAgVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKICAgIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAogICAgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCiAgICBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCiAgICBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAogICAgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKICAgIFNPRlRXQVJFCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@types/react-dom@18.3.7">
      <group>@types</group>
      <name>react-dom</name>
      <version>18.3.7</version>
      <description>TypeScript definitions for react-dom</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40types/react-dom@18.3.7#types/react-dom</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/DefinitelyTyped/DefinitelyTyped.git#types/react-dom</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react-dom</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/DefinitelyTyped/DefinitelyTyped/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@types/react-dom/-/react-dom-18.3.7.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">3047b751ea043585455f3a17116b2f72983a66f96b14d94e43b10eb2f848dc27c05f0ccf7cef10c2ec5de349dea6c60aab2c954274dd11fbfaf2af75c8b70aad</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@types/react-dom</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">ICAgIE1JVCBMaWNlbnNlCgogICAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uCgogICAgUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQogICAgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKICAgIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKICAgIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKICAgIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwogICAgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKCiAgICBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKICAgIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgogICAgVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKICAgIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAogICAgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCiAgICBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCiAgICBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAogICAgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKICAgIFNPRlRXQVJFCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@types/react@18.3.26">
      <group>@types</group>
      <name>react</name>
      <version>18.3.26</version>
      <description>TypeScript definitions for react</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40types/react@18.3.26#types/react</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/DefinitelyTyped/DefinitelyTyped.git#types/react</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/react</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/DefinitelyTyped/DefinitelyTyped/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@types/react/-/react-18.3.26.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">44503f6d446470acf1fd7f68ba63c6f55a770f725482eb3f7746faeca074b794bfada722ca68a590e6baea8961efc31423dd902db1097af3bbaefa94fe48f028</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@types/react</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">ICAgIE1JVCBMaWNlbnNlCgogICAgQ29weXJpZ2h0IChjKSBNaWNyb3NvZnQgQ29ycG9yYXRpb24uCgogICAgUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQogICAgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKICAgIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKICAgIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKICAgIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwogICAgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKCiAgICBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKICAgIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgogICAgVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKICAgIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAogICAgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCiAgICBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCiAgICBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAogICAgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKICAgIFNPRlRXQVJFCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@typescript-eslint/eslint-plugin@8.46.0">
      <group>@typescript-eslint</group>
      <name>eslint-plugin</name>
      <version>8.46.0</version>
      <description>TypeScript plugin for ESLint</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40typescript-eslint/eslint-plugin@8.46.0#packages/eslint-plugin</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/typescript-eslint/typescript-eslint.git#packages/eslint-plugin</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://typescript-eslint.io/packages/eslint-plugin</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/typescript-eslint/typescript-eslint/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@typescript-eslint/eslint-plugin/-/eslint-plugin-8.46.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">840f20c41ab8ba4a275573f2d0e2a189a521ffaf03d04f3c1929ad0b588012719a89eb838b7f0b852ee37421d12e2e84ac904d0c60b3be1e449f374fc147340c</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@typescript-eslint/eslint-plugin</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxOSB0eXBlc2NyaXB0LWVzbGludCBhbmQgb3RoZXIgY29udHJpYnV0b3JzCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@typescript-eslint/parser@8.46.0">
      <group>@typescript-eslint</group>
      <name>parser</name>
      <version>8.46.0</version>
      <description>An ESLint custom parser which leverages TypeScript ESTree</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40typescript-eslint/parser@8.46.0#packages/parser</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/typescript-eslint/typescript-eslint.git#packages/parser</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://typescript-eslint.io/packages/parser</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/typescript-eslint/typescript-eslint/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@typescript-eslint/parser/-/parser-8.46.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">9f51fa21c0e19a65041bb4cd552b291a68871eeb6dee254ab59c11a690fb7b4e3085ae4cae4575877a6d8bdc502dc08cb7a616b27729a13d07323907d4537059</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@typescript-eslint/parser</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxOSB0eXBlc2NyaXB0LWVzbGludCBhbmQgb3RoZXIgY29udHJpYnV0b3JzCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@vitejs/plugin-react@4.7.0">
      <author>Evan You</author>
      <group>@vitejs</group>
      <name>plugin-react</name>
      <version>4.7.0</version>
      <description>The default Vite plugin for React projects</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40vitejs/plugin-react@4.7.0#packages/plugin-react</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/vitejs/vite-plugin-react.git#packages/plugin-react</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/vitejs/vite-plugin-react/tree/main/packages/plugin-react#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/vitejs/vite-plugin-react/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@vitejs/plugin-react/-/plugin-react-4.7.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">814bbd8707d6bef1030419a0b40a30402a23c19989e6670b9f76ae7de0ac8ad8a3b37f9fd8db2b3ed94058847a38f8aa96397de8654251b2ded07caa22955aa0</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/@vitejs/plugin-react</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxOS1wcmVzZW50LCBZdXhpIChFdmFuKSBZb3UgYW5kIFZpdGUgY29udHJpYnV0b3JzCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|autoprefixer@10.4.21">
      <author>Andrey Sitnik</author>
      <name>autoprefixer</name>
      <version>10.4.21</version>
      <description>Parse CSS and add vendor prefixes to CSS rules using values from the Can I Use website</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/autoprefixer@10.4.21</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/postcss/autoprefixer.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/postcss/autoprefixer#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/postcss/autoprefixer/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/autoprefixer/-/autoprefixer-10.4.21.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">3be03a2d65792c31d2243dcb8c7628362e152ec8ff5a18bb93acc6d76c5361a538710f28c5019c917357f1c4472b9c8e67fa695477b46415c6cd257d8d77556d</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/autoprefixer</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCgpDb3B5cmlnaHQgMjAxMyBBbmRyZXkgU2l0bmlrIDxhbmRyZXlAc2l0bmlrLnJ1PgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZgp0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbgp0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvCnVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mCnRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywKc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTCkZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUgpDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIKSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4KQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|clsx@2.1.1">
      <author>Luke Edwards</author>
      <name>clsx</name>
      <version>2.1.1</version>
      <description>A tiny (239B) utility for constructing className strings conditionally.</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/clsx@2.1.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/lukeed/clsx.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/lukeed/clsx#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/lukeed/clsx/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/clsx/-/clsx-2.1.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">7989b441606d52b0566561b4777f3a386030d7a67df793e2395a3607b6e35926c779d1a5e5ed1959aabae6438681448d7ac1080e407d2126d383f24af5d84264</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/clsx</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: license</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgTHVrZSBFZHdhcmRzIDxsdWtlLmVkd2FyZHMwNUBnbWFpbC5jb20+IChsdWtlZWQuY29tKQoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|csstype@3.1.3">
      <author>Fredrik Nicol</author>
      <name>csstype</name>
      <version>3.1.3</version>
      <description>Strict TypeScript and Flow types for style based on MDN data</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/csstype@3.1.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/frenic/csstype.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/frenic/csstype#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/frenic/csstype/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/csstype/-/csstype-3.1.3.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">335b9090c97cad02bfb330f42cd86dab120f2e98a61a6f2c381c14ee52e70a949b4f2637c9e53555cee5e0a4f9cd3e2cff23b11c7e4eeed22eb8b3829cb00347</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/csstype</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">Q29weXJpZ2h0IChjKSAyMDE3LTIwMTggRnJlZHJpayBOaWNvbAoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|date-fns@4.1.0">
      <name>date-fns</name>
      <version>4.1.0</version>
      <description>Modern JavaScript date utility library</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/date-fns@4.1.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/date-fns/date-fns.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/date-fns/date-fns#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/date-fns/date-fns/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/date-fns/-/date-fns-4.1.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">524ab4a306d05f16bf537106b6c755064475c3b28e43980806a747da192f927cd93d8bc1c5bfda6ba13c2fbb668c5b64c1906edd45c16e32203e8fc4cf8c5a36</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/date-fns</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE.md</name>
            <text content-type="text/markdown" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMSBTYXNoYSBLb3NzIGFuZCBMZXNoYSBLb3NzIGh0dHBzOi8va29zc25vY29ycC5taXQtbGljZW5zZS5vcmcKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|eslint-plugin-react@7.37.5">
      <author>Yannick Croissant</author>
      <name>eslint-plugin-react</name>
      <version>7.37.5</version>
      <description>React specific linting rules for ESLint</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/eslint-plugin-react@7.37.5</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/jsx-eslint/eslint-plugin-react.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/jsx-eslint/eslint-plugin-react</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/jsx-eslint/eslint-plugin-react/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/eslint-plugin-react/-/eslint-plugin-react-7.37.5.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">42d7aea744aa535e6476871ec4534024cbc22447dadb150a355e020b5c6c54cac822a132dd243faeacb10963737eb777fe5772e873250f67b42435690e0daa20</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/eslint-plugin-react</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|eslint-plugin-react@7.37.5|minimatch@3.1.2">
          <author>Isaac Z. Schlueter</author>
          <name>minimatch</name>
          <version>3.1.2</version>
          <description>a glob matcher in javascript</description>
          <licenses>
            <license acknowledgement="declared">
              <id>ISC</id>
            </license>
          </licenses>
          <purl>pkg:npm/minimatch@3.1.2</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git://github.com/isaacs/minimatch.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/isaacs/minimatch#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/isaacs/minimatch/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">27ba7ade1462023c35343130c355bb8b7efe07222b3963b95d0400cd9dd539c2f43cdc9bc297e657f374e73140cf043d512c84717eaddd43be2b96aa0503881f</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/eslint-plugin-react/node_modules/minimatch</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">VGhlIElTQyBMaWNlbnNlCgpDb3B5cmlnaHQgKGMpIElzYWFjIFouIFNjaGx1ZXRlciBhbmQgQ29udHJpYnV0b3JzCgpQZXJtaXNzaW9uIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBhbmQvb3IgZGlzdHJpYnV0ZSB0aGlzIHNvZnR3YXJlIGZvciBhbnkKcHVycG9zZSB3aXRoIG9yIHdpdGhvdXQgZmVlIGlzIGhlcmVieSBncmFudGVkLCBwcm92aWRlZCB0aGF0IHRoZSBhYm92ZQpjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIGFwcGVhciBpbiBhbGwgY29waWVzLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIgQU5EIFRIRSBBVVRIT1IgRElTQ0xBSU1TIEFMTCBXQVJSQU5USUVTCldJVEggUkVHQVJEIFRPIFRISVMgU09GVFdBUkUgSU5DTFVESU5HIEFMTCBJTVBMSUVEIFdBUlJBTlRJRVMgT0YKTUVSQ0hBTlRBQklMSVRZIEFORCBGSVRORVNTLiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SIEJFIExJQUJMRSBGT1IKQU5ZIFNQRUNJQUwsIERJUkVDVCwgSU5ESVJFQ1QsIE9SIENPTlNFUVVFTlRJQUwgREFNQUdFUyBPUiBBTlkgREFNQUdFUwpXSEFUU09FVkVSIFJFU1VMVElORyBGUk9NIExPU1MgT0YgVVNFLCBEQVRBIE9SIFBST0ZJVFMsIFdIRVRIRVIgSU4gQU4KQUNUSU9OIE9GIENPTlRSQUNULCBORUdMSUdFTkNFIE9SIE9USEVSIFRPUlRJT1VTIEFDVElPTiwgQVJJU0lORyBPVVQgT0YgT1IKSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBVU0UgT1IgUEVSRk9STUFOQ0UgT0YgVEhJUyBTT0ZUV0FSRS4K</text>
              </license>
            </licenses>
          </evidence>
        </component>
        <component type="library" bom-ref="openbb-platform@1.0.0|eslint-plugin-react@7.37.5|brace-expansion@1.1.12">
          <author>Julian Gruber</author>
          <name>brace-expansion</name>
          <version>1.1.12</version>
          <description>Brace expansion as known from sh/bash</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/brace-expansion@1.1.12</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git://github.com/juliangruber/brace-expansion.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/juliangruber/brace-expansion</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/juliangruber/brace-expansion/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">f53f548d6debd145b973543b193c25969b57c21bd8984cc587331f67d1fb1505adfae65e3e364f8c13ff5b5644c99d6dc065a89b9ff9e9317894f72a8e70c772</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/eslint-plugin-react/node_modules/brace-expansion</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxMyBKdWxpYW4gR3J1YmVyIDxqdWxpYW5AanVsaWFuZ3J1YmVyLmNvbT4KClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCgpDb3B5cmlnaHQgKGMpIDIwMTQgWWFubmljayBDcm9pc3NhbnQKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|eslint@9.37.0">
      <author>Nicholas C. Zakas</author>
      <name>eslint</name>
      <version>9.37.0</version>
      <description>An AST-based pattern checker for JavaScript.</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/eslint@9.37.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/eslint/eslint.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://eslint.org</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/eslint/eslint/issues/</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/eslint/-/eslint-9.37.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">5f22e644e9c0096a92c6219802b75e7f57c8b50778ef07aa07b8b0b5fafd247c11aea21765d70532fbc470bf711c298bd1236c3af174738da55b23355397608a</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/eslint</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|eslint@9.37.0|eslint-visitor-keys@4.2.1">
          <author>Toru Nagashima</author>
          <name>eslint-visitor-keys</name>
          <version>4.2.1</version>
          <description>Constants and utilities about visitor keys to traverse AST.</description>
          <licenses>
            <license acknowledgement="declared">
              <id>Apache-2.0</id>
            </license>
          </licenses>
          <purl>pkg:npm/eslint-visitor-keys@4.2.1#packages/eslint-visitor-keys</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/eslint/js.git#packages/eslint-visitor-keys</url>
              <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/eslint/js/blob/main/packages/eslint-visitor-keys/README.md</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/eslint/js/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-4.2.1.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">521764e6c7ea71e7bff47feb08e262918cfaee8d1ad93c3684644f386d98d51d9d83b6eb45ed6e1b4c9a3500c7bbe4cefee40f17fe5e09aa6f612987523b7b25</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/eslint/node_modules/eslint-visitor-keys</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQXBhY2hlIExpY2Vuc2UKICAgICAgICAgICAgICAgICAgICAgICAgICAgVmVyc2lvbiAyLjAsIEphbnVhcnkgMjAwNAogICAgICAgICAgICAgICAgICAgICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvCgogICBURVJNUyBBTkQgQ09ORElUSU9OUyBGT1IgVVNFLCBSRVBST0RVQ1RJT04sIEFORCBESVNUUklCVVRJT04KCiAgIDEuIERlZmluaXRpb25zLgoKICAgICAgIkxpY2Vuc2UiIHNoYWxsIG1lYW4gdGhlIHRlcm1zIGFuZCBjb25kaXRpb25zIGZvciB1c2UsIHJlcHJvZHVjdGlvbiwKICAgICAgYW5kIGRpc3RyaWJ1dGlvbiBhcyBkZWZpbmVkIGJ5IFNlY3Rpb25zIDEgdGhyb3VnaCA5IG9mIHRoaXMgZG9jdW1lbnQuCgogICAgICAiTGljZW5zb3IiIHNoYWxsIG1lYW4gdGhlIGNvcHlyaWdodCBvd25lciBvciBlbnRpdHkgYXV0aG9yaXplZCBieQogICAgICB0aGUgY29weXJpZ2h0IG93bmVyIHRoYXQgaXMgZ3JhbnRpbmcgdGhlIExpY2Vuc2UuCgogICAgICAiTGVnYWwgRW50aXR5IiBzaGFsbCBtZWFuIHRoZSB1bmlvbiBvZiB0aGUgYWN0aW5nIGVudGl0eSBhbmQgYWxsCiAgICAgIG90aGVyIGVudGl0aWVzIHRoYXQgY29udHJvbCwgYXJlIGNvbnRyb2xsZWQgYnksIG9yIGFyZSB1bmRlciBjb21tb24KICAgICAgY29udHJvbCB3aXRoIHRoYXQgZW50aXR5LiBGb3IgdGhlIHB1cnBvc2VzIG9mIHRoaXMgZGVmaW5pdGlvbiwKICAgICAgImNvbnRyb2wiIG1lYW5zIChpKSB0aGUgcG93ZXIsIGRpcmVjdCBvciBpbmRpcmVjdCwgdG8gY2F1c2UgdGhlCiAgICAgIGRpcmVjdGlvbiBvciBtYW5hZ2VtZW50IG9mIHN1Y2ggZW50aXR5LCB3aGV0aGVyIGJ5IGNvbnRyYWN0IG9yCiAgICAgIG90aGVyd2lzZSwgb3IgKGlpKSBvd25lcnNoaXAgb2YgZmlmdHkgcGVyY2VudCAoNTAlKSBvciBtb3JlIG9mIHRoZQogICAgICBvdXRzdGFuZGluZyBzaGFyZXMsIG9yIChpaWkpIGJlbmVmaWNpYWwgb3duZXJzaGlwIG9mIHN1Y2ggZW50aXR5LgoKICAgICAgIllvdSIgKG9yICJZb3VyIikgc2hhbGwgbWVhbiBhbiBpbmRpdmlkdWFsIG9yIExlZ2FsIEVudGl0eQogICAgICBleGVyY2lzaW5nIHBlcm1pc3Npb25zIGdyYW50ZWQgYnkgdGhpcyBMaWNlbnNlLgoKICAgICAgIlNvdXJjZSIgZm9ybSBzaGFsbCBtZWFuIHRoZSBwcmVmZXJyZWQgZm9ybSBmb3IgbWFraW5nIG1vZGlmaWNhdGlvbnMsCiAgICAgIGluY2x1ZGluZyBidXQgbm90IGxpbWl0ZWQgdG8gc29mdHdhcmUgc291cmNlIGNvZGUsIGRvY3VtZW50YXRpb24KICAgICAgc291cmNlLCBhbmQgY29uZmlndXJhdGlvbiBmaWxlcy4KCiAgICAgICJPYmplY3QiIGZvcm0gc2hhbGwgbWVhbiBhbnkgZm9ybSByZXN1bHRpbmcgZnJvbSBtZWNoYW5pY2FsCiAgICAgIHRyYW5zZm9ybWF0aW9uIG9yIHRyYW5zbGF0aW9uIG9mIGEgU291cmNlIGZvcm0sIGluY2x1ZGluZyBidXQKICAgICAgbm90IGxpbWl0ZWQgdG8gY29tcGlsZWQgb2JqZWN0IGNvZGUsIGdlbmVyYXRlZCBkb2N1bWVudGF0aW9uLAogICAgICBhbmQgY29udmVyc2lvbnMgdG8gb3RoZXIgbWVkaWEgdHlwZXMuCgogICAgICAiV29yayIgc2hhbGwgbWVhbiB0aGUgd29yayBvZiBhdXRob3JzaGlwLCB3aGV0aGVyIGluIFNvdXJjZSBvcgogICAgICBPYmplY3QgZm9ybSwgbWFkZSBhdmFpbGFibGUgdW5kZXIgdGhlIExpY2Vuc2UsIGFzIGluZGljYXRlZCBieSBhCiAgICAgIGNvcHlyaWdodCBub3RpY2UgdGhhdCBpcyBpbmNsdWRlZCBpbiBvciBhdHRhY2hlZCB0byB0aGUgd29yawogICAgICAoYW4gZXhhbXBsZSBpcyBwcm92aWRlZCBpbiB0aGUgQXBwZW5kaXggYmVsb3cpLgoKICAgICAgIkRlcml2YXRpdmUgV29ya3MiIHNoYWxsIG1lYW4gYW55IHdvcmssIHdoZXRoZXIgaW4gU291cmNlIG9yIE9iamVjdAogICAgICBmb3JtLCB0aGF0IGlzIGJhc2VkIG9uIChvciBkZXJpdmVkIGZyb20pIHRoZSBXb3JrIGFuZCBmb3Igd2hpY2ggdGhlCiAgICAgIGVkaXRvcmlhbCByZXZpc2lvbnMsIGFubm90YXRpb25zLCBlbGFib3JhdGlvbnMsIG9yIG90aGVyIG1vZGlmaWNhdGlvbnMKICAgICAgcmVwcmVzZW50LCBhcyBhIHdob2xlLCBhbiBvcmlnaW5hbCB3b3JrIG9mIGF1dGhvcnNoaXAuIEZvciB0aGUgcHVycG9zZXMKICAgICAgb2YgdGhpcyBMaWNlbnNlLCBEZXJpdmF0aXZlIFdvcmtzIHNoYWxsIG5vdCBpbmNsdWRlIHdvcmtzIHRoYXQgcmVtYWluCiAgICAgIHNlcGFyYWJsZSBmcm9tLCBvciBtZXJlbHkgbGluayAob3IgYmluZCBieSBuYW1lKSB0byB0aGUgaW50ZXJmYWNlcyBvZiwKICAgICAgdGhlIFdvcmsgYW5kIERlcml2YXRpdmUgV29ya3MgdGhlcmVvZi4KCiAgICAgICJDb250cmlidXRpb24iIHNoYWxsIG1lYW4gYW55IHdvcmsgb2YgYXV0aG9yc2hpcCwgaW5jbHVkaW5nCiAgICAgIHRoZSBvcmlnaW5hbCB2ZXJzaW9uIG9mIHRoZSBXb3JrIGFuZCBhbnkgbW9kaWZpY2F0aW9ucyBvciBhZGRpdGlvbnMKICAgICAgdG8gdGhhdCBXb3JrIG9yIERlcml2YXRpdmUgV29ya3MgdGhlcmVvZiwgdGhhdCBpcyBpbnRlbnRpb25hbGx5CiAgICAgIHN1Ym1pdHRlZCB0byBMaWNlbnNvciBmb3IgaW5jbHVzaW9uIGluIHRoZSBXb3JrIGJ5IHRoZSBjb3B5cmlnaHQgb3duZXIKICAgICAgb3IgYnkgYW4gaW5kaXZpZHVhbCBvciBMZWdhbCBFbnRpdHkgYXV0aG9yaXplZCB0byBzdWJtaXQgb24gYmVoYWxmIG9mCiAgICAgIHRoZSBjb3B5cmlnaHQgb3duZXIuIEZvciB0aGUgcHVycG9zZXMgb2YgdGhpcyBkZWZpbml0aW9uLCAic3VibWl0dGVkIgogICAgICBtZWFucyBhbnkgZm9ybSBvZiBlbGVjdHJvbmljLCB2ZXJiYWwsIG9yIHdyaXR0ZW4gY29tbXVuaWNhdGlvbiBzZW50CiAgICAgIHRvIHRoZSBMaWNlbnNvciBvciBpdHMgcmVwcmVzZW50YXRpdmVzLCBpbmNsdWRpbmcgYnV0IG5vdCBsaW1pdGVkIHRvCiAgICAgIGNvbW11bmljYXRpb24gb24gZWxlY3Ryb25pYyBtYWlsaW5nIGxpc3RzLCBzb3VyY2UgY29kZSBjb250cm9sIHN5c3RlbXMsCiAgICAgIGFuZCBpc3N1ZSB0cmFja2luZyBzeXN0ZW1zIHRoYXQgYXJlIG1hbmFnZWQgYnksIG9yIG9uIGJlaGFsZiBvZiwgdGhlCiAgICAgIExpY2Vuc29yIGZvciB0aGUgcHVycG9zZSBvZiBkaXNjdXNzaW5nIGFuZCBpbXByb3ZpbmcgdGhlIFdvcmssIGJ1dAogICAgICBleGNsdWRpbmcgY29tbXVuaWNhdGlvbiB0aGF0IGlzIGNvbnNwaWN1b3VzbHkgbWFya2VkIG9yIG90aGVyd2lzZQogICAgICBkZXNpZ25hdGVkIGluIHdyaXRpbmcgYnkgdGhlIGNvcHlyaWdodCBvd25lciBhcyAiTm90IGEgQ29udHJpYnV0aW9uLiIKCiAgICAgICJDb250cmlidXRvciIgc2hhbGwgbWVhbiBMaWNlbnNvciBhbmQgYW55IGluZGl2aWR1YWwgb3IgTGVnYWwgRW50aXR5CiAgICAgIG9uIGJlaGFsZiBvZiB3aG9tIGEgQ29udHJpYnV0aW9uIGhhcyBiZWVuIHJlY2VpdmVkIGJ5IExpY2Vuc29yIGFuZAogICAgICBzdWJzZXF1ZW50bHkgaW5jb3Jwb3JhdGVkIHdpdGhpbiB0aGUgV29yay4KCiAgIDIuIEdyYW50IG9mIENvcHlyaWdodCBMaWNlbnNlLiBTdWJqZWN0IHRvIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZgogICAgICB0aGlzIExpY2Vuc2UsIGVhY2ggQ29udHJpYnV0b3IgaGVyZWJ5IGdyYW50cyB0byBZb3UgYSBwZXJwZXR1YWwsCiAgICAgIHdvcmxkd2lkZSwgbm9uLWV4Y2x1c2l2ZSwgbm8tY2hhcmdlLCByb3lhbHR5LWZyZWUsIGlycmV2b2NhYmxlCiAgICAgIGNvcHlyaWdodCBsaWNlbnNlIHRvIHJlcHJvZHVjZSwgcHJlcGFyZSBEZXJpdmF0aXZlIFdvcmtzIG9mLAogICAgICBwdWJsaWNseSBkaXNwbGF5LCBwdWJsaWNseSBwZXJmb3JtLCBzdWJsaWNlbnNlLCBhbmQgZGlzdHJpYnV0ZSB0aGUKICAgICAgV29yayBhbmQgc3VjaCBEZXJpdmF0aXZlIFdvcmtzIGluIFNvdXJjZSBvciBPYmplY3QgZm9ybS4KCiAgIDMuIEdyYW50IG9mIFBhdGVudCBMaWNlbnNlLiBTdWJqZWN0IHRvIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZgogICAgICB0aGlzIExpY2Vuc2UsIGVhY2ggQ29udHJpYnV0b3IgaGVyZWJ5IGdyYW50cyB0byBZb3UgYSBwZXJwZXR1YWwsCiAgICAgIHdvcmxkd2lkZSwgbm9uLWV4Y2x1c2l2ZSwgbm8tY2hhcmdlLCByb3lhbHR5LWZyZWUsIGlycmV2b2NhYmxlCiAgICAgIChleGNlcHQgYXMgc3RhdGVkIGluIHRoaXMgc2VjdGlvbikgcGF0ZW50IGxpY2Vuc2UgdG8gbWFrZSwgaGF2ZSBtYWRlLAogICAgICB1c2UsIG9mZmVyIHRvIHNlbGwsIHNlbGwsIGltcG9ydCwgYW5kIG90aGVyd2lzZSB0cmFuc2ZlciB0aGUgV29yaywKICAgICAgd2hlcmUgc3VjaCBsaWNlbnNlIGFwcGxpZXMgb25seSB0byB0aG9zZSBwYXRlbnQgY2xhaW1zIGxpY2Vuc2FibGUKICAgICAgYnkgc3VjaCBDb250cmlidXRvciB0aGF0IGFyZSBuZWNlc3NhcmlseSBpbmZyaW5nZWQgYnkgdGhlaXIKICAgICAgQ29udHJpYnV0aW9uKHMpIGFsb25lIG9yIGJ5IGNvbWJpbmF0aW9uIG9mIHRoZWlyIENvbnRyaWJ1dGlvbihzKQogICAgICB3aXRoIHRoZSBXb3JrIHRvIHdoaWNoIHN1Y2ggQ29udHJpYnV0aW9uKHMpIHdhcyBzdWJtaXR0ZWQuIElmIFlvdQogICAgICBpbnN0aXR1dGUgcGF0ZW50IGxpdGlnYXRpb24gYWdhaW5zdCBhbnkgZW50aXR5IChpbmNsdWRpbmcgYQogICAgICBjcm9zcy1jbGFpbSBvciBjb3VudGVyY2xhaW0gaW4gYSBsYXdzdWl0KSBhbGxlZ2luZyB0aGF0IHRoZSBXb3JrCiAgICAgIG9yIGEgQ29udHJpYnV0aW9uIGluY29ycG9yYXRlZCB3aXRoaW4gdGhlIFdvcmsgY29uc3RpdHV0ZXMgZGlyZWN0CiAgICAgIG9yIGNvbnRyaWJ1dG9yeSBwYXRlbnQgaW5mcmluZ2VtZW50LCB0aGVuIGFueSBwYXRlbnQgbGljZW5zZXMKICAgICAgZ3JhbnRlZCB0byBZb3UgdW5kZXIgdGhpcyBMaWNlbnNlIGZvciB0aGF0IFdvcmsgc2hhbGwgdGVybWluYXRlCiAgICAgIGFzIG9mIHRoZSBkYXRlIHN1Y2ggbGl0aWdhdGlvbiBpcyBmaWxlZC4KCiAgIDQuIFJlZGlzdHJpYnV0aW9uLiBZb3UgbWF5IHJlcHJvZHVjZSBhbmQgZGlzdHJpYnV0ZSBjb3BpZXMgb2YgdGhlCiAgICAgIFdvcmsgb3IgRGVyaXZhdGl2ZSBXb3JrcyB0aGVyZW9mIGluIGFueSBtZWRpdW0sIHdpdGggb3Igd2l0aG91dAogICAgICBtb2RpZmljYXRpb25zLCBhbmQgaW4gU291cmNlIG9yIE9iamVjdCBmb3JtLCBwcm92aWRlZCB0aGF0IFlvdQogICAgICBtZWV0IHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKCiAgICAgIChhKSBZb3UgbXVzdCBnaXZlIGFueSBvdGhlciByZWNpcGllbnRzIG9mIHRoZSBXb3JrIG9yCiAgICAgICAgICBEZXJpdmF0aXZlIFdvcmtzIGEgY29weSBvZiB0aGlzIExpY2Vuc2U7IGFuZAoKICAgICAgKGIpIFlvdSBtdXN0IGNhdXNlIGFueSBtb2RpZmllZCBmaWxlcyB0byBjYXJyeSBwcm9taW5lbnQgbm90aWNlcwogICAgICAgICAgc3RhdGluZyB0aGF0IFlvdSBjaGFuZ2VkIHRoZSBmaWxlczsgYW5kCgogICAgICAoYykgWW91IG11c3QgcmV0YWluLCBpbiB0aGUgU291cmNlIGZvcm0gb2YgYW55IERlcml2YXRpdmUgV29ya3MKICAgICAgICAgIHRoYXQgWW91IGRpc3RyaWJ1dGUsIGFsbCBjb3B5cmlnaHQsIHBhdGVudCwgdHJhZGVtYXJrLCBhbmQKICAgICAgICAgIGF0dHJpYnV0aW9uIG5vdGljZXMgZnJvbSB0aGUgU291cmNlIGZvcm0gb2YgdGhlIFdvcmssCiAgICAgICAgICBleGNsdWRpbmcgdGhvc2Ugbm90aWNlcyB0aGF0IGRvIG5vdCBwZXJ0YWluIHRvIGFueSBwYXJ0IG9mCiAgICAgICAgICB0aGUgRGVyaXZhdGl2ZSBXb3JrczsgYW5kCgogICAgICAoZCkgSWYgdGhlIFdvcmsgaW5jbHVkZXMgYSAiTk9USUNFIiB0ZXh0IGZpbGUgYXMgcGFydCBvZiBpdHMKICAgICAgICAgIGRpc3RyaWJ1dGlvbiwgdGhlbiBhbnkgRGVyaXZhdGl2ZSBXb3JrcyB0aGF0IFlvdSBkaXN0cmlidXRlIG11c3QKICAgICAgICAgIGluY2x1ZGUgYSByZWFkYWJsZSBjb3B5IG9mIHRoZSBhdHRyaWJ1dGlvbiBub3RpY2VzIGNvbnRhaW5lZAogICAgICAgICAgd2l0aGluIHN1Y2ggTk9USUNFIGZpbGUsIGV4Y2x1ZGluZyB0aG9zZSBub3RpY2VzIHRoYXQgZG8gbm90CiAgICAgICAgICBwZXJ0YWluIHRvIGFueSBwYXJ0IG9mIHRoZSBEZXJpdmF0aXZlIFdvcmtzLCBpbiBhdCBsZWFzdCBvbmUKICAgICAgICAgIG9mIHRoZSBmb2xsb3dpbmcgcGxhY2VzOiB3aXRoaW4gYSBOT1RJQ0UgdGV4dCBmaWxlIGRpc3RyaWJ1dGVkCiAgICAgICAgICBhcyBwYXJ0IG9mIHRoZSBEZXJpdmF0aXZlIFdvcmtzOyB3aXRoaW4gdGhlIFNvdXJjZSBmb3JtIG9yCiAgICAgICAgICBkb2N1bWVudGF0aW9uLCBpZiBwcm92aWRlZCBhbG9uZyB3aXRoIHRoZSBEZXJpdmF0aXZlIFdvcmtzOyBvciwKICAgICAgICAgIHdpdGhpbiBhIGRpc3BsYXkgZ2VuZXJhdGVkIGJ5IHRoZSBEZXJpdmF0aXZlIFdvcmtzLCBpZiBhbmQKICAgICAgICAgIHdoZXJldmVyIHN1Y2ggdGhpcmQtcGFydHkgbm90aWNlcyBub3JtYWxseSBhcHBlYXIuIFRoZSBjb250ZW50cwogICAgICAgICAgb2YgdGhlIE5PVElDRSBmaWxlIGFyZSBmb3IgaW5mb3JtYXRpb25hbCBwdXJwb3NlcyBvbmx5IGFuZAogICAgICAgICAgZG8gbm90IG1vZGlmeSB0aGUgTGljZW5zZS4gWW91IG1heSBhZGQgWW91ciBvd24gYXR0cmlidXRpb24KICAgICAgICAgIG5vdGljZXMgd2l0aGluIERlcml2YXRpdmUgV29ya3MgdGhhdCBZb3UgZGlzdHJpYnV0ZSwgYWxvbmdzaWRlCiAgICAgICAgICBvciBhcyBhbiBhZGRlbmR1bSB0byB0aGUgTk9USUNFIHRleHQgZnJvbSB0aGUgV29yaywgcHJvdmlkZWQKICAgICAgICAgIHRoYXQgc3VjaCBhZGRpdGlvbmFsIGF0dHJpYnV0aW9uIG5vdGljZXMgY2Fubm90IGJlIGNvbnN0cnVlZAogICAgICAgICAgYXMgbW9kaWZ5aW5nIHRoZSBMaWNlbnNlLgoKICAgICAgWW91IG1heSBhZGQgWW91ciBvd24gY29weXJpZ2h0IHN0YXRlbWVudCB0byBZb3VyIG1vZGlmaWNhdGlvbnMgYW5kCiAgICAgIG1heSBwcm92aWRlIGFkZGl0aW9uYWwgb3IgZGlmZmVyZW50IGxpY2Vuc2UgdGVybXMgYW5kIGNvbmRpdGlvbnMKICAgICAgZm9yIHVzZSwgcmVwcm9kdWN0aW9uLCBvciBkaXN0cmlidXRpb24gb2YgWW91ciBtb2RpZmljYXRpb25zLCBvcgogICAgICBmb3IgYW55IHN1Y2ggRGVyaXZhdGl2ZSBXb3JrcyBhcyBhIHdob2xlLCBwcm92aWRlZCBZb3VyIHVzZSwKICAgICAgcmVwcm9kdWN0aW9uLCBhbmQgZGlzdHJpYnV0aW9uIG9mIHRoZSBXb3JrIG90aGVyd2lzZSBjb21wbGllcyB3aXRoCiAgICAgIHRoZSBjb25kaXRpb25zIHN0YXRlZCBpbiB0aGlzIExpY2Vuc2UuCgogICA1LiBTdWJtaXNzaW9uIG9mIENvbnRyaWJ1dGlvbnMuIFVubGVzcyBZb3UgZXhwbGljaXRseSBzdGF0ZSBvdGhlcndpc2UsCiAgICAgIGFueSBDb250cmlidXRpb24gaW50ZW50aW9uYWxseSBzdWJtaXR0ZWQgZm9yIGluY2x1c2lvbiBpbiB0aGUgV29yawogICAgICBieSBZb3UgdG8gdGhlIExpY2Vuc29yIHNoYWxsIGJlIHVuZGVyIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZgogICAgICB0aGlzIExpY2Vuc2UsIHdpdGhvdXQgYW55IGFkZGl0aW9uYWwgdGVybXMgb3IgY29uZGl0aW9ucy4KICAgICAgTm90d2l0aHN0YW5kaW5nIHRoZSBhYm92ZSwgbm90aGluZyBoZXJlaW4gc2hhbGwgc3VwZXJzZWRlIG9yIG1vZGlmeQogICAgICB0aGUgdGVybXMgb2YgYW55IHNlcGFyYXRlIGxpY2Vuc2UgYWdyZWVtZW50IHlvdSBtYXkgaGF2ZSBleGVjdXRlZAogICAgICB3aXRoIExpY2Vuc29yIHJlZ2FyZGluZyBzdWNoIENvbnRyaWJ1dGlvbnMuCgogICA2LiBUcmFkZW1hcmtzLiBUaGlzIExpY2Vuc2UgZG9lcyBub3QgZ3JhbnQgcGVybWlzc2lvbiB0byB1c2UgdGhlIHRyYWRlCiAgICAgIG5hbWVzLCB0cmFkZW1hcmtzLCBzZXJ2aWNlIG1hcmtzLCBvciBwcm9kdWN0IG5hbWVzIG9mIHRoZSBMaWNlbnNvciwKICAgICAgZXhjZXB0IGFzIHJlcXVpcmVkIGZvciByZWFzb25hYmxlIGFuZCBjdXN0b21hcnkgdXNlIGluIGRlc2NyaWJpbmcgdGhlCiAgICAgIG9yaWdpbiBvZiB0aGUgV29yayBhbmQgcmVwcm9kdWNpbmcgdGhlIGNvbnRlbnQgb2YgdGhlIE5PVElDRSBmaWxlLgoKICAgNy4gRGlzY2xhaW1lciBvZiBXYXJyYW50eS4gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yCiAgICAgIGFncmVlZCB0byBpbiB3cml0aW5nLCBMaWNlbnNvciBwcm92aWRlcyB0aGUgV29yayAoYW5kIGVhY2gKICAgICAgQ29udHJpYnV0b3IgcHJvdmlkZXMgaXRzIENvbnRyaWJ1dGlvbnMpIG9uIGFuICJBUyBJUyIgQkFTSVMsCiAgICAgIFdJVEhPVVQgV0FSUkFOVElFUyBPUiBDT05ESVRJT05TIE9GIEFOWSBLSU5ELCBlaXRoZXIgZXhwcmVzcyBvcgogICAgICBpbXBsaWVkLCBpbmNsdWRpbmcsIHdpdGhvdXQgbGltaXRhdGlvbiwgYW55IHdhcnJhbnRpZXMgb3IgY29uZGl0aW9ucwogICAgICBvZiBUSVRMRSwgTk9OLUlORlJJTkdFTUVOVCwgTUVSQ0hBTlRBQklMSVRZLCBvciBGSVRORVNTIEZPUiBBCiAgICAgIFBBUlRJQ1VMQVIgUFVSUE9TRS4gWW91IGFyZSBzb2xlbHkgcmVzcG9uc2libGUgZm9yIGRldGVybWluaW5nIHRoZQogICAgICBhcHByb3ByaWF0ZW5lc3Mgb2YgdXNpbmcgb3IgcmVkaXN0cmlidXRpbmcgdGhlIFdvcmsgYW5kIGFzc3VtZSBhbnkKICAgICAgcmlza3MgYXNzb2NpYXRlZCB3aXRoIFlvdXIgZXhlcmNpc2Ugb2YgcGVybWlzc2lvbnMgdW5kZXIgdGhpcyBMaWNlbnNlLgoKICAgOC4gTGltaXRhdGlvbiBvZiBMaWFiaWxpdHkuIEluIG5vIGV2ZW50IGFuZCB1bmRlciBubyBsZWdhbCB0aGVvcnksCiAgICAgIHdoZXRoZXIgaW4gdG9ydCAoaW5jbHVkaW5nIG5lZ2xpZ2VuY2UpLCBjb250cmFjdCwgb3Igb3RoZXJ3aXNlLAogICAgICB1bmxlc3MgcmVxdWlyZWQgYnkgYXBwbGljYWJsZSBsYXcgKHN1Y2ggYXMgZGVsaWJlcmF0ZSBhbmQgZ3Jvc3NseQogICAgICBuZWdsaWdlbnQgYWN0cykgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsIHNoYWxsIGFueSBDb250cmlidXRvciBiZQogICAgICBsaWFibGUgdG8gWW91IGZvciBkYW1hZ2VzLCBpbmNsdWRpbmcgYW55IGRpcmVjdCwgaW5kaXJlY3QsIHNwZWNpYWwsCiAgICAgIGluY2lkZW50YWwsIG9yIGNvbnNlcXVlbnRpYWwgZGFtYWdlcyBvZiBhbnkgY2hhcmFjdGVyIGFyaXNpbmcgYXMgYQogICAgICByZXN1bHQgb2YgdGhpcyBMaWNlbnNlIG9yIG91dCBvZiB0aGUgdXNlIG9yIGluYWJpbGl0eSB0byB1c2UgdGhlCiAgICAgIFdvcmsgKGluY2x1ZGluZyBidXQgbm90IGxpbWl0ZWQgdG8gZGFtYWdlcyBmb3IgbG9zcyBvZiBnb29kd2lsbCwKICAgICAgd29yayBzdG9wcGFnZSwgY29tcHV0ZXIgZmFpbHVyZSBvciBtYWxmdW5jdGlvbiwgb3IgYW55IGFuZCBhbGwKICAgICAgb3RoZXIgY29tbWVyY2lhbCBkYW1hZ2VzIG9yIGxvc3NlcyksIGV2ZW4gaWYgc3VjaCBDb250cmlidXRvcgogICAgICBoYXMgYmVlbiBhZHZpc2VkIG9mIHRoZSBwb3NzaWJpbGl0eSBvZiBzdWNoIGRhbWFnZXMuCgogICA5LiBBY2NlcHRpbmcgV2FycmFudHkgb3IgQWRkaXRpb25hbCBMaWFiaWxpdHkuIFdoaWxlIHJlZGlzdHJpYnV0aW5nCiAgICAgIHRoZSBXb3JrIG9yIERlcml2YXRpdmUgV29ya3MgdGhlcmVvZiwgWW91IG1heSBjaG9vc2UgdG8gb2ZmZXIsCiAgICAgIGFuZCBjaGFyZ2UgYSBmZWUgZm9yLCBhY2NlcHRhbmNlIG9mIHN1cHBvcnQsIHdhcnJhbnR5LCBpbmRlbW5pdHksCiAgICAgIG9yIG90aGVyIGxpYWJpbGl0eSBvYmxpZ2F0aW9ucyBhbmQvb3IgcmlnaHRzIGNvbnNpc3RlbnQgd2l0aCB0aGlzCiAgICAgIExpY2Vuc2UuIEhvd2V2ZXIsIGluIGFjY2VwdGluZyBzdWNoIG9ibGlnYXRpb25zLCBZb3UgbWF5IGFjdCBvbmx5CiAgICAgIG9uIFlvdXIgb3duIGJlaGFsZiBhbmQgb24gWW91ciBzb2xlIHJlc3BvbnNpYmlsaXR5LCBub3Qgb24gYmVoYWxmCiAgICAgIG9mIGFueSBvdGhlciBDb250cmlidXRvciwgYW5kIG9ubHkgaWYgWW91IGFncmVlIHRvIGluZGVtbmlmeSwKICAgICAgZGVmZW5kLCBhbmQgaG9sZCBlYWNoIENvbnRyaWJ1dG9yIGhhcm1sZXNzIGZvciBhbnkgbGlhYmlsaXR5CiAgICAgIGluY3VycmVkIGJ5LCBvciBjbGFpbXMgYXNzZXJ0ZWQgYWdhaW5zdCwgc3VjaCBDb250cmlidXRvciBieSByZWFzb24KICAgICAgb2YgeW91ciBhY2NlcHRpbmcgYW55IHN1Y2ggd2FycmFudHkgb3IgYWRkaXRpb25hbCBsaWFiaWxpdHkuCgogICBFTkQgT0YgVEVSTVMgQU5EIENPTkRJVElPTlMKCiAgIEFQUEVORElYOiBIb3cgdG8gYXBwbHkgdGhlIEFwYWNoZSBMaWNlbnNlIHRvIHlvdXIgd29yay4KCiAgICAgIFRvIGFwcGx5IHRoZSBBcGFjaGUgTGljZW5zZSB0byB5b3VyIHdvcmssIGF0dGFjaCB0aGUgZm9sbG93aW5nCiAgICAgIGJvaWxlcnBsYXRlIG5vdGljZSwgd2l0aCB0aGUgZmllbGRzIGVuY2xvc2VkIGJ5IGJyYWNrZXRzICJ7fSIKICAgICAgcmVwbGFjZWQgd2l0aCB5b3VyIG93biBpZGVudGlmeWluZyBpbmZvcm1hdGlvbi4gKERvbid0IGluY2x1ZGUKICAgICAgdGhlIGJyYWNrZXRzISkgIFRoZSB0ZXh0IHNob3VsZCBiZSBlbmNsb3NlZCBpbiB0aGUgYXBwcm9wcmlhdGUKICAgICAgY29tbWVudCBzeW50YXggZm9yIHRoZSBmaWxlIGZvcm1hdC4gV2UgYWxzbyByZWNvbW1lbmQgdGhhdCBhCiAgICAgIGZpbGUgb3IgY2xhc3MgbmFtZSBhbmQgZGVzY3JpcHRpb24gb2YgcHVycG9zZSBiZSBpbmNsdWRlZCBvbiB0aGUKICAgICAgc2FtZSAicHJpbnRlZCBwYWdlIiBhcyB0aGUgY29weXJpZ2h0IG5vdGljZSBmb3IgZWFzaWVyCiAgICAgIGlkZW50aWZpY2F0aW9uIHdpdGhpbiB0aGlyZC1wYXJ0eSBhcmNoaXZlcy4KCiAgIENvcHlyaWdodCBjb250cmlidXRvcnMKCiAgIExpY2Vuc2VkIHVuZGVyIHRoZSBBcGFjaGUgTGljZW5zZSwgVmVyc2lvbiAyLjAgKHRoZSAiTGljZW5zZSIpOwogICB5b3UgbWF5IG5vdCB1c2UgdGhpcyBmaWxlIGV4Y2VwdCBpbiBjb21wbGlhbmNlIHdpdGggdGhlIExpY2Vuc2UuCiAgIFlvdSBtYXkgb2J0YWluIGEgY29weSBvZiB0aGUgTGljZW5zZSBhdAoKICAgICAgIGh0dHA6Ly93d3cuYXBhY2hlLm9yZy9saWNlbnNlcy9MSUNFTlNFLTIuMAoKICAgVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQogICBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAogICBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KICAgU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAogICBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4K</text>
              </license>
            </licenses>
          </evidence>
        </component>
        <component type="library" bom-ref="openbb-platform@1.0.0|eslint@9.37.0|glob-parent@6.0.2">
          <author>Gulp Team</author>
          <name>glob-parent</name>
          <version>6.0.2</version>
          <description>Extract the non-magic parent path from a glob string.</description>
          <licenses>
            <license acknowledgement="declared">
              <id>ISC</id>
            </license>
          </licenses>
          <purl>pkg:npm/glob-parent@6.0.2</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/gulpjs/glob-parent.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/gulpjs/glob-parent#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/gulpjs/glob-parent/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">5f1c08f043a1550816a7a8832feddbd2bf3a7f877a017eb3494e791df078c9d084b972d773915c61e3aefa79c67ed4b84c48eeff5d6bb782893d33206df9afe0</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/eslint/node_modules/glob-parent</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">VGhlIElTQyBMaWNlbnNlCgpDb3B5cmlnaHQgKGMpIDIwMTUsIDIwMTkgRWxhbiBTaGFua2VyLCAyMDIxIEJsYWluZSBCdWJsaXR6IDxibGFpbmUuYnVibGl0ekBnbWFpbC5jb20+LCBFcmljIFNjaG9mZnN0YWxsIDx5b0Bjb250cmEuaW8+IGFuZCBvdGhlciBjb250cmlidXRvcnMKClBlcm1pc3Npb24gdG8gdXNlLCBjb3B5LCBtb2RpZnksIGFuZC9vciBkaXN0cmlidXRlIHRoaXMgc29mdHdhcmUgZm9yIGFueQpwdXJwb3NlIHdpdGggb3Igd2l0aG91dCBmZWUgaXMgaGVyZWJ5IGdyYW50ZWQsIHByb3ZpZGVkIHRoYXQgdGhlIGFib3ZlCmNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2UgYXBwZWFyIGluIGFsbCBjb3BpZXMuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiBBTkQgVEhFIEFVVEhPUiBESVNDTEFJTVMgQUxMIFdBUlJBTlRJRVMKV0lUSCBSRUdBUkQgVE8gVEhJUyBTT0ZUV0FSRSBJTkNMVURJTkcgQUxMIElNUExJRUQgV0FSUkFOVElFUyBPRgpNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1IgQkUgTElBQkxFIEZPUgpBTlkgU1BFQ0lBTCwgRElSRUNULCBJTkRJUkVDVCwgT1IgQ09OU0VRVUVOVElBTCBEQU1BR0VTIE9SIEFOWSBEQU1BR0VTCldIQVRTT0VWRVIgUkVTVUxUSU5HIEZST00gTE9TUyBPRiBVU0UsIERBVEEgT1IgUFJPRklUUywgV0hFVEhFUiBJTiBBTgpBQ1RJT04gT0YgQ09OVFJBQ1QsIE5FR0xJR0VOQ0UgT1IgT1RIRVIgVE9SVElPVVMgQUNUSU9OLCBBUklTSU5HIE9VVCBPRiBPUgpJTiBDT05ORUNUSU9OIFdJVEggVEhFIFVTRSBPUiBQRVJGT1JNQU5DRSBPRiBUSElTIFNPRlRXQVJFLgo=</text>
              </license>
            </licenses>
          </evidence>
        </component>
        <component type="library" bom-ref="openbb-platform@1.0.0|eslint@9.37.0|ignore@5.3.2">
          <author>kael</author>
          <name>ignore</name>
          <version>5.3.2</version>
          <description>Ignore is a manager and filter for .gitignore rules, the one used by eslint, gitbook and many others.</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/ignore@5.3.2</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+ssh://git@github.com/kaelzhang/node-ignore.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/kaelzhang/node-ignore#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/kaelzhang/node-ignore/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">86c053354a904c3c245ad71d608da2d3a63f9d4044b0d10324a8d676280bbde832f240ee2404bcb91969924710a721172f467fa630f2e4706632344227682afa</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/eslint/node_modules/ignore</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE-MIT</name>
                <text content-type="text/plain" encoding="base64">Q29weXJpZ2h0IChjKSAyMDEzIEthZWwgWmhhbmcgPGlAa2FlbC5tZT4sIGNvbnRyaWJ1dG9ycwpodHRwOi8va2FlbC5tZS8KClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZwphIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUKIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZwp3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsCmRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0bwpwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8KdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUKaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwKRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GCk1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5ECk5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUKTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTgpPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04KV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUu</text>
              </license>
            </licenses>
          </evidence>
        </component>
        <component type="library" bom-ref="openbb-platform@1.0.0|eslint@9.37.0|minimatch@3.1.2">
          <author>Isaac Z. Schlueter</author>
          <name>minimatch</name>
          <version>3.1.2</version>
          <description>a glob matcher in javascript</description>
          <licenses>
            <license acknowledgement="declared">
              <id>ISC</id>
            </license>
          </licenses>
          <purl>pkg:npm/minimatch@3.1.2</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git://github.com/isaacs/minimatch.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/isaacs/minimatch#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/isaacs/minimatch/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/minimatch/-/minimatch-3.1.2.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">27ba7ade1462023c35343130c355bb8b7efe07222b3963b95d0400cd9dd539c2f43cdc9bc297e657f374e73140cf043d512c84717eaddd43be2b96aa0503881f</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/eslint/node_modules/minimatch</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">VGhlIElTQyBMaWNlbnNlCgpDb3B5cmlnaHQgKGMpIElzYWFjIFouIFNjaGx1ZXRlciBhbmQgQ29udHJpYnV0b3JzCgpQZXJtaXNzaW9uIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBhbmQvb3IgZGlzdHJpYnV0ZSB0aGlzIHNvZnR3YXJlIGZvciBhbnkKcHVycG9zZSB3aXRoIG9yIHdpdGhvdXQgZmVlIGlzIGhlcmVieSBncmFudGVkLCBwcm92aWRlZCB0aGF0IHRoZSBhYm92ZQpjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIGFwcGVhciBpbiBhbGwgY29waWVzLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIgQU5EIFRIRSBBVVRIT1IgRElTQ0xBSU1TIEFMTCBXQVJSQU5USUVTCldJVEggUkVHQVJEIFRPIFRISVMgU09GVFdBUkUgSU5DTFVESU5HIEFMTCBJTVBMSUVEIFdBUlJBTlRJRVMgT0YKTUVSQ0hBTlRBQklMSVRZIEFORCBGSVRORVNTLiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SIEJFIExJQUJMRSBGT1IKQU5ZIFNQRUNJQUwsIERJUkVDVCwgSU5ESVJFQ1QsIE9SIENPTlNFUVVFTlRJQUwgREFNQUdFUyBPUiBBTlkgREFNQUdFUwpXSEFUU09FVkVSIFJFU1VMVElORyBGUk9NIExPU1MgT0YgVVNFLCBEQVRBIE9SIFBST0ZJVFMsIFdIRVRIRVIgSU4gQU4KQUNUSU9OIE9GIENPTlRSQUNULCBORUdMSUdFTkNFIE9SIE9USEVSIFRPUlRJT1VTIEFDVElPTiwgQVJJU0lORyBPVVQgT0YgT1IKSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBVU0UgT1IgUEVSRk9STUFOQ0UgT0YgVEhJUyBTT0ZUV0FSRS4K</text>
              </license>
            </licenses>
          </evidence>
        </component>
        <component type="library" bom-ref="openbb-platform@1.0.0|eslint@9.37.0|brace-expansion@1.1.12">
          <author>Julian Gruber</author>
          <name>brace-expansion</name>
          <version>1.1.12</version>
          <description>Brace expansion as known from sh/bash</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/brace-expansion@1.1.12</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git://github.com/juliangruber/brace-expansion.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/juliangruber/brace-expansion</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/juliangruber/brace-expansion/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/brace-expansion/-/brace-expansion-1.1.12.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">f53f548d6debd145b973543b193c25969b57c21bd8984cc587331f67d1fb1505adfae65e3e364f8c13ff5b5644c99d6dc065a89b9ff9e9317894f72a8e70c772</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/eslint/node_modules/brace-expansion</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxMyBKdWxpYW4gR3J1YmVyIDxqdWxpYW5AanVsaWFuZ3J1YmVyLmNvbT4KClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">Q29weXJpZ2h0IE9wZW5KUyBGb3VuZGF0aW9uIGFuZCBvdGhlciBjb250cmlidXRvcnMsIDx3d3cub3BlbmpzZi5vcmc+CgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCmFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KVEhFIFNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|jsdom@26.1.0">
      <name>jsdom</name>
      <version>26.1.0</version>
      <description>A JavaScript implementation of many web standards</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/jsdom@26.1.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/jsdom/jsdom.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/jsdom/jsdom#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/jsdom/jsdom/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/jsdom/-/jsdom-26.1.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">0af73d59487148c128e0c7044b73fba0add069795d09f356a7ba65d8d35e8881650a82ebde47eaf646f57f17ed8b093514b57b0afa6f0dfa27c6dcd40de48e3e</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/jsdom</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE.txt</name>
            <text content-type="text/plain" encoding="base64">Q29weXJpZ2h0IChjKSAyMDEwIEVsaWphaCBJbnN1YQoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24Kb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24KZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dApyZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwKY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlClNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nCmNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZQppbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELApFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMKT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQKTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQKSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksCldIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORwpGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SCk9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|postcss@8.5.6">
      <author>Andrey Sitnik</author>
      <name>postcss</name>
      <version>8.5.6</version>
      <description>Tool for transforming styles with JS plugins</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/postcss@8.5.6</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/postcss/postcss.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://postcss.org/</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/postcss/postcss/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/postcss/-/postcss-8.5.6.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">dd86e2d6d02ec003fdb34af5510d89e27e58d06d396c99295083b4fdb23d321c260fbd12e5a4d66d7181c311eb7a54fe5ccd64e9d334a64f92c0d9294d137b3e</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/postcss</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCgpDb3B5cmlnaHQgMjAxMyBBbmRyZXkgU2l0bmlrIDxhbmRyZXlAc2l0bmlrLnJ1PgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZgp0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbgp0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvCnVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mCnRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywKc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTCkZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUgpDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIKSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4KQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|react-dom@18.3.1">
      <name>react-dom</name>
      <version>18.3.1</version>
      <description>React package for working with the DOM.</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/react-dom@18.3.1#packages/react-dom</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/facebook/react.git#packages/react-dom</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://reactjs.org/</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/facebook/react/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/react-dom/-/react-dom-18.3.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">e66e2740aa7ead945bd3d2cd1f9f463380714e1f76e75ff295b2886e97bb4e91b17c9fbd92fe812e42c15c88e3b296e06e720136a948db7b519d3593d2c9d423</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/react-dom</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgRmFjZWJvb2ssIEluYy4gYW5kIGl0cyBhZmZpbGlhdGVzLgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|react-hook-form@7.64.0">
      <author>Beier</author>
      <name>react-hook-form</name>
      <version>7.64.0</version>
      <description>Performant, flexible and extensible forms library for React Hooks</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/react-hook-form@7.64.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/react-hook-form/react-hook-form.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://react-hook-form.com</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/react-hook-form/react-hook-form/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/react-hook-form/-/react-hook-form-7.64.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">7e737ebef4e230b9d1a8a3535610f2b1dad46b2d245140329909c52339e6803bdaa63bde51638e3ea30dccf83e03ed327fd0ee13687ac73063375b3e431f3072</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/react-hook-form</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxOS1wcmVzZW50IEJlaWVyKEJpbGwpIEx1bwoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|react-markdown@8.0.7">
      <author>Espen Hovlandsdal</author>
      <name>react-markdown</name>
      <version>8.0.7</version>
      <description>React component to render markdown</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/react-markdown@8.0.7</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/remarkjs/react-markdown.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/remarkjs/react-markdown#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/remarkjs/react-markdown/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/react-markdown/-/react-markdown-8.0.7.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">6ef59bcc6e0cb4e53ad97a81c775f1fb3076ada68516cab8998880cdf8d724c133dac8b181e01fada037b6fcd42c5d3665d38c50e29304515a6490c3aeaf8125</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/react-markdown</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|react-markdown@8.0.7|react-is@18.3.1">
          <name>react-is</name>
          <version>18.3.1</version>
          <description>Brand checking of React Elements.</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/react-is@18.3.1#packages/react-is</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/facebook/react.git#packages/react-is</url>
              <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
            </reference>
            <reference type="website">
              <url>https://reactjs.org/</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/facebook/react/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/react-is/-/react-is-18.3.1.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">fcb2cc5726acd258e302da1888fa9888bf15597cd451d4e1ae6539fa7db40d9bfe6be0a54687af533c3927153e21e879fdcf3bcada13055f46d4588a7cd25d9a</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:path">node_modules/react-markdown/node_modules/react-is</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgRmFjZWJvb2ssIEluYy4gYW5kIGl0cyBhZmZpbGlhdGVzLgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence>
        <licenses>
          <license>
            <name>file: license</name>
            <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCgpDb3B5cmlnaHQgKGMpIDIwMTUgRXNwZW4gSG92bGFuZHNkYWwKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|react-select@5.10.2">
      <author>Jed Watson</author>
      <name>react-select</name>
      <version>5.10.2</version>
      <description>A Select control built with and for ReactJS</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/react-select@5.10.2#master</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/JedWatson/react-select.git#master</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/JedWatson/react-select/tree/master#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/JedWatson/react-select/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/react-select/-/react-select-5.10.2.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">677de71dd1055aaf6d7e77d55da88cd76adb26693e423144ced58bb665ea421cfa025e14659f71734c226ad986b543820a71cdd168b32f7b42318444357e2b55</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/react-select</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCgpDb3B5cmlnaHQgKGMpIDIwMjIgSmVkIFdhdHNvbgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|react@18.3.1">
      <name>react</name>
      <version>18.3.1</version>
      <description>React is a JavaScript library for building user interfaces.</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/react@18.3.1#packages/react</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/facebook/react.git#packages/react</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://reactjs.org/</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/facebook/react/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/react/-/react-18.3.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">c12fa1020252851d0a844bcf240adfb8f54dd7e1f3d6dd18ea7e632eb1906e46f8bab80f13fd11bdefb590c075bffa16807826e1621c57e8bb176a53563fb689</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/react</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgRmFjZWJvb2ssIEluYy4gYW5kIGl0cyBhZmZpbGlhdGVzLgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|tailwindcss@3.4.18">
      <name>tailwindcss</name>
      <version>3.4.18</version>
      <description>A utility-first CSS framework for rapidly building custom user interfaces.</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/tailwindcss@3.4.18</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/tailwindlabs/tailwindcss.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://tailwindcss.com</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/tailwindlabs/tailwindcss/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/tailwindcss/-/tailwindcss-3.4.18.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">e80dab9e65b9c5931dc35d4b62385c239f38eabb7da5b2d269b6395cfc68f9759dc7065a1449f8ec6a383731621eef6c34d9abfe45e2bcfd6f4ad7ef31a2b519</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/tailwindcss</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|tailwindcss@3.4.18|glob-parent@6.0.2">
          <author>Gulp Team</author>
          <name>glob-parent</name>
          <version>6.0.2</version>
          <description>Extract the non-magic parent path from a glob string.</description>
          <licenses>
            <license acknowledgement="declared">
              <id>ISC</id>
            </license>
          </licenses>
          <purl>pkg:npm/glob-parent@6.0.2</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/gulpjs/glob-parent.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/gulpjs/glob-parent#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/gulpjs/glob-parent/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">5f1c08f043a1550816a7a8832feddbd2bf3a7f877a017eb3494e791df078c9d084b972d773915c61e3aefa79c67ed4b84c48eeff5d6bb782893d33206df9afe0</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:path">node_modules/tailwindcss/node_modules/glob-parent</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">VGhlIElTQyBMaWNlbnNlCgpDb3B5cmlnaHQgKGMpIDIwMTUsIDIwMTkgRWxhbiBTaGFua2VyLCAyMDIxIEJsYWluZSBCdWJsaXR6IDxibGFpbmUuYnVibGl0ekBnbWFpbC5jb20+LCBFcmljIFNjaG9mZnN0YWxsIDx5b0Bjb250cmEuaW8+IGFuZCBvdGhlciBjb250cmlidXRvcnMKClBlcm1pc3Npb24gdG8gdXNlLCBjb3B5LCBtb2RpZnksIGFuZC9vciBkaXN0cmlidXRlIHRoaXMgc29mdHdhcmUgZm9yIGFueQpwdXJwb3NlIHdpdGggb3Igd2l0aG91dCBmZWUgaXMgaGVyZWJ5IGdyYW50ZWQsIHByb3ZpZGVkIHRoYXQgdGhlIGFib3ZlCmNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2UgYXBwZWFyIGluIGFsbCBjb3BpZXMuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiBBTkQgVEhFIEFVVEhPUiBESVNDTEFJTVMgQUxMIFdBUlJBTlRJRVMKV0lUSCBSRUdBUkQgVE8gVEhJUyBTT0ZUV0FSRSBJTkNMVURJTkcgQUxMIElNUExJRUQgV0FSUkFOVElFUyBPRgpNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1IgQkUgTElBQkxFIEZPUgpBTlkgU1BFQ0lBTCwgRElSRUNULCBJTkRJUkVDVCwgT1IgQ09OU0VRVUVOVElBTCBEQU1BR0VTIE9SIEFOWSBEQU1BR0VTCldIQVRTT0VWRVIgUkVTVUxUSU5HIEZST00gTE9TUyBPRiBVU0UsIERBVEEgT1IgUFJPRklUUywgV0hFVEhFUiBJTiBBTgpBQ1RJT04gT0YgQ09OVFJBQ1QsIE5FR0xJR0VOQ0UgT1IgT1RIRVIgVE9SVElPVVMgQUNUSU9OLCBBUklTSU5HIE9VVCBPRiBPUgpJTiBDT05ORUNUSU9OIFdJVEggVEhFIFVTRSBPUiBQRVJGT1JNQU5DRSBPRiBUSElTIFNPRlRXQVJFLgo=</text>
              </license>
            </licenses>
          </evidence>
        </component>
        <component type="library" bom-ref="openbb-platform@1.0.0|tailwindcss@3.4.18|postcss-load-config@6.0.1">
          <author>Michael Ciniawky</author>
          <name>postcss-load-config</name>
          <version>6.0.1</version>
          <description>Autoload Config for PostCSS</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/postcss-load-config@6.0.1</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/postcss/postcss-load-config.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/postcss/postcss-load-config#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/postcss/postcss-load-config/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/postcss-load-config/-/postcss-load-config-6.0.1.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">a0fb53338a1eacbf945e6c7ef77cad65537cd91ae563fc0f515f08783c45af32235ce2c5d6937e12628f2dbb9bbca1d3d870b6d315ec0801f667e08a57a3b3fe</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:path">node_modules/tailwindcss/node_modules/postcss-load-config</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCgpDb3B5cmlnaHQgTWljaGFlbCBDaW5pYXdza3kgPG1pY2hhZWwuY2luaWF3c2t5QGdtYWlsLmNvbT4KClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YKdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4KdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0bwp1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZgp0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sCnN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUwpGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IKQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSCklOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOCkNPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCg==</text>
              </license>
            </licenses>
          </evidence>
        </component>
        <component type="library" bom-ref="openbb-platform@1.0.0|tailwindcss@3.4.18|resolve@1.22.10">
          <author>James Halliday</author>
          <name>resolve</name>
          <version>1.22.10</version>
          <description>resolve like require.resolve() on behalf of files asynchronously and synchronously</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/resolve@1.22.10</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git://github.com/browserify/resolve.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/browserify/resolve#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/browserify/resolve/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/resolve/-/resolve-1.22.10.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">34f472fbf9dc20c78395302cbaac0a2227deae26b085e7c526d90d496d2a64912a3046fea81b7fefb07f8c679e7a4f85d2e39e374e420dae875db6c882d557e3</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:path">node_modules/tailwindcss/node_modules/resolve</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxMiBKYW1lcyBIYWxsaWRheQoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgVGFpbHdpbmQgTGFicywgSW5jLgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|taurpc@1.8.1">
      <author>MatsDK</author>
      <name>taurpc</name>
      <version>1.8.1</version>
      <licenses>
        <license acknowledgement="declared">
          <id>ISC</id>
        </license>
      </licenses>
      <purl>pkg:npm/taurpc@1.8.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/MatsDK/TauRPC.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/MatsDK/TauRPC#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/MatsDK/TauRPC/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/taurpc/-/taurpc-1.8.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">a9f4757a48570298db9d602ac84e6aa436bfa0c98a0708cd343baa8d89fbb0ef82848e6ac10e09fdf4bed347552c4dc8d256d90e2cf263c39b485073dcc45ead</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/taurpc</property>
      </properties>
      <evidence/>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|tiny-invariant@1.3.3">
      <author>Alex Reardon</author>
      <name>tiny-invariant</name>
      <version>1.3.3</version>
      <description>A tiny invariant function</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/tiny-invariant@1.3.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/alexreardon/tiny-invariant.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/alexreardon/tiny-invariant#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/alexreardon/tiny-invariant/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/tiny-invariant/-/tiny-invariant-1.3.3.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">f856c13c4d68f50018bef89abbfa82e5213771ac36d6adf192f58a06d8dae6f82a3962071c9de2a1aab554f7e7fd2cea72dcf66d4fe861e29df7fcf904bf8f56</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/tiny-invariant</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxOSBBbGV4YW5kZXIgUmVhcmRvbgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|typescript-eslint@8.46.0">
      <name>typescript-eslint</name>
      <version>8.46.0</version>
      <description>Tooling which enables you to use TypeScript with ESLint</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/typescript-eslint@8.46.0#packages/typescript-eslint</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/typescript-eslint/typescript-eslint.git#packages/typescript-eslint</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://typescript-eslint.io/packages/typescript-eslint</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/typescript-eslint/typescript-eslint/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/typescript-eslint/-/typescript-eslint-8.46.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">ebe66b07acb66d3d835f72be41df6f9fb38538947ec522c38fe030fcddf307052ddbbb93c36b30d93136f94718d518b205991a19b4e4560f5249d3cd506e9a53</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/typescript-eslint</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxOSB0eXBlc2NyaXB0LWVzbGludCBhbmQgb3RoZXIgY29udHJpYnV0b3JzCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|typescript@5.9.3">
      <author>Microsoft Corp.</author>
      <name>typescript</name>
      <version>5.9.3</version>
      <description>TypeScript is a language for application scale JavaScript development</description>
      <licenses>
        <license acknowledgement="declared">
          <id>Apache-2.0</id>
        </license>
      </licenses>
      <purl>pkg:npm/typescript@5.9.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/microsoft/TypeScript.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://www.typescriptlang.org/</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/microsoft/TypeScript/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/typescript/-/typescript-5.9.3.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">8e5d6f6733c38a72ebf5e52ddc9feded5e8580d130f508ef04f772b33f4a7d00c3e357d0ac2d98e2f290762694a454f86d795bd511e12e9a7cc2d9ba3394e04b</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/typescript</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE.txt</name>
            <text content-type="text/plain" encoding="base64">QXBhY2hlIExpY2Vuc2UNCg0KVmVyc2lvbiAyLjAsIEphbnVhcnkgMjAwNA0KDQpodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvIA0KDQpURVJNUyBBTkQgQ09ORElUSU9OUyBGT1IgVVNFLCBSRVBST0RVQ1RJT04sIEFORCBESVNUUklCVVRJT04NCg0KMS4gRGVmaW5pdGlvbnMuDQoNCiJMaWNlbnNlIiBzaGFsbCBtZWFuIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBmb3IgdXNlLCByZXByb2R1Y3Rpb24sIGFuZCBkaXN0cmlidXRpb24gYXMgZGVmaW5lZCBieSBTZWN0aW9ucyAxIHRocm91Z2ggOSBvZiB0aGlzIGRvY3VtZW50Lg0KDQoiTGljZW5zb3IiIHNoYWxsIG1lYW4gdGhlIGNvcHlyaWdodCBvd25lciBvciBlbnRpdHkgYXV0aG9yaXplZCBieSB0aGUgY29weXJpZ2h0IG93bmVyIHRoYXQgaXMgZ3JhbnRpbmcgdGhlIExpY2Vuc2UuDQoNCiJMZWdhbCBFbnRpdHkiIHNoYWxsIG1lYW4gdGhlIHVuaW9uIG9mIHRoZSBhY3RpbmcgZW50aXR5IGFuZCBhbGwgb3RoZXIgZW50aXRpZXMgdGhhdCBjb250cm9sLCBhcmUgY29udHJvbGxlZCBieSwgb3IgYXJlIHVuZGVyIGNvbW1vbiBjb250cm9sIHdpdGggdGhhdCBlbnRpdHkuIEZvciB0aGUgcHVycG9zZXMgb2YgdGhpcyBkZWZpbml0aW9uLCAiY29udHJvbCIgbWVhbnMgKGkpIHRoZSBwb3dlciwgZGlyZWN0IG9yIGluZGlyZWN0LCB0byBjYXVzZSB0aGUgZGlyZWN0aW9uIG9yIG1hbmFnZW1lbnQgb2Ygc3VjaCBlbnRpdHksIHdoZXRoZXIgYnkgY29udHJhY3Qgb3Igb3RoZXJ3aXNlLCBvciAoaWkpIG93bmVyc2hpcCBvZiBmaWZ0eSBwZXJjZW50ICg1MCUpIG9yIG1vcmUgb2YgdGhlIG91dHN0YW5kaW5nIHNoYXJlcywgb3IgKGlpaSkgYmVuZWZpY2lhbCBvd25lcnNoaXAgb2Ygc3VjaCBlbnRpdHkuDQoNCiJZb3UiIChvciAiWW91ciIpIHNoYWxsIG1lYW4gYW4gaW5kaXZpZHVhbCBvciBMZWdhbCBFbnRpdHkgZXhlcmNpc2luZyBwZXJtaXNzaW9ucyBncmFudGVkIGJ5IHRoaXMgTGljZW5zZS4NCg0KIlNvdXJjZSIgZm9ybSBzaGFsbCBtZWFuIHRoZSBwcmVmZXJyZWQgZm9ybSBmb3IgbWFraW5nIG1vZGlmaWNhdGlvbnMsIGluY2x1ZGluZyBidXQgbm90IGxpbWl0ZWQgdG8gc29mdHdhcmUgc291cmNlIGNvZGUsIGRvY3VtZW50YXRpb24gc291cmNlLCBhbmQgY29uZmlndXJhdGlvbiBmaWxlcy4NCg0KIk9iamVjdCIgZm9ybSBzaGFsbCBtZWFuIGFueSBmb3JtIHJlc3VsdGluZyBmcm9tIG1lY2hhbmljYWwgdHJhbnNmb3JtYXRpb24gb3IgdHJhbnNsYXRpb24gb2YgYSBTb3VyY2UgZm9ybSwgaW5jbHVkaW5nIGJ1dCBub3QgbGltaXRlZCB0byBjb21waWxlZCBvYmplY3QgY29kZSwgZ2VuZXJhdGVkIGRvY3VtZW50YXRpb24sIGFuZCBjb252ZXJzaW9ucyB0byBvdGhlciBtZWRpYSB0eXBlcy4NCg0KIldvcmsiIHNoYWxsIG1lYW4gdGhlIHdvcmsgb2YgYXV0aG9yc2hpcCwgd2hldGhlciBpbiBTb3VyY2Ugb3IgT2JqZWN0IGZvcm0sIG1hZGUgYXZhaWxhYmxlIHVuZGVyIHRoZSBMaWNlbnNlLCBhcyBpbmRpY2F0ZWQgYnkgYSBjb3B5cmlnaHQgbm90aWNlIHRoYXQgaXMgaW5jbHVkZWQgaW4gb3IgYXR0YWNoZWQgdG8gdGhlIHdvcmsgKGFuIGV4YW1wbGUgaXMgcHJvdmlkZWQgaW4gdGhlIEFwcGVuZGl4IGJlbG93KS4NCg0KIkRlcml2YXRpdmUgV29ya3MiIHNoYWxsIG1lYW4gYW55IHdvcmssIHdoZXRoZXIgaW4gU291cmNlIG9yIE9iamVjdCBmb3JtLCB0aGF0IGlzIGJhc2VkIG9uIChvciBkZXJpdmVkIGZyb20pIHRoZSBXb3JrIGFuZCBmb3Igd2hpY2ggdGhlIGVkaXRvcmlhbCByZXZpc2lvbnMsIGFubm90YXRpb25zLCBlbGFib3JhdGlvbnMsIG9yIG90aGVyIG1vZGlmaWNhdGlvbnMgcmVwcmVzZW50LCBhcyBhIHdob2xlLCBhbiBvcmlnaW5hbCB3b3JrIG9mIGF1dGhvcnNoaXAuIEZvciB0aGUgcHVycG9zZXMgb2YgdGhpcyBMaWNlbnNlLCBEZXJpdmF0aXZlIFdvcmtzIHNoYWxsIG5vdCBpbmNsdWRlIHdvcmtzIHRoYXQgcmVtYWluIHNlcGFyYWJsZSBmcm9tLCBvciBtZXJlbHkgbGluayAob3IgYmluZCBieSBuYW1lKSB0byB0aGUgaW50ZXJmYWNlcyBvZiwgdGhlIFdvcmsgYW5kIERlcml2YXRpdmUgV29ya3MgdGhlcmVvZi4NCg0KIkNvbnRyaWJ1dGlvbiIgc2hhbGwgbWVhbiBhbnkgd29yayBvZiBhdXRob3JzaGlwLCBpbmNsdWRpbmcgdGhlIG9yaWdpbmFsIHZlcnNpb24gb2YgdGhlIFdvcmsgYW5kIGFueSBtb2RpZmljYXRpb25zIG9yIGFkZGl0aW9ucyB0byB0aGF0IFdvcmsgb3IgRGVyaXZhdGl2ZSBXb3JrcyB0aGVyZW9mLCB0aGF0IGlzIGludGVudGlvbmFsbHkgc3VibWl0dGVkIHRvIExpY2Vuc29yIGZvciBpbmNsdXNpb24gaW4gdGhlIFdvcmsgYnkgdGhlIGNvcHlyaWdodCBvd25lciBvciBieSBhbiBpbmRpdmlkdWFsIG9yIExlZ2FsIEVudGl0eSBhdXRob3JpemVkIHRvIHN1Ym1pdCBvbiBiZWhhbGYgb2YgdGhlIGNvcHlyaWdodCBvd25lci4gRm9yIHRoZSBwdXJwb3NlcyBvZiB0aGlzIGRlZmluaXRpb24sICJzdWJtaXR0ZWQiIG1lYW5zIGFueSBmb3JtIG9mIGVsZWN0cm9uaWMsIHZlcmJhbCwgb3Igd3JpdHRlbiBjb21tdW5pY2F0aW9uIHNlbnQgdG8gdGhlIExpY2Vuc29yIG9yIGl0cyByZXByZXNlbnRhdGl2ZXMsIGluY2x1ZGluZyBidXQgbm90IGxpbWl0ZWQgdG8gY29tbXVuaWNhdGlvbiBvbiBlbGVjdHJvbmljIG1haWxpbmcgbGlzdHMsIHNvdXJjZSBjb2RlIGNvbnRyb2wgc3lzdGVtcywgYW5kIGlzc3VlIHRyYWNraW5nIHN5c3RlbXMgdGhhdCBhcmUgbWFuYWdlZCBieSwgb3Igb24gYmVoYWxmIG9mLCB0aGUgTGljZW5zb3IgZm9yIHRoZSBwdXJwb3NlIG9mIGRpc2N1c3NpbmcgYW5kIGltcHJvdmluZyB0aGUgV29yaywgYnV0IGV4Y2x1ZGluZyBjb21tdW5pY2F0aW9uIHRoYXQgaXMgY29uc3BpY3VvdXNseSBtYXJrZWQgb3Igb3RoZXJ3aXNlIGRlc2lnbmF0ZWQgaW4gd3JpdGluZyBieSB0aGUgY29weXJpZ2h0IG93bmVyIGFzICJOb3QgYSBDb250cmlidXRpb24uIg0KDQoiQ29udHJpYnV0b3IiIHNoYWxsIG1lYW4gTGljZW5zb3IgYW5kIGFueSBpbmRpdmlkdWFsIG9yIExlZ2FsIEVudGl0eSBvbiBiZWhhbGYgb2Ygd2hvbSBhIENvbnRyaWJ1dGlvbiBoYXMgYmVlbiByZWNlaXZlZCBieSBMaWNlbnNvciBhbmQgc3Vic2VxdWVudGx5IGluY29ycG9yYXRlZCB3aXRoaW4gdGhlIFdvcmsuDQoNCjIuIEdyYW50IG9mIENvcHlyaWdodCBMaWNlbnNlLiBTdWJqZWN0IHRvIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZiB0aGlzIExpY2Vuc2UsIGVhY2ggQ29udHJpYnV0b3IgaGVyZWJ5IGdyYW50cyB0byBZb3UgYSBwZXJwZXR1YWwsIHdvcmxkd2lkZSwgbm9uLWV4Y2x1c2l2ZSwgbm8tY2hhcmdlLCByb3lhbHR5LWZyZWUsIGlycmV2b2NhYmxlIGNvcHlyaWdodCBsaWNlbnNlIHRvIHJlcHJvZHVjZSwgcHJlcGFyZSBEZXJpdmF0aXZlIFdvcmtzIG9mLCBwdWJsaWNseSBkaXNwbGF5LCBwdWJsaWNseSBwZXJmb3JtLCBzdWJsaWNlbnNlLCBhbmQgZGlzdHJpYnV0ZSB0aGUgV29yayBhbmQgc3VjaCBEZXJpdmF0aXZlIFdvcmtzIGluIFNvdXJjZSBvciBPYmplY3QgZm9ybS4NCg0KMy4gR3JhbnQgb2YgUGF0ZW50IExpY2Vuc2UuIFN1YmplY3QgdG8gdGhlIHRlcm1zIGFuZCBjb25kaXRpb25zIG9mIHRoaXMgTGljZW5zZSwgZWFjaCBDb250cmlidXRvciBoZXJlYnkgZ3JhbnRzIHRvIFlvdSBhIHBlcnBldHVhbCwgd29ybGR3aWRlLCBub24tZXhjbHVzaXZlLCBuby1jaGFyZ2UsIHJveWFsdHktZnJlZSwgaXJyZXZvY2FibGUgKGV4Y2VwdCBhcyBzdGF0ZWQgaW4gdGhpcyBzZWN0aW9uKSBwYXRlbnQgbGljZW5zZSB0byBtYWtlLCBoYXZlIG1hZGUsIHVzZSwgb2ZmZXIgdG8gc2VsbCwgc2VsbCwgaW1wb3J0LCBhbmQgb3RoZXJ3aXNlIHRyYW5zZmVyIHRoZSBXb3JrLCB3aGVyZSBzdWNoIGxpY2Vuc2UgYXBwbGllcyBvbmx5IHRvIHRob3NlIHBhdGVudCBjbGFpbXMgbGljZW5zYWJsZSBieSBzdWNoIENvbnRyaWJ1dG9yIHRoYXQgYXJlIG5lY2Vzc2FyaWx5IGluZnJpbmdlZCBieSB0aGVpciBDb250cmlidXRpb24ocykgYWxvbmUgb3IgYnkgY29tYmluYXRpb24gb2YgdGhlaXIgQ29udHJpYnV0aW9uKHMpIHdpdGggdGhlIFdvcmsgdG8gd2hpY2ggc3VjaCBDb250cmlidXRpb24ocykgd2FzIHN1Ym1pdHRlZC4gSWYgWW91IGluc3RpdHV0ZSBwYXRlbnQgbGl0aWdhdGlvbiBhZ2FpbnN0IGFueSBlbnRpdHkgKGluY2x1ZGluZyBhIGNyb3NzLWNsYWltIG9yIGNvdW50ZXJjbGFpbSBpbiBhIGxhd3N1aXQpIGFsbGVnaW5nIHRoYXQgdGhlIFdvcmsgb3IgYSBDb250cmlidXRpb24gaW5jb3Jwb3JhdGVkIHdpdGhpbiB0aGUgV29yayBjb25zdGl0dXRlcyBkaXJlY3Qgb3IgY29udHJpYnV0b3J5IHBhdGVudCBpbmZyaW5nZW1lbnQsIHRoZW4gYW55IHBhdGVudCBsaWNlbnNlcyBncmFudGVkIHRvIFlvdSB1bmRlciB0aGlzIExpY2Vuc2UgZm9yIHRoYXQgV29yayBzaGFsbCB0ZXJtaW5hdGUgYXMgb2YgdGhlIGRhdGUgc3VjaCBsaXRpZ2F0aW9uIGlzIGZpbGVkLg0KDQo0LiBSZWRpc3RyaWJ1dGlvbi4gWW91IG1heSByZXByb2R1Y2UgYW5kIGRpc3RyaWJ1dGUgY29waWVzIG9mIHRoZSBXb3JrIG9yIERlcml2YXRpdmUgV29ya3MgdGhlcmVvZiBpbiBhbnkgbWVkaXVtLCB3aXRoIG9yIHdpdGhvdXQgbW9kaWZpY2F0aW9ucywgYW5kIGluIFNvdXJjZSBvciBPYmplY3QgZm9ybSwgcHJvdmlkZWQgdGhhdCBZb3UgbWVldCB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6DQoNCllvdSBtdXN0IGdpdmUgYW55IG90aGVyIHJlY2lwaWVudHMgb2YgdGhlIFdvcmsgb3IgRGVyaXZhdGl2ZSBXb3JrcyBhIGNvcHkgb2YgdGhpcyBMaWNlbnNlOyBhbmQNCg0KWW91IG11c3QgY2F1c2UgYW55IG1vZGlmaWVkIGZpbGVzIHRvIGNhcnJ5IHByb21pbmVudCBub3RpY2VzIHN0YXRpbmcgdGhhdCBZb3UgY2hhbmdlZCB0aGUgZmlsZXM7IGFuZA0KDQpZb3UgbXVzdCByZXRhaW4sIGluIHRoZSBTb3VyY2UgZm9ybSBvZiBhbnkgRGVyaXZhdGl2ZSBXb3JrcyB0aGF0IFlvdSBkaXN0cmlidXRlLCBhbGwgY29weXJpZ2h0LCBwYXRlbnQsIHRyYWRlbWFyaywgYW5kIGF0dHJpYnV0aW9uIG5vdGljZXMgZnJvbSB0aGUgU291cmNlIGZvcm0gb2YgdGhlIFdvcmssIGV4Y2x1ZGluZyB0aG9zZSBub3RpY2VzIHRoYXQgZG8gbm90IHBlcnRhaW4gdG8gYW55IHBhcnQgb2YgdGhlIERlcml2YXRpdmUgV29ya3M7IGFuZA0KDQpJZiB0aGUgV29yayBpbmNsdWRlcyBhICJOT1RJQ0UiIHRleHQgZmlsZSBhcyBwYXJ0IG9mIGl0cyBkaXN0cmlidXRpb24sIHRoZW4gYW55IERlcml2YXRpdmUgV29ya3MgdGhhdCBZb3UgZGlzdHJpYnV0ZSBtdXN0IGluY2x1ZGUgYSByZWFkYWJsZSBjb3B5IG9mIHRoZSBhdHRyaWJ1dGlvbiBub3RpY2VzIGNvbnRhaW5lZCB3aXRoaW4gc3VjaCBOT1RJQ0UgZmlsZSwgZXhjbHVkaW5nIHRob3NlIG5vdGljZXMgdGhhdCBkbyBub3QgcGVydGFpbiB0byBhbnkgcGFydCBvZiB0aGUgRGVyaXZhdGl2ZSBXb3JrcywgaW4gYXQgbGVhc3Qgb25lIG9mIHRoZSBmb2xsb3dpbmcgcGxhY2VzOiB3aXRoaW4gYSBOT1RJQ0UgdGV4dCBmaWxlIGRpc3RyaWJ1dGVkIGFzIHBhcnQgb2YgdGhlIERlcml2YXRpdmUgV29ya3M7IHdpdGhpbiB0aGUgU291cmNlIGZvcm0gb3IgZG9jdW1lbnRhdGlvbiwgaWYgcHJvdmlkZWQgYWxvbmcgd2l0aCB0aGUgRGVyaXZhdGl2ZSBXb3Jrczsgb3IsIHdpdGhpbiBhIGRpc3BsYXkgZ2VuZXJhdGVkIGJ5IHRoZSBEZXJpdmF0aXZlIFdvcmtzLCBpZiBhbmQgd2hlcmV2ZXIgc3VjaCB0aGlyZC1wYXJ0eSBub3RpY2VzIG5vcm1hbGx5IGFwcGVhci4gVGhlIGNvbnRlbnRzIG9mIHRoZSBOT1RJQ0UgZmlsZSBhcmUgZm9yIGluZm9ybWF0aW9uYWwgcHVycG9zZXMgb25seSBhbmQgZG8gbm90IG1vZGlmeSB0aGUgTGljZW5zZS4gWW91IG1heSBhZGQgWW91ciBvd24gYXR0cmlidXRpb24gbm90aWNlcyB3aXRoaW4gRGVyaXZhdGl2ZSBXb3JrcyB0aGF0IFlvdSBkaXN0cmlidXRlLCBhbG9uZ3NpZGUgb3IgYXMgYW4gYWRkZW5kdW0gdG8gdGhlIE5PVElDRSB0ZXh0IGZyb20gdGhlIFdvcmssIHByb3ZpZGVkIHRoYXQgc3VjaCBhZGRpdGlvbmFsIGF0dHJpYnV0aW9uIG5vdGljZXMgY2Fubm90IGJlIGNvbnN0cnVlZCBhcyBtb2RpZnlpbmcgdGhlIExpY2Vuc2UuIFlvdSBtYXkgYWRkIFlvdXIgb3duIGNvcHlyaWdodCBzdGF0ZW1lbnQgdG8gWW91ciBtb2RpZmljYXRpb25zIGFuZCBtYXkgcHJvdmlkZSBhZGRpdGlvbmFsIG9yIGRpZmZlcmVudCBsaWNlbnNlIHRlcm1zIGFuZCBjb25kaXRpb25zIGZvciB1c2UsIHJlcHJvZHVjdGlvbiwgb3IgZGlzdHJpYnV0aW9uIG9mIFlvdXIgbW9kaWZpY2F0aW9ucywgb3IgZm9yIGFueSBzdWNoIERlcml2YXRpdmUgV29ya3MgYXMgYSB3aG9sZSwgcHJvdmlkZWQgWW91ciB1c2UsIHJlcHJvZHVjdGlvbiwgYW5kIGRpc3RyaWJ1dGlvbiBvZiB0aGUgV29yayBvdGhlcndpc2UgY29tcGxpZXMgd2l0aCB0aGUgY29uZGl0aW9ucyBzdGF0ZWQgaW4gdGhpcyBMaWNlbnNlLg0KDQo1LiBTdWJtaXNzaW9uIG9mIENvbnRyaWJ1dGlvbnMuIFVubGVzcyBZb3UgZXhwbGljaXRseSBzdGF0ZSBvdGhlcndpc2UsIGFueSBDb250cmlidXRpb24gaW50ZW50aW9uYWxseSBzdWJtaXR0ZWQgZm9yIGluY2x1c2lvbiBpbiB0aGUgV29yayBieSBZb3UgdG8gdGhlIExpY2Vuc29yIHNoYWxsIGJlIHVuZGVyIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZiB0aGlzIExpY2Vuc2UsIHdpdGhvdXQgYW55IGFkZGl0aW9uYWwgdGVybXMgb3IgY29uZGl0aW9ucy4gTm90d2l0aHN0YW5kaW5nIHRoZSBhYm92ZSwgbm90aGluZyBoZXJlaW4gc2hhbGwgc3VwZXJzZWRlIG9yIG1vZGlmeSB0aGUgdGVybXMgb2YgYW55IHNlcGFyYXRlIGxpY2Vuc2UgYWdyZWVtZW50IHlvdSBtYXkgaGF2ZSBleGVjdXRlZCB3aXRoIExpY2Vuc29yIHJlZ2FyZGluZyBzdWNoIENvbnRyaWJ1dGlvbnMuDQoNCjYuIFRyYWRlbWFya3MuIFRoaXMgTGljZW5zZSBkb2VzIG5vdCBncmFudCBwZXJtaXNzaW9uIHRvIHVzZSB0aGUgdHJhZGUgbmFtZXMsIHRyYWRlbWFya3MsIHNlcnZpY2UgbWFya3MsIG9yIHByb2R1Y3QgbmFtZXMgb2YgdGhlIExpY2Vuc29yLCBleGNlcHQgYXMgcmVxdWlyZWQgZm9yIHJlYXNvbmFibGUgYW5kIGN1c3RvbWFyeSB1c2UgaW4gZGVzY3JpYmluZyB0aGUgb3JpZ2luIG9mIHRoZSBXb3JrIGFuZCByZXByb2R1Y2luZyB0aGUgY29udGVudCBvZiB0aGUgTk9USUNFIGZpbGUuDQoNCjcuIERpc2NsYWltZXIgb2YgV2FycmFudHkuIFVubGVzcyByZXF1aXJlZCBieSBhcHBsaWNhYmxlIGxhdyBvciBhZ3JlZWQgdG8gaW4gd3JpdGluZywgTGljZW5zb3IgcHJvdmlkZXMgdGhlIFdvcmsgKGFuZCBlYWNoIENvbnRyaWJ1dG9yIHByb3ZpZGVzIGl0cyBDb250cmlidXRpb25zKSBvbiBhbiAiQVMgSVMiIEJBU0lTLCBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZCwgaW5jbHVkaW5nLCB3aXRob3V0IGxpbWl0YXRpb24sIGFueSB3YXJyYW50aWVzIG9yIGNvbmRpdGlvbnMgb2YgVElUTEUsIE5PTi1JTkZSSU5HRU1FTlQsIE1FUkNIQU5UQUJJTElUWSwgb3IgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UuIFlvdSBhcmUgc29sZWx5IHJlc3BvbnNpYmxlIGZvciBkZXRlcm1pbmluZyB0aGUgYXBwcm9wcmlhdGVuZXNzIG9mIHVzaW5nIG9yIHJlZGlzdHJpYnV0aW5nIHRoZSBXb3JrIGFuZCBhc3N1bWUgYW55IHJpc2tzIGFzc29jaWF0ZWQgd2l0aCBZb3VyIGV4ZXJjaXNlIG9mIHBlcm1pc3Npb25zIHVuZGVyIHRoaXMgTGljZW5zZS4NCg0KOC4gTGltaXRhdGlvbiBvZiBMaWFiaWxpdHkuIEluIG5vIGV2ZW50IGFuZCB1bmRlciBubyBsZWdhbCB0aGVvcnksIHdoZXRoZXIgaW4gdG9ydCAoaW5jbHVkaW5nIG5lZ2xpZ2VuY2UpLCBjb250cmFjdCwgb3Igb3RoZXJ3aXNlLCB1bmxlc3MgcmVxdWlyZWQgYnkgYXBwbGljYWJsZSBsYXcgKHN1Y2ggYXMgZGVsaWJlcmF0ZSBhbmQgZ3Jvc3NseSBuZWdsaWdlbnQgYWN0cykgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsIHNoYWxsIGFueSBDb250cmlidXRvciBiZSBsaWFibGUgdG8gWW91IGZvciBkYW1hZ2VzLCBpbmNsdWRpbmcgYW55IGRpcmVjdCwgaW5kaXJlY3QsIHNwZWNpYWwsIGluY2lkZW50YWwsIG9yIGNvbnNlcXVlbnRpYWwgZGFtYWdlcyBvZiBhbnkgY2hhcmFjdGVyIGFyaXNpbmcgYXMgYSByZXN1bHQgb2YgdGhpcyBMaWNlbnNlIG9yIG91dCBvZiB0aGUgdXNlIG9yIGluYWJpbGl0eSB0byB1c2UgdGhlIFdvcmsgKGluY2x1ZGluZyBidXQgbm90IGxpbWl0ZWQgdG8gZGFtYWdlcyBmb3IgbG9zcyBvZiBnb29kd2lsbCwgd29yayBzdG9wcGFnZSwgY29tcHV0ZXIgZmFpbHVyZSBvciBtYWxmdW5jdGlvbiwgb3IgYW55IGFuZCBhbGwgb3RoZXIgY29tbWVyY2lhbCBkYW1hZ2VzIG9yIGxvc3NlcyksIGV2ZW4gaWYgc3VjaCBDb250cmlidXRvciBoYXMgYmVlbiBhZHZpc2VkIG9mIHRoZSBwb3NzaWJpbGl0eSBvZiBzdWNoIGRhbWFnZXMuDQoNCjkuIEFjY2VwdGluZyBXYXJyYW50eSBvciBBZGRpdGlvbmFsIExpYWJpbGl0eS4gV2hpbGUgcmVkaXN0cmlidXRpbmcgdGhlIFdvcmsgb3IgRGVyaXZhdGl2ZSBXb3JrcyB0aGVyZW9mLCBZb3UgbWF5IGNob29zZSB0byBvZmZlciwgYW5kIGNoYXJnZSBhIGZlZSBmb3IsIGFjY2VwdGFuY2Ugb2Ygc3VwcG9ydCwgd2FycmFudHksIGluZGVtbml0eSwgb3Igb3RoZXIgbGlhYmlsaXR5IG9ibGlnYXRpb25zIGFuZC9vciByaWdodHMgY29uc2lzdGVudCB3aXRoIHRoaXMgTGljZW5zZS4gSG93ZXZlciwgaW4gYWNjZXB0aW5nIHN1Y2ggb2JsaWdhdGlvbnMsIFlvdSBtYXkgYWN0IG9ubHkgb24gWW91ciBvd24gYmVoYWxmIGFuZCBvbiBZb3VyIHNvbGUgcmVzcG9uc2liaWxpdHksIG5vdCBvbiBiZWhhbGYgb2YgYW55IG90aGVyIENvbnRyaWJ1dG9yLCBhbmQgb25seSBpZiBZb3UgYWdyZWUgdG8gaW5kZW1uaWZ5LCBkZWZlbmQsIGFuZCBob2xkIGVhY2ggQ29udHJpYnV0b3IgaGFybWxlc3MgZm9yIGFueSBsaWFiaWxpdHkgaW5jdXJyZWQgYnksIG9yIGNsYWltcyBhc3NlcnRlZCBhZ2FpbnN0LCBzdWNoIENvbnRyaWJ1dG9yIGJ5IHJlYXNvbiBvZiB5b3VyIGFjY2VwdGluZyBhbnkgc3VjaCB3YXJyYW50eSBvciBhZGRpdGlvbmFsIGxpYWJpbGl0eS4NCg0KRU5EIE9GIFRFUk1TIEFORCBDT05ESVRJT05TDQo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|vite-plugin-static-copy@3.1.4">
      <author>sapphi-red</author>
      <name>vite-plugin-static-copy</name>
      <version>3.1.4</version>
      <description>rollup-plugin-copy for vite with dev server support.</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/vite-plugin-static-copy@3.1.4</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/sapphi-red/vite-plugin-static-copy.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/sapphi-red/vite-plugin-static-copy#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/sapphi-red/vite-plugin-static-copy/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/vite-plugin-static-copy/-/vite-plugin-static-copy-3.1.4.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">8829abe064b0e1e4a7681f86f337367f87714ae0e36e48f0a6e04b2c6bd0611f485bbae70f37ed9d48ce1f9a7845847e7781ac881a9746fcee161b396e7cd5cb</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/vite-plugin-static-copy</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMSBzYXBwaGktcmVkCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|vite-plugin-svgr@4.5.0">
      <author>Rongjian Zhang</author>
      <name>vite-plugin-svgr</name>
      <version>4.5.0</version>
      <description>Vite plugin to transform SVGs into React components</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/vite-plugin-svgr@4.5.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/pd4d10/vite-plugin-svgr.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/pd4d10/vite-plugin-svgr#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/pd4d10/vite-plugin-svgr/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/vite-plugin-svgr/-/vite-plugin-svgr-4.5.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">5beba84a999591298d3863d2b03096556fc30c0caffbd7daa7d0195c1bd6890aab6e8274f23daf874b45c530ff2e3c2ac00777c984952609b9e12ff51a16dd9c</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/vite-plugin-svgr</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMSBSb25namlhbiBaaGFuZwoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|vite@7.1.11">
      <author>Evan You</author>
      <name>vite</name>
      <version>7.1.11</version>
      <description>Native-ESM powered web dev build tool</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/vite@7.1.11#packages/vite</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/vitejs/vite.git#packages/vite</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://vite.dev</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/vitejs/vite/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/vite/-/vite-7.1.11.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">bb37319d20d58c0a291148e58e45a1f0422b83ab65ceb8c551f31c475115b110c6c1ffdc71e7f4a903d1c8ead13b086b4c3680a6e7aafa36be28b3e5cd1ff376</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/vite</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|vite@7.1.11|fdir@6.5.0">
          <author>thecodrr</author>
          <name>fdir</name>
          <version>6.5.0</version>
          <description>The fastest directory crawler &amp; globbing alternative to glob, fast-glob, &amp; tiny-glob. Crawls 1m files in &lt; 1s</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/fdir@6.5.0</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/thecodrr/fdir.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/thecodrr/fdir#readme</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/thecodrr/fdir/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">b486d8b596ee70eb340511aa3c992c84951874bf920c7edd54cf208f2f84469dd60148cb105244fb4da46a7c87b708d63a7c2b298062c0098cd29e242c90275e</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:path">node_modules/vite/node_modules/fdir</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">Q29weXJpZ2h0IDIwMjMgQWJkdWxsYWggQXR0YQoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4K</text>
              </license>
            </licenses>
          </evidence>
        </component>
        <component type="library" bom-ref="openbb-platform@1.0.0|vite@7.1.11|picomatch@4.0.3">
          <author>Jon Schlinkert</author>
          <name>picomatch</name>
          <version>4.0.3</version>
          <description>Blazing fast and accurate glob matcher written in JavaScript, with no dependencies and full support for standard and extended Bash glob features, including braces, extglobs, POSIX brackets, and regular expressions.</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/picomatch@4.0.3</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/micromatch/picomatch.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/micromatch/picomatch</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/micromatch/picomatch/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">e604e680463fb2a2ba8055cb22c40d1f5f6559be1e6cf0cb03849d2cfeddb169085c75a51baea83ee56f5d21853e9a58673f190d9ab475862b6c77c109551bd5</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:path">node_modules/vite/node_modules/picomatch</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCgpDb3B5cmlnaHQgKGMpIDIwMTctcHJlc2VudCwgSm9uIFNjaGxpbmtlcnQuCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCmFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KVEhFIFNPRlRXQVJFLgo=</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE.md</name>
            <text content-type="text/markdown" encoding="base64">IyBWaXRlIGNvcmUgbGljZW5zZQpWaXRlIGlzIHJlbGVhc2VkIHVuZGVyIHRoZSBNSVQgbGljZW5zZToKCk1JVCBMaWNlbnNlCgpDb3B5cmlnaHQgKGMpIDIwMTktcHJlc2VudCwgVm9pZFplcm8gSW5jLiBhbmQgVml0ZSBjb250cmlidXRvcnMKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCgojIExpY2Vuc2VzIG9mIGJ1bmRsZWQgZGVwZW5kZW5jaWVzClRoZSBwdWJsaXNoZWQgVml0ZSBhcnRpZmFjdCBhZGRpdGlvbmFsbHkgY29udGFpbnMgY29kZSB3aXRoIHRoZSBmb2xsb3dpbmcgbGljZW5zZXM6CkJTRC0yLUNsYXVzZSwgQ0MwLTEuMCwgSVNDLCBNSVQKCiMgQnVuZGxlZCBkZXBlbmRlbmNpZXM6CiMjIEBqcmlkZ2V3ZWxsL2dlbi1tYXBwaW5nLCBAanJpZGdld2VsbC9yZW1hcHBpbmcsIEBqcmlkZ2V3ZWxsL3NvdXJjZW1hcC1jb2RlYywgQGpyaWRnZXdlbGwvdHJhY2UtbWFwcGluZwpMaWNlbnNlOiBNSVQKQnk6IEp1c3RpbiBSaWRnZXdlbGwKUmVwb3NpdG9yaWVzOiBnaXQraHR0cHM6Ly9naXRodWIuY29tL2pyaWRnZXdlbGwvc291cmNlbWFwcy5naXQsIGdpdCtodHRwczovL2dpdGh1Yi5jb20vanJpZGdld2VsbC9zb3VyY2VtYXBzLmdpdCwgZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS9qcmlkZ2V3ZWxsL3NvdXJjZW1hcHMuZ2l0LCBnaXQraHR0cHM6Ly9naXRodWIuY29tL2pyaWRnZXdlbGwvc291cmNlbWFwcy5naXQKCj4gQ29weXJpZ2h0IDIwMjQgSnVzdGluIFJpZGdld2VsbCA8anVzdGluQHJpZGdld2VsbC5uYW1lPgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbgo+IGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgQGpyaWRnZXdlbGwvcmVzb2x2ZS11cmkKTGljZW5zZTogTUlUCkJ5OiBKdXN0aW4gUmlkZ2V3ZWxsClJlcG9zaXRvcnk6IGh0dHBzOi8vZ2l0aHViLmNvbS9qcmlkZ2V3ZWxsL3Jlc29sdmUtdXJpCgo+IENvcHlyaWdodCAyMDE5IEp1c3RpbiBSaWRnZXdlbGwgPGpyaWRnZXdlbGxAZ29vZ2xlLmNvbT4KPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFCj4gU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIEBwb2xrYS9jb21wcmVzc2lvbgpMaWNlbnNlOiBNSVQKUmVwb3NpdG9yeTogbHVrZWVkL3BvbGthCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIEBwb2xrYS91cmwKTGljZW5zZTogTUlUCkJ5OiBMdWtlIEVkd2FyZHMKUmVwb3NpdG9yeTogbHVrZWVkL3BvbGthCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIEByb2xsZG93bi9wbHVnaW51dGlscwpMaWNlbnNlOiBNSVQKUmVwb3NpdG9yeTogZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS9yb2xsZG93bi9yb2xsZG93bi5naXQKCj4gTUlUIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMjQtcHJlc2VudCBWb2lkWmVybyBJbmMuICYgQ29udHJpYnV0b3JzCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAo+IGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQo+IFNPRlRXQVJFLgo+IAo+IGVuZCBvZiB0ZXJtcyBhbmQgY29uZGl0aW9ucwo+IAo+IFRoZSBsaWNlbnNlcyBvZiBleHRlcm5hbGx5IG1haW50YWluZWQgbGlicmFyaWVzIGZyb20gd2hpY2ggcGFydHMgb2YgdGhlIFNvZnR3YXJlIGlzIGRlcml2ZWQgYXJlIGxpc3RlZCBbaGVyZV0oaHR0cHM6Ly9naXRodWIuY29tL3JvbGxkb3duL3JvbGxkb3duL2Jsb2IvbWFpbi9USElSRC1QQVJUWS1MSUNFTlNFKS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgQHJvbGx1cC9wbHVnaW4tYWxpYXMsIEByb2xsdXAvcGx1Z2luLWNvbW1vbmpzLCBAcm9sbHVwL3BsdWdpbi1keW5hbWljLWltcG9ydC12YXJzLCBAcm9sbHVwL3BsdWdpbnV0aWxzCkxpY2Vuc2U6IE1JVApCeTogSm9oYW5uZXMgU3RlaW4KUmVwb3NpdG9yeTogcm9sbHVwL3BsdWdpbnMKCkxpY2Vuc2U6IE1JVApCeTogUmljaCBIYXJyaXMKUmVwb3NpdG9yeTogcm9sbHVwL3BsdWdpbnMKCkxpY2Vuc2U6IE1JVApCeTogTGFyc0RlbkJha2tlcgpSZXBvc2l0b3J5OiByb2xsdXAvcGx1Z2lucwoKTGljZW5zZTogTUlUCkJ5OiBSaWNoIEhhcnJpcwpSZXBvc2l0b3J5OiByb2xsdXAvcGx1Z2lucwoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTkgUm9sbHVwSlMgUGx1Z2luIENvbnRyaWJ1dG9ycyAoaHR0cHM6Ly9naXRodWIuY29tL3JvbGx1cC9wbHVnaW5zL2dyYXBocy9jb250cmlidXRvcnMpCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCj4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOCj4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBhbnltYXRjaApMaWNlbnNlOiBJU0MKQnk6IEVsYW4gU2hhbmtlcgpSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vbWljcm9tYXRjaC9hbnltYXRjaAoKPiBUaGUgSVNDIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTkgRWxhbiBTaGFua2VyLCBQYXVsIE1pbGxlciAoaHR0cHM6Ly9wYXVsbWlsbHIuY29tKQo+IAo+IFBlcm1pc3Npb24gdG8gdXNlLCBjb3B5LCBtb2RpZnksIGFuZC9vciBkaXN0cmlidXRlIHRoaXMgc29mdHdhcmUgZm9yIGFueQo+IHB1cnBvc2Ugd2l0aCBvciB3aXRob3V0IGZlZSBpcyBoZXJlYnkgZ3JhbnRlZCwgcHJvdmlkZWQgdGhhdCB0aGUgYWJvdmUKPiBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIGFwcGVhciBpbiBhbGwgY29waWVzLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiIEFORCBUSEUgQVVUSE9SIERJU0NMQUlNUyBBTEwgV0FSUkFOVElFUwo+IFdJVEggUkVHQVJEIFRPIFRISVMgU09GVFdBUkUgSU5DTFVESU5HIEFMTCBJTVBMSUVEIFdBUlJBTlRJRVMgT0YKPiBNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1IgQkUgTElBQkxFIEZPUgo+IEFOWSBTUEVDSUFMLCBESVJFQ1QsIElORElSRUNULCBPUiBDT05TRVFVRU5USUFMIERBTUFHRVMgT1IgQU5ZIERBTUFHRVMKPiBXSEFUU09FVkVSIFJFU1VMVElORyBGUk9NIExPU1MgT0YgVVNFLCBEQVRBIE9SIFBST0ZJVFMsIFdIRVRIRVIgSU4gQU4KPiBBQ1RJT04gT0YgQ09OVFJBQ1QsIE5FR0xJR0VOQ0UgT1IgT1RIRVIgVE9SVElPVVMgQUNUSU9OLCBBUklTSU5HIE9VVCBPRiBPUgo+IElOIENPTk5FQ1RJT04gV0lUSCBUSEUgVVNFIE9SIFBFUkZPUk1BTkNFIE9GIFRISVMgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGFydGljaG9raWUKTGljZW5zZTogTUlUCkJ5OiBzYXBwaGktcmVkLCBFdmFuIFlvdQpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL3NhcHBoaS1yZWQvYXJ0aWNob2tpZS5naXQKCj4gTUlUIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMjAtcHJlc2VudCwgWXV4aSAoRXZhbikgWW91Cj4gQ29weXJpZ2h0IChjKSAyMDIzLXByZXNlbnQsIHNhcHBoaS1yZWQKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFCj4gU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGJpbmFyeS1leHRlbnNpb25zCkxpY2Vuc2U6IE1JVApCeTogU2luZHJlIFNvcmh1cwpSZXBvc2l0b3J5OiBzaW5kcmVzb3JodXMvYmluYXJ5LWV4dGVuc2lvbnMKCj4gTUlUIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIFNpbmRyZSBTb3JodXMgPHNpbmRyZXNvcmh1c0BnbWFpbC5jb20+IChodHRwczovL3NpbmRyZXNvcmh1cy5jb20pCj4gQ29weXJpZ2h0IChjKSBQYXVsIE1pbGxlciAoaHR0cHM6Ly9wYXVsbWlsbHIuY29tKQo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgYnJhY2VzLCBmaWxsLXJhbmdlLCBpcy1udW1iZXIKTGljZW5zZTogTUlUCkJ5OiBKb24gU2NobGlua2VydCwgQnJpYW4gV29vZHdhcmQsIEVsYW4gU2hhbmtlciwgRXVnZW5lIFNoYXJ5Z2luLCBoZW1hbnRoLmhtClJlcG9zaXRvcnk6IG1pY3JvbWF0Y2gvYnJhY2VzCgpMaWNlbnNlOiBNSVQKQnk6IEpvbiBTY2hsaW5rZXJ0LCBFZG8gUml2YWksIFBhdWwgTWlsbGVyLCBSb3V2ZW4gV2XDn2xpbmcKUmVwb3NpdG9yeTogam9uc2NobGlua2VydC9maWxsLXJhbmdlCgpMaWNlbnNlOiBNSVQKQnk6IEpvbiBTY2hsaW5rZXJ0LCBPbHN0ZW4gTGFyY2ssIFJvdXZlbiBXZcOfbGluZwpSZXBvc2l0b3J5OiBqb25zY2hsaW5rZXJ0L2lzLW51bWJlcgoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTQtcHJlc2VudCwgSm9uIFNjaGxpbmtlcnQuCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCj4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOCj4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBidW5kbGUtbmFtZSwgZGVmYXVsdC1icm93c2VyLCBkZWZhdWx0LWJyb3dzZXItaWQsIGRlZmluZS1sYXp5LXByb3AsIGlzLWRvY2tlciwgaXMtaW5zaWRlLWNvbnRhaW5lciwgaXMtd3NsLCBvcGVuLCBydW4tYXBwbGVzY3JpcHQsIHdzbC11dGlscwpMaWNlbnNlOiBNSVQKQnk6IFNpbmRyZSBTb3JodXMKUmVwb3NpdG9yaWVzOiBzaW5kcmVzb3JodXMvYnVuZGxlLW5hbWUsIHNpbmRyZXNvcmh1cy9kZWZhdWx0LWJyb3dzZXIsIHNpbmRyZXNvcmh1cy9kZWZhdWx0LWJyb3dzZXItaWQsIHNpbmRyZXNvcmh1cy9kZWZpbmUtbGF6eS1wcm9wLCBzaW5kcmVzb3JodXMvaXMtZG9ja2VyLCBzaW5kcmVzb3JodXMvaXMtaW5zaWRlLWNvbnRhaW5lciwgc2luZHJlc29yaHVzL2lzLXdzbCwgc2luZHJlc29yaHVzL29wZW4sIHNpbmRyZXNvcmh1cy9ydW4tYXBwbGVzY3JpcHQsIHNpbmRyZXNvcmh1cy93c2wtdXRpbHMKCj4gTUlUIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIFNpbmRyZSBTb3JodXMgPHNpbmRyZXNvcmh1c0BnbWFpbC5jb20+IChodHRwczovL3NpbmRyZXNvcmh1cy5jb20pCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBjYWMKTGljZW5zZTogTUlUCkJ5OiBlZ29pc3QKUmVwb3NpdG9yeTogZWdvaXN0L2NhYwoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIEVHT0lTVCA8MHgxNDI4NTdAZ21haWwuY29tPiAoaHR0cHM6Ly9naXRodWIuY29tL2Vnb2lzdCkKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGNob2tpZGFyCkxpY2Vuc2U6IE1JVApCeTogUGF1bCBNaWxsZXIsIEVsYW4gU2hhbmtlcgpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL3BhdWxtaWxsci9jaG9raWRhci5naXQKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDEyLTIwMTkgUGF1bCBNaWxsZXIgKGh0dHBzOi8vcGF1bG1pbGxyLmNvbSksIEVsYW4gU2hhbmtlcgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSDigJxTb2Z0d2FyZeKAnSksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQg4oCcQVMgSVPigJ0sIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOCj4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBjb21tb25kaXIsIHNoZWxsLXF1b3RlCkxpY2Vuc2U6IE1JVApCeTogSmFtZXMgSGFsbGlkYXkKUmVwb3NpdG9yaWVzOiBodHRwOi8vZ2l0aHViLmNvbS9zdWJzdGFjay9ub2RlLWNvbW1vbmRpci5naXQsIGh0dHA6Ly9naXRodWIuY29tL2xqaGFyYi9zaGVsbC1xdW90ZS5naXQKCj4gVGhlIE1JVCBMaWNlbnNlCj4gCj4gQ29weXJpZ2h0IChjKSAyMDEzIEphbWVzIEhhbGxpZGF5IChtYWlsQHN1YnN0YWNrLm5ldCkKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgCj4gdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIAo+IGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byAKPiBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgCj4gd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIAo+IG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCAKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSAKPiB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCAKPiBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSAKPiBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgCj4gRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIAo+IE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gCj4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiAKPiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgCj4gVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgCj4gU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGNvbm5lY3QKTGljZW5zZTogTUlUCkJ5OiBUSiBIb2xvd2F5Y2h1aywgRG91Z2xhcyBDaHJpc3RvcGhlciBXaWxzb24sIEpvbmF0aGFuIE9uZywgVGltIENhc3dlbGwKUmVwb3NpdG9yeTogc2VuY2hhbGFicy9jb25uZWN0Cgo+IChUaGUgTUlUIExpY2Vuc2UpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDEwIFNlbmNoYSBJbmMuCj4gQ29weXJpZ2h0IChjKSAyMDExIExlYXJuQm9vc3QKPiBDb3B5cmlnaHQgKGMpIDIwMTEtMjAxNCBUSiBIb2xvd2F5Y2h1awo+IENvcHlyaWdodCAoYykgMjAxNSBEb3VnbGFzIENocmlzdG9waGVyIFdpbHNvbgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZwo+IGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZQo+ICdTb2Z0d2FyZScpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcKPiB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsCj4gZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvCj4gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvCj4gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlCj4gaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICdBUyBJUycsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsCj4gRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GCj4gTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULgo+IElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZCj4gQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwKPiBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRQo+IFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBjb252ZXJ0LXNvdXJjZS1tYXAKTGljZW5zZTogTUlUCkJ5OiBUaG9yc3RlbiBMb3JlbnoKUmVwb3NpdG9yeTogZ2l0Oi8vZ2l0aHViLmNvbS90aGxvcmVuei9jb252ZXJ0LXNvdXJjZS1tYXAuZ2l0Cgo+IENvcHlyaWdodCAyMDEzIFRob3JzdGVuIExvcmVuei4gCj4gQWxsIHJpZ2h0cyByZXNlcnZlZC4KPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbgo+IG9idGFpbmluZyBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uCj4gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dAo+IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLAo+IGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlCj4gU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcKPiBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlCj4gaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsCj4gRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTCj4gT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQKPiBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVAo+IEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLAo+IFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORwo+IEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IKPiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGNvcnMKTGljZW5zZTogTUlUCkJ5OiBUcm95IEdvb2RlClJlcG9zaXRvcnk6IGV4cHJlc3Nqcy9jb3JzCgo+IChUaGUgTUlUIExpY2Vuc2UpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDEzIFRyb3kgR29vZGUgPHRyb3lnb29kZUBnbWFpbC5jb20+Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nCj4gYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlCj4gJ1NvZnR3YXJlJyksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZwo+IHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwKPiBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8KPiBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8KPiB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUKPiBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgJ0FTIElTJywgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwKPiBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YKPiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuCj4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkKPiBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULAo+IFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFCj4gU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGNyb3NzLXNwYXduCkxpY2Vuc2U6IE1JVApCeTogQW5kcsOpIENydXoKUmVwb3NpdG9yeTogZ2l0QGdpdGh1Yi5jb206bW94eXN0dWRpby9ub2RlLWNyb3NzLXNwYXduLmdpdAoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTggTWFkZSBXaXRoIE1PWFkgTGRhIDxoZWxsb0Btb3h5LnN0dWRpbz4KPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGNzc2VzYwpMaWNlbnNlOiBNSVQKQnk6IE1hdGhpYXMgQnluZW5zClJlcG9zaXRvcnk6IGh0dHBzOi8vZ2l0aHViLmNvbS9tYXRoaWFzYnluZW5zL2Nzc2VzYy5naXQKCj4gQ29weXJpZ2h0IE1hdGhpYXMgQnluZW5zIDxodHRwczovL21hdGhpYXNieW5lbnMuYmUvPgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZwo+IGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZQo+ICJTb2Z0d2FyZSIpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcKPiB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsCj4gZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvCj4gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvCj4gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlCj4gaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsCj4gRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GCj4gTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQKPiBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFCj4gTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTgo+IE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTgo+IFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBkZWJ1ZwpMaWNlbnNlOiBNSVQKQnk6IEpvc2ggSnVub24sIFRKIEhvbG93YXljaHVrLCBOYXRoYW4gUmFqbGljaCwgQW5kcmV3IFJoeW5lClJlcG9zaXRvcnk6IGdpdDovL2dpdGh1Yi5jb20vZGVidWctanMvZGVidWcuZ2l0Cgo+IChUaGUgTUlUIExpY2Vuc2UpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDE0LTIwMTcgVEogSG9sb3dheWNodWsgPHRqQHZpc2lvbi1tZWRpYS5jYT4KPiBDb3B5cmlnaHQgKGMpIDIwMTgtMjAyMSBKb3NoIEp1bm9uCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlCj4gYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICdTb2Z0d2FyZScpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLAo+IGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsCj4gYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywKPiBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsCj4gcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAnQVMgSVMnLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UCj4gTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuCj4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLAo+IFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRQo+IFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBkb3RlbnYKTGljZW5zZTogQlNELTItQ2xhdXNlClJlcG9zaXRvcnk6IGdpdDovL2dpdGh1Yi5jb20vbW90ZG90bGEvZG90ZW52LmdpdAoKPiBDb3B5cmlnaHQgKGMpIDIwMTUsIFNjb3R0IE1vdHRlCj4gQWxsIHJpZ2h0cyByZXNlcnZlZC4KPiAKPiBSZWRpc3RyaWJ1dGlvbiBhbmQgdXNlIGluIHNvdXJjZSBhbmQgYmluYXJ5IGZvcm1zLCB3aXRoIG9yIHdpdGhvdXQKPiBtb2RpZmljYXRpb24sIGFyZSBwZXJtaXR0ZWQgcHJvdmlkZWQgdGhhdCB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnMgYXJlIG1ldDoKPiAKPiAqIFJlZGlzdHJpYnV0aW9ucyBvZiBzb3VyY2UgY29kZSBtdXN0IHJldGFpbiB0aGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSwgdGhpcwo+ICAgbGlzdCBvZiBjb25kaXRpb25zIGFuZCB0aGUgZm9sbG93aW5nIGRpc2NsYWltZXIuCj4gCj4gKiBSZWRpc3RyaWJ1dGlvbnMgaW4gYmluYXJ5IGZvcm0gbXVzdCByZXByb2R1Y2UgdGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UsCj4gICB0aGlzIGxpc3Qgb2YgY29uZGl0aW9ucyBhbmQgdGhlIGZvbGxvd2luZyBkaXNjbGFpbWVyIGluIHRoZSBkb2N1bWVudGF0aW9uCj4gICBhbmQvb3Igb3RoZXIgbWF0ZXJpYWxzIHByb3ZpZGVkIHdpdGggdGhlIGRpc3RyaWJ1dGlvbi4KPiAKPiBUSElTIFNPRlRXQVJFIElTIFBST1ZJREVEIEJZIFRIRSBDT1BZUklHSFQgSE9MREVSUyBBTkQgQ09OVFJJQlVUT1JTICJBUyBJUyIKPiBBTkQgQU5ZIEVYUFJFU1MgT1IgSU1QTElFRCBXQVJSQU5USUVTLCBJTkNMVURJTkcsIEJVVCBOT1QgTElNSVRFRCBUTywgVEhFCj4gSU1QTElFRCBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSBBTkQgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQVJFCj4gRElTQ0xBSU1FRC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIENPUFlSSUdIVCBIT0xERVIgT1IgQ09OVFJJQlVUT1JTIEJFIExJQUJMRQo+IEZPUiBBTlkgRElSRUNULCBJTkRJUkVDVCwgSU5DSURFTlRBTCwgU1BFQ0lBTCwgRVhFTVBMQVJZLCBPUiBDT05TRVFVRU5USUFMCj4gREFNQUdFUyAoSU5DTFVESU5HLCBCVVQgTk9UIExJTUlURUQgVE8sIFBST0NVUkVNRU5UIE9GIFNVQlNUSVRVVEUgR09PRFMgT1IKPiBTRVJWSUNFUzsgTE9TUyBPRiBVU0UsIERBVEEsIE9SIFBST0ZJVFM7IE9SIEJVU0lORVNTIElOVEVSUlVQVElPTikgSE9XRVZFUgo+IENBVVNFRCBBTkQgT04gQU5ZIFRIRU9SWSBPRiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQ09OVFJBQ1QsIFNUUklDVCBMSUFCSUxJVFksCj4gT1IgVE9SVCAoSU5DTFVESU5HIE5FR0xJR0VOQ0UgT1IgT1RIRVJXSVNFKSBBUklTSU5HIElOIEFOWSBXQVkgT1VUIE9GIFRIRSBVU0UKPiBPRiBUSElTIFNPRlRXQVJFLCBFVkVOIElGIEFEVklTRUQgT0YgVEhFIFBPU1NJQklMSVRZIE9GIFNVQ0ggREFNQUdFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBkb3RlbnYtZXhwYW5kCkxpY2Vuc2U6IEJTRC0yLUNsYXVzZQpCeTogbW90ZG90bGEKUmVwb3NpdG9yeTogaHR0cHM6Ly9naXRodWIuY29tL21vdGRvdGxhL2RvdGVudi1leHBhbmQKCj4gQ29weXJpZ2h0IChjKSAyMDE2LCBTY290dCBNb3R0ZQo+IEFsbCByaWdodHMgcmVzZXJ2ZWQuCj4gCj4gUmVkaXN0cmlidXRpb24gYW5kIHVzZSBpbiBzb3VyY2UgYW5kIGJpbmFyeSBmb3Jtcywgd2l0aCBvciB3aXRob3V0Cj4gbW9kaWZpY2F0aW9uLCBhcmUgcGVybWl0dGVkIHByb3ZpZGVkIHRoYXQgdGhlIGZvbGxvd2luZyBjb25kaXRpb25zIGFyZSBtZXQ6Cj4gCj4gKiBSZWRpc3RyaWJ1dGlvbnMgb2Ygc291cmNlIGNvZGUgbXVzdCByZXRhaW4gdGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UsIHRoaXMKPiAgIGxpc3Qgb2YgY29uZGl0aW9ucyBhbmQgdGhlIGZvbGxvd2luZyBkaXNjbGFpbWVyLgo+IAo+ICogUmVkaXN0cmlidXRpb25zIGluIGJpbmFyeSBmb3JtIG11c3QgcmVwcm9kdWNlIHRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlLAo+ICAgdGhpcyBsaXN0IG9mIGNvbmRpdGlvbnMgYW5kIHRoZSBmb2xsb3dpbmcgZGlzY2xhaW1lciBpbiB0aGUgZG9jdW1lbnRhdGlvbgo+ICAgYW5kL29yIG90aGVyIG1hdGVyaWFscyBwcm92aWRlZCB3aXRoIHRoZSBkaXN0cmlidXRpb24uCj4gCj4gVEhJUyBTT0ZUV0FSRSBJUyBQUk9WSURFRCBCWSBUSEUgQ09QWVJJR0hUIEhPTERFUlMgQU5EIENPTlRSSUJVVE9SUyAiQVMgSVMiCj4gQU5EIEFOWSBFWFBSRVNTIE9SIElNUExJRUQgV0FSUkFOVElFUywgSU5DTFVESU5HLCBCVVQgTk9UIExJTUlURUQgVE8sIFRIRQo+IElNUExJRUQgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFSRQo+IERJU0NMQUlNRUQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBDT1BZUklHSFQgSE9MREVSIE9SIENPTlRSSUJVVE9SUyBCRSBMSUFCTEUKPiBGT1IgQU5ZIERJUkVDVCwgSU5ESVJFQ1QsIElOQ0lERU5UQUwsIFNQRUNJQUwsIEVYRU1QTEFSWSwgT1IgQ09OU0VRVUVOVElBTAo+IERBTUFHRVMgKElOQ0xVRElORywgQlVUIE5PVCBMSU1JVEVEIFRPLCBQUk9DVVJFTUVOVCBPRiBTVUJTVElUVVRFIEdPT0RTIE9SCj4gU0VSVklDRVM7IExPU1MgT0YgVVNFLCBEQVRBLCBPUiBQUk9GSVRTOyBPUiBCVVNJTkVTUyBJTlRFUlJVUFRJT04pIEhPV0VWRVIKPiBDQVVTRUQgQU5EIE9OIEFOWSBUSEVPUlkgT0YgTElBQklMSVRZLCBXSEVUSEVSIElOIENPTlRSQUNULCBTVFJJQ1QgTElBQklMSVRZLAo+IE9SIFRPUlQgKElOQ0xVRElORyBORUdMSUdFTkNFIE9SIE9USEVSV0lTRSkgQVJJU0lORyBJTiBBTlkgV0FZIE9VVCBPRiBUSEUgVVNFCj4gT0YgVEhJUyBTT0ZUV0FSRSwgRVZFTiBJRiBBRFZJU0VEIE9GIFRIRSBQT1NTSUJJTElUWSBPRiBTVUNIIERBTUFHRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgZWUtZmlyc3QKTGljZW5zZTogTUlUCkJ5OiBKb25hdGhhbiBPbmcsIERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uClJlcG9zaXRvcnk6IGpvbmF0aGFub25nL2VlLWZpcnN0Cgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+IAo+IENvcHlyaWdodCAoYykgMjAxNCBKb25hdGhhbiBPbmcgbWVAam9uZ2xlYmVycnkuY29tCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCj4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOCj4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBlbmNvZGV1cmwKTGljZW5zZTogTUlUCkJ5OiBEb3VnbGFzIENocmlzdG9waGVyIFdpbHNvbgpSZXBvc2l0b3J5OiBwaWxsYXJqcy9lbmNvZGV1cmwKCj4gKFRoZSBNSVQgTGljZW5zZSkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTYgRG91Z2xhcyBDaHJpc3RvcGhlciBXaWxzb24KPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcKPiBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUKPiAnU29mdHdhcmUnKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nCj4gd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLAo+IGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0bwo+IHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0bwo+IHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZQo+IGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAnQVMgSVMnLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELAo+IEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRgo+IE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4KPiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWQo+IENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsCj4gVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUKPiBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgZW50aXRpZXMKTGljZW5zZTogQlNELTItQ2xhdXNlCkJ5OiBGZWxpeCBCb2VobQpSZXBvc2l0b3J5OiBnaXQ6Ly9naXRodWIuY29tL2ZiNTUvZW50aXRpZXMuZ2l0Cgo+IENvcHlyaWdodCAoYykgRmVsaXggQsO2aG0KPiBBbGwgcmlnaHRzIHJlc2VydmVkLgo+IAo+IFJlZGlzdHJpYnV0aW9uIGFuZCB1c2UgaW4gc291cmNlIGFuZCBiaW5hcnkgZm9ybXMsIHdpdGggb3Igd2l0aG91dCBtb2RpZmljYXRpb24sIGFyZSBwZXJtaXR0ZWQgcHJvdmlkZWQgdGhhdCB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnMgYXJlIG1ldDoKPiAKPiBSZWRpc3RyaWJ1dGlvbnMgb2Ygc291cmNlIGNvZGUgbXVzdCByZXRhaW4gdGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UsIHRoaXMgbGlzdCBvZiBjb25kaXRpb25zIGFuZCB0aGUgZm9sbG93aW5nIGRpc2NsYWltZXIuCj4gCj4gUmVkaXN0cmlidXRpb25zIGluIGJpbmFyeSBmb3JtIG11c3QgcmVwcm9kdWNlIHRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlLCB0aGlzIGxpc3Qgb2YgY29uZGl0aW9ucyBhbmQgdGhlIGZvbGxvd2luZyBkaXNjbGFpbWVyIGluIHRoZSBkb2N1bWVudGF0aW9uIGFuZC9vciBvdGhlciBtYXRlcmlhbHMgcHJvdmlkZWQgd2l0aCB0aGUgZGlzdHJpYnV0aW9uLgo+IAo+IFRISVMgSVMgUFJPVklERUQgQlkgVEhFIENPUFlSSUdIVCBIT0xERVJTIEFORCBDT05UUklCVVRPUlMgIkFTIElTIiBBTkQgQU5ZIEVYUFJFU1MgT1IgSU1QTElFRCBXQVJSQU5USUVTLCBJTkNMVURJTkcsIEJVVCBOT1QgTElNSVRFRCBUTywgVEhFIElNUExJRUQgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFSRSBESVNDTEFJTUVELiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQ09QWVJJR0hUIEhPTERFUiBPUiBDT05UUklCVVRPUlMgQkUgTElBQkxFIEZPUiBBTlkgRElSRUNULCBJTkRJUkVDVCwgSU5DSURFTlRBTCwgU1BFQ0lBTCwgRVhFTVBMQVJZLCBPUiBDT05TRVFVRU5USUFMIERBTUFHRVMgKElOQ0xVRElORywgQlVUIE5PVCBMSU1JVEVEIFRPLCBQUk9DVVJFTUVOVCBPRiBTVUJTVElUVVRFIEdPT0RTIE9SIFNFUlZJQ0VTOyBMT1NTIE9GIFVTRSwgREFUQSwgT1IgUFJPRklUUzsgT1IgQlVTSU5FU1MgSU5URVJSVVBUSU9OKSBIT1dFVkVSIENBVVNFRCBBTkQgT04gQU5ZIFRIRU9SWSBPRiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQ09OVFJBQ1QsIFNUUklDVCBMSUFCSUxJVFksIE9SIFRPUlQgKElOQ0xVRElORyBORUdMSUdFTkNFIE9SIE9USEVSV0lTRSkgQVJJU0lORyBJTiBBTlkgV0FZIE9VVCBPRiBUSEUgVVNFIE9GIFRISVMsCj4gRVZFTiBJRiBBRFZJU0VEIE9GIFRIRSBQT1NTSUJJTElUWSBPRiBTVUNIIERBTUFHRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgZXMtbW9kdWxlLWxleGVyCkxpY2Vuc2U6IE1JVApCeTogR3V5IEJlZGZvcmQKUmVwb3NpdG9yeTogZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS9ndXliZWRmb3JkL2VzLW1vZHVsZS1sZXhlci5naXQKCj4gTUlUIExpY2Vuc2UKPiAtLS0tLS0tLS0tLQo+IAo+IENvcHlyaWdodCAoQykgMjAxOC0yMDIyIEd1eSBCZWRmb3JkCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBlc2NhcGUtaHRtbApMaWNlbnNlOiBNSVQKUmVwb3NpdG9yeTogY29tcG9uZW50L2VzY2FwZS1odG1sCgo+IChUaGUgTUlUIExpY2Vuc2UpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDEyLTIwMTMgVEogSG9sb3dheWNodWsKPiBDb3B5cmlnaHQgKGMpIDIwMTUgQW5kcmVhcyBMdWJiZQo+IENvcHlyaWdodCAoYykgMjAxNSBUaWFuY2hlbmcgIlRpbW90aHkiIEd1Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nCj4gYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlCj4gJ1NvZnR3YXJlJyksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZwo+IHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwKPiBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8KPiBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8KPiB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUKPiBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgJ0FTIElTJywgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwKPiBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YKPiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuCj4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkKPiBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULAo+IFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFCj4gU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGVzdHJlZS13YWxrZXIKTGljZW5zZTogTUlUCkJ5OiBSaWNoIEhhcnJpcwpSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vUmljaC1IYXJyaXMvZXN0cmVlLXdhbGtlcgoKPiBDb3B5cmlnaHQgKGMpIDIwMTUtMjAgW3RoZXNlIHBlb3BsZV0oaHR0cHM6Ly9naXRodWIuY29tL1JpY2gtSGFycmlzL2VzdHJlZS13YWxrZXIvZ3JhcGhzL2NvbnRyaWJ1dG9ycykKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGV0YWcKTGljZW5zZTogTUlUCkJ5OiBEb3VnbGFzIENocmlzdG9waGVyIFdpbHNvbiwgRGF2aWQgQmrDtnJrbHVuZApSZXBvc2l0b3J5OiBqc2h0dHAvZXRhZwoKPiAoVGhlIE1JVCBMaWNlbnNlKQo+IAo+IENvcHlyaWdodCAoYykgMjAxNC0yMDE2IERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nCj4gYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlCj4gJ1NvZnR3YXJlJyksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZwo+IHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwKPiBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8KPiBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8KPiB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUKPiBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgJ0FTIElTJywgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwKPiBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YKPiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuCj4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkKPiBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULAo+IFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFCj4gU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGZpbmFsaGFuZGxlcgpMaWNlbnNlOiBNSVQKQnk6IERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uClJlcG9zaXRvcnk6IHBpbGxhcmpzL2ZpbmFsaGFuZGxlcgoKPiAoVGhlIE1JVCBMaWNlbnNlKQo+IAo+IENvcHlyaWdodCAoYykgMjAxNC0yMDE3IERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uIDxkb3VnQHNvbWV0aGluZ2RvdWcuY29tPgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZwo+IGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZQo+ICdTb2Z0d2FyZScpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcKPiB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsCj4gZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvCj4gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvCj4gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlCj4gaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICdBUyBJUycsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsCj4gRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GCj4gTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULgo+IElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZCj4gQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwKPiBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRQo+IFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBmb2xsb3ctcmVkaXJlY3RzCkxpY2Vuc2U6IE1JVApCeTogUnViZW4gVmVyYm9yZ2gsIE9saXZpZXIgTGFsb25kZSwgSmFtZXMgVGFsbWFnZQpSZXBvc2l0b3J5OiBnaXQrc3NoOi8vZ2l0QGdpdGh1Yi5jb20vZm9sbG93LXJlZGlyZWN0cy9mb2xsb3ctcmVkaXJlY3RzLmdpdAoKPiBDb3B5cmlnaHQgMjAxNOKAk3ByZXNlbnQgT2xpdmllciBMYWxvbmRlIDxvbGFsb25kZUBnbWFpbC5jb20+LCBKYW1lcyBUYWxtYWdlIDxqYW1lc0B0YWxtYWdlLmlvPiwgUnViZW4gVmVyYm9yZ2gKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mCj4gdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4KPiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvCj4gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMKPiBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8KPiBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLAo+IFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IKPiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBnZW5lcmljLW5hbWVzCkxpY2Vuc2U6IE1JVApCeTogQWxleGV5IExpdHZpbm92ClJlcG9zaXRvcnk6IGdpdCtodHRwczovL2dpdGh1Yi5jb20vY3NzLW1vZHVsZXMvZ2VuZXJpYy1uYW1lcy5naXQKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDE1IEFsZXhleSBMaXR2aW5vdgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgZ2xvYi1wYXJlbnQKTGljZW5zZTogSVNDCkJ5OiBHdWxwIFRlYW0sIEVsYW4gU2hhbmtlciwgQmxhaW5lIEJ1YmxpdHoKUmVwb3NpdG9yeTogZ3VscGpzL2dsb2ItcGFyZW50Cgo+IFRoZSBJU0MgTGljZW5zZQo+IAo+IENvcHlyaWdodCAoYykgMjAxNSwgMjAxOSBFbGFuIFNoYW5rZXIKPiAKPiBQZXJtaXNzaW9uIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBhbmQvb3IgZGlzdHJpYnV0ZSB0aGlzIHNvZnR3YXJlIGZvciBhbnkKPiBwdXJwb3NlIHdpdGggb3Igd2l0aG91dCBmZWUgaXMgaGVyZWJ5IGdyYW50ZWQsIHByb3ZpZGVkIHRoYXQgdGhlIGFib3ZlCj4gY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBhcHBlYXIgaW4gYWxsIGNvcGllcy4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiBBTkQgVEhFIEFVVEhPUiBESVNDTEFJTVMgQUxMIFdBUlJBTlRJRVMKPiBXSVRIIFJFR0FSRCBUTyBUSElTIFNPRlRXQVJFIElOQ0xVRElORyBBTEwgSU1QTElFRCBXQVJSQU5USUVTIE9GCj4gTUVSQ0hBTlRBQklMSVRZIEFORCBGSVRORVNTLiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SIEJFIExJQUJMRSBGT1IKPiBBTlkgU1BFQ0lBTCwgRElSRUNULCBJTkRJUkVDVCwgT1IgQ09OU0VRVUVOVElBTCBEQU1BR0VTIE9SIEFOWSBEQU1BR0VTCj4gV0hBVFNPRVZFUiBSRVNVTFRJTkcgRlJPTSBMT1NTIE9GIFVTRSwgREFUQSBPUiBQUk9GSVRTLCBXSEVUSEVSIElOIEFOCj4gQUNUSU9OIE9GIENPTlRSQUNULCBORUdMSUdFTkNFIE9SIE9USEVSIFRPUlRJT1VTIEFDVElPTiwgQVJJU0lORyBPVVQgT0YgT1IKPiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFVTRSBPUiBQRVJGT1JNQU5DRSBPRiBUSElTIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBob3N0LXZhbGlkYXRpb24tbWlkZGxld2FyZQpMaWNlbnNlOiBNSVQKQnk6IHNhcHBoaS1yZWQKUmVwb3NpdG9yeTogZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS9zYXBwaGktcmVkL2hvc3QtdmFsaWRhdGlvbi1taWRkbGV3YXJlLmdpdAoKPiBNSVQgTGljZW5zZQo+IAo+IENvcHlyaWdodCAoYykgMjAyNSBzYXBwaGktcmVkCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAo+IGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQo+IFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBodHRwLXByb3h5LTMKTGljZW5zZTogTUlUCkJ5OiBXaWxsaWFtIFN0ZWluLCBDaGFybGllIFJvYmJpbnMsIEppbWIgRXNzZXIsIGpjcnVnenoKUmVwb3NpdG9yeTogaHR0cHM6Ly9naXRodWIuY29tL3NhZ2VtYXRoaW5jL2h0dHAtcHJveHktMy5naXQKCj4gbm9kZS1odHRwLTMKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTAtMjAyNSBXaWxsaWFtIFN0ZWluLCBDaGFybGllIFJvYmJpbnMsIEphcnJldHQgQ3J1Z2VyICYgdGhlIENvbnRyaWJ1dG9ycy4KPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcKPiBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUKPiAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nCj4gd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLAo+IGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0bwo+IHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0bwo+IHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZQo+IGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELAo+IEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRgo+IE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5ECj4gTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRQo+IExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04KPiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04KPiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgaWNzcy11dGlscwpMaWNlbnNlOiBJU0MKQnk6IEdsZW4gTWFkZGVybgpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL2Nzcy1tb2R1bGVzL2ljc3MtdXRpbHMuZ2l0Cgo+IElTQyBMaWNlbnNlIChJU0MpCj4gQ29weXJpZ2h0IDIwMTggR2xlbiBNYWRkZXJuCj4gCj4gUGVybWlzc2lvbiB0byB1c2UsIGNvcHksIG1vZGlmeSwgYW5kL29yIGRpc3RyaWJ1dGUgdGhpcyBzb2Z0d2FyZSBmb3IgYW55IHB1cnBvc2Ugd2l0aCBvciB3aXRob3V0IGZlZSBpcyBoZXJlYnkgZ3JhbnRlZCwgcHJvdmlkZWQgdGhhdCB0aGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBhcHBlYXIgaW4gYWxsIGNvcGllcy4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiBBTkQgVEhFIEFVVEhPUiBESVNDTEFJTVMgQUxMIFdBUlJBTlRJRVMgV0lUSCBSRUdBUkQgVE8gVEhJUyBTT0ZUV0FSRSBJTkNMVURJTkcgQUxMIElNUExJRUQgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1IgQkUgTElBQkxFIEZPUiBBTlkgU1BFQ0lBTCwgRElSRUNULCBJTkRJUkVDVCwgT1IgQ09OU0VRVUVOVElBTCBEQU1BR0VTIE9SIEFOWSBEQU1BR0VTIFdIQVRTT0VWRVIgUkVTVUxUSU5HIEZST00gTE9TUyBPRiBVU0UsIERBVEEgT1IgUFJPRklUUywgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIE5FR0xJR0VOQ0UgT1IgT1RIRVIgVE9SVElPVVMgQUNUSU9OLCBBUklTSU5HIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFVTRSBPUiBQRVJGT1JNQU5DRSBPRiBUSElTIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBpcy1iaW5hcnktcGF0aApMaWNlbnNlOiBNSVQKQnk6IFNpbmRyZSBTb3JodXMKUmVwb3NpdG9yeTogc2luZHJlc29yaHVzL2lzLWJpbmFyeS1wYXRoCgo+IE1JVCBMaWNlbnNlCj4gCj4gQ29weXJpZ2h0IChjKSAyMDE5IFNpbmRyZSBTb3JodXMgPHNpbmRyZXNvcmh1c0BnbWFpbC5jb20+IChodHRwczovL3NpbmRyZXNvcmh1cy5jb20pLCBQYXVsIE1pbGxlciAoaHR0cHM6Ly9wYXVsbWlsbHIuY29tKQo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgaXMtZXh0Z2xvYgpMaWNlbnNlOiBNSVQKQnk6IEpvbiBTY2hsaW5rZXJ0ClJlcG9zaXRvcnk6IGpvbnNjaGxpbmtlcnQvaXMtZXh0Z2xvYgoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTQtMjAxNiwgSm9uIFNjaGxpbmtlcnQKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGlzLWdsb2IKTGljZW5zZTogTUlUCkJ5OiBKb24gU2NobGlua2VydCwgQnJpYW4gV29vZHdhcmQsIERhbmllbCBQZXJlegpSZXBvc2l0b3J5OiBtaWNyb21hdGNoL2lzLWdsb2IKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDE0LTIwMTcsIEpvbiBTY2hsaW5rZXJ0Lgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbgo+IGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTgo+IFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgaXMtcmVmZXJlbmNlCkxpY2Vuc2U6IE1JVApCeTogUmljaCBIYXJyaXMKUmVwb3NpdG9yeTogZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS9SaWNoLUhhcnJpcy9pcy1yZWZlcmVuY2UuZ2l0CgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGlzZXhlLCB3aGljaApMaWNlbnNlOiBJU0MKQnk6IElzYWFjIFouIFNjaGx1ZXRlcgpSZXBvc2l0b3JpZXM6IGdpdCtodHRwczovL2dpdGh1Yi5jb20vaXNhYWNzL2lzZXhlLmdpdCwgZ2l0Oi8vZ2l0aHViLmNvbS9pc2FhY3Mvbm9kZS13aGljaC5naXQKCj4gVGhlIElTQyBMaWNlbnNlCj4gCj4gQ29weXJpZ2h0IChjKSBJc2FhYyBaLiBTY2hsdWV0ZXIgYW5kIENvbnRyaWJ1dG9ycwo+IAo+IFBlcm1pc3Npb24gdG8gdXNlLCBjb3B5LCBtb2RpZnksIGFuZC9vciBkaXN0cmlidXRlIHRoaXMgc29mdHdhcmUgZm9yIGFueQo+IHB1cnBvc2Ugd2l0aCBvciB3aXRob3V0IGZlZSBpcyBoZXJlYnkgZ3JhbnRlZCwgcHJvdmlkZWQgdGhhdCB0aGUgYWJvdmUKPiBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIGFwcGVhciBpbiBhbGwgY29waWVzLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiIEFORCBUSEUgQVVUSE9SIERJU0NMQUlNUyBBTEwgV0FSUkFOVElFUwo+IFdJVEggUkVHQVJEIFRPIFRISVMgU09GVFdBUkUgSU5DTFVESU5HIEFMTCBJTVBMSUVEIFdBUlJBTlRJRVMgT0YKPiBNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1IgQkUgTElBQkxFIEZPUgo+IEFOWSBTUEVDSUFMLCBESVJFQ1QsIElORElSRUNULCBPUiBDT05TRVFVRU5USUFMIERBTUFHRVMgT1IgQU5ZIERBTUFHRVMKPiBXSEFUU09FVkVSIFJFU1VMVElORyBGUk9NIExPU1MgT0YgVVNFLCBEQVRBIE9SIFBST0ZJVFMsIFdIRVRIRVIgSU4gQU4KPiBBQ1RJT04gT0YgQ09OVFJBQ1QsIE5FR0xJR0VOQ0UgT1IgT1RIRVIgVE9SVElPVVMgQUNUSU9OLCBBUklTSU5HIE9VVCBPRiBPUgo+IElOIENPTk5FQ1RJT04gV0lUSCBUSEUgVVNFIE9SIFBFUkZPUk1BTkNFIE9GIFRISVMgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGpzLXRva2VucwpMaWNlbnNlOiBNSVQKQnk6IFNpbW9uIEx5ZGVsbApSZXBvc2l0b3J5OiBseWRlbGwvanMtdG9rZW5zCgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+IAo+IENvcHlyaWdodCAoYykgMjAxNCwgMjAxNSwgMjAxNiwgMjAxNywgMjAxOCwgMjAxOSwgMjAyMCwgMjAyMSwgMjAyMiwgMjAyMywgMjAyNCBTaW1vbiBMeWRlbGwKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGxhdW5jaC1lZGl0b3IsIGxhdW5jaC1lZGl0b3ItbWlkZGxld2FyZQpMaWNlbnNlOiBNSVQKQnk6IEV2YW4gWW91ClJlcG9zaXRvcmllczogZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS95eXg5OTA4MDMvbGF1bmNoLWVkaXRvci5naXQsIGdpdCtodHRwczovL2dpdGh1Yi5jb20veXl4OTkwODAzL2xhdW5jaC1lZGl0b3IuZ2l0Cgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+IAo+IENvcHlyaWdodCAoYykgMjAxNy1wcmVzZW50LCBZdXhpIChFdmFuKSBZb3UKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGxpbGNvbmZpZwpMaWNlbnNlOiBNSVQKQnk6IGFudG9uazUyClJlcG9zaXRvcnk6IGh0dHBzOi8vZ2l0aHViLmNvbS9hbnRvbms1Mi9saWxjb25maWcKCj4gTUlUIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMjIgQW50b24gS2FzdHJpdHNraXkKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFCj4gU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGxvYWRlci11dGlscwpMaWNlbnNlOiBNSVQKQnk6IFRvYmlhcyBLb3BwZXJzIEBzb2tyYQpSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vd2VicGFjay9sb2FkZXItdXRpbHMuZ2l0Cgo+IENvcHlyaWdodCBKUyBGb3VuZGF0aW9uIGFuZCBvdGhlciBjb250cmlidXRvcnMKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcKPiBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUKPiAnU29mdHdhcmUnKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nCj4gd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLAo+IGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0bwo+IHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0bwo+IHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZQo+IGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAnQVMgSVMnLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELAo+IEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRgo+IE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4KPiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWQo+IENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsCj4gVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUKPiBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgbG9kYXNoLmNhbWVsY2FzZQpMaWNlbnNlOiBNSVQKQnk6IEpvaG4tRGF2aWQgRGFsdG9uLCBCbGFpbmUgQnVibGl0eiwgTWF0aGlhcyBCeW5lbnMKUmVwb3NpdG9yeTogbG9kYXNoL2xvZGFzaAoKPiBDb3B5cmlnaHQgalF1ZXJ5IEZvdW5kYXRpb24gYW5kIG90aGVyIGNvbnRyaWJ1dG9ycyA8aHR0cHM6Ly9qcXVlcnkub3JnLz4KPiAKPiBCYXNlZCBvbiBVbmRlcnNjb3JlLmpzLCBjb3B5cmlnaHQgSmVyZW15IEFzaGtlbmFzLAo+IERvY3VtZW50Q2xvdWQgYW5kIEludmVzdGlnYXRpdmUgUmVwb3J0ZXJzICYgRWRpdG9ycyA8aHR0cDovL3VuZGVyc2NvcmVqcy5vcmcvPgo+IAo+IFRoaXMgc29mdHdhcmUgY29uc2lzdHMgb2Ygdm9sdW50YXJ5IGNvbnRyaWJ1dGlvbnMgbWFkZSBieSBtYW55Cj4gaW5kaXZpZHVhbHMuIEZvciBleGFjdCBjb250cmlidXRpb24gaGlzdG9yeSwgc2VlIHRoZSByZXZpc2lvbiBoaXN0b3J5Cj4gYXZhaWxhYmxlIGF0IGh0dHBzOi8vZ2l0aHViLmNvbS9sb2Rhc2gvbG9kYXNoCj4gCj4gVGhlIGZvbGxvd2luZyBsaWNlbnNlIGFwcGxpZXMgdG8gYWxsIHBhcnRzIG9mIHRoaXMgc29mdHdhcmUgZXhjZXB0IGFzCj4gZG9jdW1lbnRlZCBiZWxvdzoKPiAKPiA9PT09Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nCj4gYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlCj4gIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZwo+IHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwKPiBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8KPiBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8KPiB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUKPiBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwKPiBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YKPiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORAo+IE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUKPiBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OCj4gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OCj4gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCj4gCj4gPT09PQo+IAo+IENvcHlyaWdodCBhbmQgcmVsYXRlZCByaWdodHMgZm9yIHNhbXBsZSBjb2RlIGFyZSB3YWl2ZWQgdmlhIENDMC4gU2FtcGxlCj4gY29kZSBpcyBkZWZpbmVkIGFzIGFsbCBzb3VyY2UgY29kZSBkaXNwbGF5ZWQgd2l0aGluIHRoZSBwcm9zZSBvZiB0aGUKPiBkb2N1bWVudGF0aW9uLgo+IAo+IENDMDogaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvcHVibGljZG9tYWluL3plcm8vMS4wLwo+IAo+ID09PT0KPiAKPiBGaWxlcyBsb2NhdGVkIGluIHRoZSBub2RlX21vZHVsZXMgYW5kIHZlbmRvciBkaXJlY3RvcmllcyBhcmUgZXh0ZXJuYWxseQo+IG1haW50YWluZWQgbGlicmFyaWVzIHVzZWQgYnkgdGhpcyBzb2Z0d2FyZSB3aGljaCBoYXZlIHRoZWlyIG93bgo+IGxpY2Vuc2VzOyB3ZSByZWNvbW1lbmQgeW91IHJlYWQgdGhlbSwgYXMgdGhlaXIgdGVybXMgbWF5IGRpZmZlciBmcm9tIHRoZQo+IHRlcm1zIGFib3ZlLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBtYWdpYy1zdHJpbmcKTGljZW5zZTogTUlUCkJ5OiBSaWNoIEhhcnJpcwpSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vcmljaC1oYXJyaXMvbWFnaWMtc3RyaW5nLmdpdAoKPiBDb3B5cmlnaHQgMjAxOCBSaWNoIEhhcnJpcwo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgbWxseSwgdWZvCkxpY2Vuc2U6IE1JVApSZXBvc2l0b3JpZXM6IHVuanMvbWxseSwgdW5qcy91Zm8KCj4gTUlUIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIFBvb3lhIFBhcnNhIDxwb295YUBwaTAuaW8+Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAo+IGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQo+IFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBtcm1pbWUKTGljZW5zZTogTUlUCkJ5OiBMdWtlIEVkd2FyZHMKUmVwb3NpdG9yeTogbHVrZWVkL21ybWltZQoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIEx1a2UgRWR3YXJkcyA8bHVrZS5lZHdhcmRzMDVAZ21haWwuY29tPiAoaHR0cHM6Ly9sdWtlZWQuY29tKQo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbgo+IGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTgo+IFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgbXMKTGljZW5zZTogTUlUClJlcG9zaXRvcnk6IHZlcmNlbC9tcwoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMjAgVmVyY2VsLCBJbmMuCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAo+IGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQo+IFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBub3JtYWxpemUtcGF0aApMaWNlbnNlOiBNSVQKQnk6IEpvbiBTY2hsaW5rZXJ0LCBCbGFpbmUgQnVibGl0egpSZXBvc2l0b3J5OiBqb25zY2hsaW5rZXJ0L25vcm1hbGl6ZS1wYXRoCgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+IAo+IENvcHlyaWdodCAoYykgMjAxNC0yMDE4LCBKb24gU2NobGlua2VydC4KPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIG9iamVjdC1hc3NpZ24KTGljZW5zZTogTUlUCkJ5OiBTaW5kcmUgU29yaHVzClJlcG9zaXRvcnk6IHNpbmRyZXNvcmh1cy9vYmplY3QtYXNzaWduCgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+IAo+IENvcHlyaWdodCAoYykgU2luZHJlIFNvcmh1cyA8c2luZHJlc29yaHVzQGdtYWlsLmNvbT4gKHNpbmRyZXNvcmh1cy5jb20pCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCj4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOCj4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBvbi1maW5pc2hlZApMaWNlbnNlOiBNSVQKQnk6IERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uLCBKb25hdGhhbiBPbmcKUmVwb3NpdG9yeToganNodHRwL29uLWZpbmlzaGVkCgo+IChUaGUgTUlUIExpY2Vuc2UpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDEzIEpvbmF0aGFuIE9uZyA8bWVAam9uZ2xlYmVycnkuY29tPgo+IENvcHlyaWdodCAoYykgMjAxNCBEb3VnbGFzIENocmlzdG9waGVyIFdpbHNvbiA8ZG91Z0Bzb21ldGhpbmdkb3VnLmNvbT4KPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcKPiBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUKPiAnU29mdHdhcmUnKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nCj4gd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLAo+IGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0bwo+IHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0bwo+IHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZQo+IGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAnQVMgSVMnLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELAo+IEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRgo+IE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4KPiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWQo+IENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsCj4gVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUKPiBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgcGFyc2U1CkxpY2Vuc2U6IE1JVApCeTogSXZhbiBOaWt1bGluLCBodHRwczovL2dpdGh1Yi5jb20vaW5pa3VsaW4vcGFyc2U1L2dyYXBocy9jb250cmlidXRvcnMKUmVwb3NpdG9yeTogZ2l0Oi8vZ2l0aHViLmNvbS9pbmlrdWxpbi9wYXJzZTUuZ2l0Cgo+IENvcHlyaWdodCAoYykgMjAxMy0yMDE5IEl2YW4gTmlrdWxpbiAoaWZhYWFuQGdtYWlsLmNvbSwgaHR0cHM6Ly9naXRodWIuY29tL2luaWt1bGluKQo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbgo+IGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTgo+IFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgcGFyc2V1cmwKTGljZW5zZTogTUlUCkJ5OiBEb3VnbGFzIENocmlzdG9waGVyIFdpbHNvbiwgSm9uYXRoYW4gT25nClJlcG9zaXRvcnk6IHBpbGxhcmpzL3BhcnNldXJsCgo+IChUaGUgTUlUIExpY2Vuc2UpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDE0IEpvbmF0aGFuIE9uZyA8bWVAam9uZ2xlYmVycnkuY29tPgo+IENvcHlyaWdodCAoYykgMjAxNC0yMDE3IERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uIDxkb3VnQHNvbWV0aGluZ2RvdWcuY29tPgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZwo+IGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZQo+ICdTb2Z0d2FyZScpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcKPiB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsCj4gZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvCj4gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvCj4gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlCj4gaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICdBUyBJUycsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsCj4gRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GCj4gTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULgo+IElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZCj4gQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwKPiBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRQo+IFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBwYXRoLWtleSwgc2hlYmFuZy1yZWdleApMaWNlbnNlOiBNSVQKQnk6IFNpbmRyZSBTb3JodXMKUmVwb3NpdG9yaWVzOiBzaW5kcmVzb3JodXMvcGF0aC1rZXksIHNpbmRyZXNvcmh1cy9zaGViYW5nLXJlZ2V4Cgo+IE1JVCBMaWNlbnNlCj4gCj4gQ29weXJpZ2h0IChjKSBTaW5kcmUgU29yaHVzIDxzaW5kcmVzb3JodXNAZ21haWwuY29tPiAoc2luZHJlc29yaHVzLmNvbSkKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHBlcmlzY29waWMKTGljZW5zZTogTUlUClJlcG9zaXRvcnk6IFJpY2gtSGFycmlzL3BlcmlzY29waWMKCj4gQ29weXJpZ2h0IChjKSAyMDE5IFJpY2ggSGFycmlzCj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBwaWNvY29sb3JzCkxpY2Vuc2U6IElTQwpCeTogQWxleGV5IFJhc3BvcG92ClJlcG9zaXRvcnk6IGFsZXhleXJhc3BvcG92L3BpY29jb2xvcnMKCj4gSVNDIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMjEtMjAyNCBPbGVrc2lpIFJhc3BvcG92LCBLb3N0aWFudHluIERlbnlzb3YsIEFudG9uIFZlcmlub3YKPiAKPiBQZXJtaXNzaW9uIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBhbmQvb3IgZGlzdHJpYnV0ZSB0aGlzIHNvZnR3YXJlIGZvciBhbnkKPiBwdXJwb3NlIHdpdGggb3Igd2l0aG91dCBmZWUgaXMgaGVyZWJ5IGdyYW50ZWQsIHByb3ZpZGVkIHRoYXQgdGhlIGFib3ZlCj4gY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBhcHBlYXIgaW4gYWxsIGNvcGllcy4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiBBTkQgVEhFIEFVVEhPUiBESVNDTEFJTVMgQUxMIFdBUlJBTlRJRVMKPiBXSVRIIFJFR0FSRCBUTyBUSElTIFNPRlRXQVJFIElOQ0xVRElORyBBTEwgSU1QTElFRCBXQVJSQU5USUVTIE9GCj4gTUVSQ0hBTlRBQklMSVRZIEFORCBGSVRORVNTLiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SIEJFIExJQUJMRSBGT1IKPiBBTlkgU1BFQ0lBTCwgRElSRUNULCBJTkRJUkVDVCwgT1IgQ09OU0VRVUVOVElBTCBEQU1BR0VTIE9SIEFOWSBEQU1BR0VTCj4gV0hBVFNPRVZFUiBSRVNVTFRJTkcgRlJPTSBMT1NTIE9GIFVTRSwgREFUQSBPUiBQUk9GSVRTLCBXSEVUSEVSIElOIEFOCj4gQUNUSU9OIE9GIENPTlRSQUNULCBORUdMSUdFTkNFIE9SIE9USEVSIFRPUlRJT1VTIEFDVElPTiwgQVJJU0lORyBPVVQgT0YKPiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFVTRSBPUiBQRVJGT1JNQU5DRSBPRiBUSElTIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBwb3N0Y3NzLWltcG9ydApMaWNlbnNlOiBNSVQKQnk6IE1heGltZSBUaGlyb3VpbgpSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vcG9zdGNzcy9wb3N0Y3NzLWltcG9ydC5naXQKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDE0IE1heGltZSBUaGlyb3VpbiwgSmFzb24gQ2FtcGJlbGwgJiBLZXZpbiBNw6VydGVuc3Nvbgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YKPiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbgo+IHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8KPiB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZgo+IHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywKPiBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MKPiBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IKPiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIKPiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTgo+IENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHBvc3Rjc3MtbG9hZC1jb25maWcKTGljZW5zZTogTUlUCkJ5OiBNaWNoYWVsIENpbmlhd2t5LCBSeWFuIER1bmNrZWwsIE1hdGV1c3ogRGVya3MsIERhbHRvbiBTYW50b3MsIFBhdHJpY2sgR2lsZGF5LCBGcmFuw6dvaXMgV291dHMKUmVwb3NpdG9yeTogcG9zdGNzcy9wb3N0Y3NzLWxvYWQtY29uZmlnCgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+IAo+IENvcHlyaWdodCBNaWNoYWVsIENpbmlhd3NreSA8bWljaGFlbC5jaW5pYXdza3lAZ21haWwuY29tPgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YKPiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbgo+IHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8KPiB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZgo+IHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywKPiBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MKPiBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IKPiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIKPiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTgo+IENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHBvc3Rjc3MtbW9kdWxlcwpMaWNlbnNlOiBNSVQKQnk6IEFsZXhhbmRlciBNYWR5YW5raW4KUmVwb3NpdG9yeTogaHR0cHM6Ly9naXRodWIuY29tL2Nzcy1tb2R1bGVzL3Bvc3Rjc3MtbW9kdWxlcy5naXQKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4gCj4gQ29weXJpZ2h0IDIwMTUtcHJlc2VudCBBbGV4YW5kZXIgTWFkeWFua2luIDxhbGV4YW5kZXJAbWFkeWFua2luLm5hbWU+Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZgo+IHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsIGluCj4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0bwo+IHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mCj4gdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLAo+IHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAo+IGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUwo+IEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUgo+IENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUgo+IElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOCj4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgcG9zdGNzcy1tb2R1bGVzLWV4dHJhY3QtaW1wb3J0cwpMaWNlbnNlOiBJU0MKQnk6IEdsZW4gTWFkZGVybgpSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vY3NzLW1vZHVsZXMvcG9zdGNzcy1tb2R1bGVzLWV4dHJhY3QtaW1wb3J0cy5naXQKCj4gQ29weXJpZ2h0IDIwMTUgR2xlbiBNYWRkZXJuCj4gCj4gUGVybWlzc2lvbiB0byB1c2UsIGNvcHksIG1vZGlmeSwgYW5kL29yIGRpc3RyaWJ1dGUgdGhpcyBzb2Z0d2FyZSBmb3IgYW55IHB1cnBvc2Ugd2l0aCBvciB3aXRob3V0IGZlZSBpcyBoZXJlYnkgZ3JhbnRlZCwgcHJvdmlkZWQgdGhhdCB0aGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBhcHBlYXIgaW4gYWxsIGNvcGllcy4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiBBTkQgVEhFIEFVVEhPUiBESVNDTEFJTVMgQUxMIFdBUlJBTlRJRVMgV0lUSCBSRUdBUkQgVE8gVEhJUyBTT0ZUV0FSRSBJTkNMVURJTkcgQUxMIElNUExJRUQgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1IgQkUgTElBQkxFIEZPUiBBTlkgU1BFQ0lBTCwgRElSRUNULCBJTkRJUkVDVCwgT1IgQ09OU0VRVUVOVElBTCBEQU1BR0VTIE9SIEFOWSBEQU1BR0VTIFdIQVRTT0VWRVIgUkVTVUxUSU5HIEZST00gTE9TUyBPRiBVU0UsIERBVEEgT1IgUFJPRklUUywgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIE5FR0xJR0VOQ0UgT1IgT1RIRVIgVE9SVElPVVMgQUNUSU9OLCBBUklTSU5HIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFVTRSBPUiBQRVJGT1JNQU5DRSBPRiBUSElTIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBwb3N0Y3NzLW1vZHVsZXMtbG9jYWwtYnktZGVmYXVsdApMaWNlbnNlOiBNSVQKQnk6IE1hcmsgRGFsZ2xlaXNoClJlcG9zaXRvcnk6IGh0dHBzOi8vZ2l0aHViLmNvbS9jc3MtbW9kdWxlcy9wb3N0Y3NzLW1vZHVsZXMtbG9jYWwtYnktZGVmYXVsdC5naXQKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4gCj4gQ29weXJpZ2h0IDIwMTUgTWFyayBEYWxnbGVpc2ggPG1hcmsuam9obi5kYWxnbGVpc2hAZ21haWwuY29tPgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YKPiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbgo+IHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8KPiB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZgo+IHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywKPiBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MKPiBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IKPiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIKPiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTgo+IENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHBvc3Rjc3MtbW9kdWxlcy1zY29wZQpMaWNlbnNlOiBJU0MKQnk6IEdsZW4gTWFkZGVybgpSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vY3NzLW1vZHVsZXMvcG9zdGNzcy1tb2R1bGVzLXNjb3BlLmdpdAoKPiBJU0MgTGljZW5zZSAoSVNDKQo+IAo+IENvcHlyaWdodCAoYykgMjAxNSwgR2xlbiBNYWRkZXJuCj4gCj4gUGVybWlzc2lvbiB0byB1c2UsIGNvcHksIG1vZGlmeSwgYW5kL29yIGRpc3RyaWJ1dGUgdGhpcyBzb2Z0d2FyZSBmb3IgYW55IHB1cnBvc2Ugd2l0aCBvciB3aXRob3V0IGZlZSBpcyBoZXJlYnkgZ3JhbnRlZCwgcHJvdmlkZWQgdGhhdCB0aGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBhcHBlYXIgaW4gYWxsIGNvcGllcy4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiBBTkQgVEhFIEFVVEhPUiBESVNDTEFJTVMgQUxMIFdBUlJBTlRJRVMgV0lUSCBSRUdBUkQgVE8gVEhJUyBTT0ZUV0FSRSBJTkNMVURJTkcgQUxMIElNUExJRUQgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1IgQkUgTElBQkxFIEZPUiBBTlkgU1BFQ0lBTCwgRElSRUNULCBJTkRJUkVDVCwgT1IgQ09OU0VRVUVOVElBTCBEQU1BR0VTIE9SIEFOWSBEQU1BR0VTIFdIQVRTT0VWRVIgUkVTVUxUSU5HIEZST00gTE9TUyBPRiBVU0UsIERBVEEgT1IgUFJPRklUUywgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIE5FR0xJR0VOQ0UgT1IgT1RIRVIgVE9SVElPVVMgQUNUSU9OLCBBUklTSU5HIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFVTRSBPUiBQRVJGT1JNQU5DRSBPRiBUSElTIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBwb3N0Y3NzLW1vZHVsZXMtdmFsdWVzCkxpY2Vuc2U6IElTQwpCeTogR2xlbiBNYWRkZXJuClJlcG9zaXRvcnk6IGdpdCtodHRwczovL2dpdGh1Yi5jb20vY3NzLW1vZHVsZXMvcG9zdGNzcy1tb2R1bGVzLXZhbHVlcy5naXQKCj4gSVNDIExpY2Vuc2UgKElTQykKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTUsIEdsZW4gTWFkZGVybgo+IAo+IFBlcm1pc3Npb24gdG8gdXNlLCBjb3B5LCBtb2RpZnksIGFuZC9vciBkaXN0cmlidXRlIHRoaXMgc29mdHdhcmUgZm9yIGFueSBwdXJwb3NlIHdpdGggb3Igd2l0aG91dCBmZWUgaXMgaGVyZWJ5IGdyYW50ZWQsIHByb3ZpZGVkIHRoYXQgdGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2UgYXBwZWFyIGluIGFsbCBjb3BpZXMuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIgQU5EIFRIRSBBVVRIT1IgRElTQ0xBSU1TIEFMTCBXQVJSQU5USUVTIFdJVEggUkVHQVJEIFRPIFRISVMgU09GVFdBUkUgSU5DTFVESU5HIEFMTCBJTVBMSUVEIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZIEFORCBGSVRORVNTLiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SIEJFIExJQUJMRSBGT1IgQU5ZIFNQRUNJQUwsIERJUkVDVCwgSU5ESVJFQ1QsIE9SIENPTlNFUVVFTlRJQUwgREFNQUdFUyBPUiBBTlkgREFNQUdFUyBXSEFUU09FVkVSIFJFU1VMVElORyBGUk9NIExPU1MgT0YgVVNFLCBEQVRBIE9SIFBST0ZJVFMsIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBORUdMSUdFTkNFIE9SIE9USEVSIFRPUlRJT1VTIEFDVElPTiwgQVJJU0lORyBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBVU0UgT1IgUEVSRk9STUFOQ0UgT0YgVEhJUyBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgcG9zdGNzcy1zZWxlY3Rvci1wYXJzZXIKTGljZW5zZTogTUlUCkJ5OiBCZW4gQnJpZ2dzLCBDaHJpcyBFcHBzdGVpbgpSZXBvc2l0b3J5OiBwb3N0Y3NzL3Bvc3Rjc3Mtc2VsZWN0b3ItcGFyc2VyCgo+IENvcHlyaWdodCAoYykgQmVuIEJyaWdncyA8YmVuZWIuaW5mb0BnbWFpbC5jb20+IChodHRwOi8vYmVuZWIuaW5mbykKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbgo+IG9idGFpbmluZyBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uCj4gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dAo+IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLAo+IGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlCj4gU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcKPiBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlCj4gaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsCj4gRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTCj4gT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQKPiBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVAo+IEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLAo+IFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORwo+IEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IKPiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHBvc3Rjc3MtdmFsdWUtcGFyc2VyCkxpY2Vuc2U6IE1JVApCeTogQm9nZGFuIENoYWRraW4KUmVwb3NpdG9yeTogaHR0cHM6Ly9naXRodWIuY29tL1RyeVNvdW5kL3Bvc3Rjc3MtdmFsdWUtcGFyc2VyLmdpdAoKPiBDb3B5cmlnaHQgKGMpIEJvZ2RhbiBDaGFka2luIDx0cnlzb3VuZEB5YW5kZXgucnU+Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24KPiBvYnRhaW5pbmcgYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbgo+IGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQKPiByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwKPiBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZQo+IFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nCj4gY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZQo+IGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELAo+IEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUwo+IE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5ECj4gTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQKPiBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwKPiBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcKPiBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SCj4gT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyByZWFkZGlycApMaWNlbnNlOiBNSVQKQnk6IFRob3JzdGVuIExvcmVueiwgUGF1bCBNaWxsZXIKUmVwb3NpdG9yeTogZ2l0Oi8vZ2l0aHViLmNvbS9wYXVsbWlsbHIvcmVhZGRpcnAuZ2l0Cgo+IE1JVCBMaWNlbnNlCj4gCj4gQ29weXJpZ2h0IChjKSAyMDEyLTIwMTkgVGhvcnN0ZW4gTG9yZW56LCBQYXVsIE1pbGxlciAoaHR0cHM6Ly9wYXVsbWlsbHIuY29tKQo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgcmVzb2x2ZS5leHBvcnRzLCB0b3RhbGlzdApMaWNlbnNlOiBNSVQKQnk6IEx1a2UgRWR3YXJkcwpSZXBvc2l0b3JpZXM6IGx1a2VlZC9yZXNvbHZlLmV4cG9ydHMsIGx1a2VlZC90b3RhbGlzdAoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIEx1a2UgRWR3YXJkcyA8bHVrZS5lZHdhcmRzMDVAZ21haWwuY29tPiAobHVrZWVkLmNvbSkKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHNoZWJhbmctY29tbWFuZApMaWNlbnNlOiBNSVQKQnk6IEtldmluIE3DpXJ0ZW5zc29uClJlcG9zaXRvcnk6IGtldnZhL3NoZWJhbmctY29tbWFuZAoKPiBNSVQgTGljZW5zZQo+IAo+IENvcHlyaWdodCAoYykgS2V2aW4gTcOlcnRlbnNzb24gPGtldmlubWFydGVuc3NvbkBnbWFpbC5jb20+IChnaXRodWIuY29tL2tldnZhKQo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgc2lydgpMaWNlbnNlOiBNSVQKQnk6IEx1a2UgRWR3YXJkcwpSZXBvc2l0b3J5OiBsdWtlZWQvc2lydgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBzdGF0dXNlcwpMaWNlbnNlOiBNSVQKQnk6IERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uLCBKb25hdGhhbiBPbmcKUmVwb3NpdG9yeToganNodHRwL3N0YXR1c2VzCgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+IAo+IENvcHlyaWdodCAoYykgMjAxNCBKb25hdGhhbiBPbmcgPG1lQGpvbmdsZWJlcnJ5LmNvbT4KPiBDb3B5cmlnaHQgKGMpIDIwMTYgRG91Z2xhcyBDaHJpc3RvcGhlciBXaWxzb24gPGRvdWdAc29tZXRoaW5nZG91Zy5jb20+Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCj4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOCj4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBzdHJpbmctaGFzaApMaWNlbnNlOiBDQzAtMS4wCkJ5OiBUaGUgRGFyayBTa3kgQ29tcGFueQpSZXBvc2l0b3J5OiBnaXQ6Ly9naXRodWIuY29tL2Rhcmtza3lhcHAvc3RyaW5nLWhhc2guZ2l0CgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHN0cmlwLWxpdGVyYWwKTGljZW5zZTogTUlUCkJ5OiBBbnRob255IEZ1ClJlcG9zaXRvcnk6IGdpdCtodHRwczovL2dpdGh1Yi5jb20vYW50ZnUvc3RyaXAtbGl0ZXJhbC5naXQKCj4gTUlUIExpY2Vuc2UKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMjIgQW50aG9ueSBGdSA8aHR0cHM6Ly9naXRodWIuY29tL2FudGZ1Pgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgdG8tcmVnZXgtcmFuZ2UKTGljZW5zZTogTUlUCkJ5OiBKb24gU2NobGlua2VydCwgUm91dmVuIFdlw59saW5nClJlcG9zaXRvcnk6IG1pY3JvbWF0Y2gvdG8tcmVnZXgtcmFuZ2UKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4gCj4gQ29weXJpZ2h0IChjKSAyMDE1LXByZXNlbnQsIEpvbiBTY2hsaW5rZXJ0Lgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbgo+IGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTgo+IFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgdHNjb25mY2sKTGljZW5zZTogTUlUCkJ5OiBkb21pbmlrZwpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL2RvbWluaWtnL3RzY29uZmNrLmdpdAoKPiBNSVQgTGljZW5zZQo+IAo+IENvcHlyaWdodCAoYykgMjAyMS1wcmVzZW50IGRvbWluaWtnIGFuZCBbY29udHJpYnV0b3JzXShodHRwczovL2dpdGh1Yi5jb20vZG9taW5pa2cvdHNjb25mY2svZ3JhcGhzL2NvbnRyaWJ1dG9ycykKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFCj4gU09GVFdBUkUuCj4gCj4gLS0gTGljZW5zZXMgZm9yIDNyZC1wYXJ0eSBjb2RlIGluY2x1ZGVkIGluIHRzY29uZmNrIC0tCj4gCj4gIyBzdHJpcC1ib20gYW5kIHN0cmlwLWpzb24tY29tbWVudHMKPiBNSVQgTGljZW5zZQo+IAo+IENvcHlyaWdodCAoYykgU2luZHJlIFNvcmh1cyA8c2luZHJlc29yaHVzQGdtYWlsLmNvbT4gKGh0dHBzOi8vc2luZHJlc29yaHVzLmNvbSkKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFCj4gU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHVucGlwZQpMaWNlbnNlOiBNSVQKQnk6IERvdWdsYXMgQ2hyaXN0b3BoZXIgV2lsc29uClJlcG9zaXRvcnk6IHN0cmVhbS11dGlscy91bnBpcGUKCj4gKFRoZSBNSVQgTGljZW5zZSkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTUgRG91Z2xhcyBDaHJpc3RvcGhlciBXaWxzb24gPGRvdWdAc29tZXRoaW5nZG91Zy5jb20+Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nCj4gYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlCj4gJ1NvZnR3YXJlJyksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZwo+IHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwKPiBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8KPiBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8KPiB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUKPiBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgJ0FTIElTJywgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwKPiBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YKPiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuCj4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkKPiBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULAo+IFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFCj4gU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHV0aWwtZGVwcmVjYXRlCkxpY2Vuc2U6IE1JVApCeTogTmF0aGFuIFJhamxpY2gKUmVwb3NpdG9yeTogZ2l0Oi8vZ2l0aHViLmNvbS9Ub29UYWxsTmF0ZS91dGlsLWRlcHJlY2F0ZS5naXQKCj4gKFRoZSBNSVQgTGljZW5zZSkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTQgTmF0aGFuIFJhamxpY2ggPG5hdGhhbkB0b290YWxsbmF0ZS5uZXQ+Cj4gCj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24KPiBvYnRhaW5pbmcgYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbgo+IGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQKPiByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwKPiBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZQo+IFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nCj4gY29uZGl0aW9uczoKPiAKPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZQo+IGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+IAo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELAo+IEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUwo+IE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5ECj4gTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQKPiBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwKPiBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcKPiBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SCj4gT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyB1dGlscy1tZXJnZQpMaWNlbnNlOiBNSVQKQnk6IEphcmVkIEhhbnNvbgpSZXBvc2l0b3J5OiBnaXQ6Ly9naXRodWIuY29tL2phcmVkaGFuc29uL3V0aWxzLW1lcmdlLmdpdAoKPiBUaGUgTUlUIExpY2Vuc2UgKE1JVCkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTMtMjAxNyBKYXJlZCBIYW5zb24KPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mCj4gdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4KPiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvCj4gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YKPiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sCj4gc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTCj4gRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SCj4gQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSCj4gSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4KPiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyB2YXJ5CkxpY2Vuc2U6IE1JVApCeTogRG91Z2xhcyBDaHJpc3RvcGhlciBXaWxzb24KUmVwb3NpdG9yeToganNodHRwL3ZhcnkKCj4gKFRoZSBNSVQgTGljZW5zZSkKPiAKPiBDb3B5cmlnaHQgKGMpIDIwMTQtMjAxNyBEb3VnbGFzIENocmlzdG9waGVyIFdpbHNvbgo+IAo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZwo+IGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZQo+ICdTb2Z0d2FyZScpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcKPiB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsCj4gZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvCj4gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvCj4gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+IAo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlCj4gaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4gCj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICdBUyBJUycsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsCj4gRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GCj4gTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULgo+IElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZCj4gQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwKPiBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRQo+IFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyB3cwpMaWNlbnNlOiBNSVQKQnk6IEVpbmFyIE90dG8gU3Rhbmd2aWsKUmVwb3NpdG9yeTogZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS93ZWJzb2NrZXRzL3dzLmdpdAoKPiBDb3B5cmlnaHQgKGMpIDIwMTEgRWluYXIgT3R0byBTdGFuZ3ZpayA8ZWluYXJvc0BnbWFpbC5jb20+Cj4gQ29weXJpZ2h0IChjKSAyMDEzIEFybm91dCBLYXplbWllciBhbmQgY29udHJpYnV0b3JzCj4gQ29weXJpZ2h0IChjKSAyMDE2IEx1aWdpIFBpbmNhIGFuZCBjb250cmlidXRvcnMKPiAKPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mCj4gdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4KPiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvCj4gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YKPiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sCj4gc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4gCj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPiAKPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTCj4gRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SCj4gQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSCj4gSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4KPiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|vitest@3.2.4">
      <author>Anthony Fu</author>
      <name>vitest</name>
      <version>3.2.4</version>
      <description>Next generation testing framework powered by Vite</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/vitest@3.2.4#packages/vitest</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/vitest-dev/vitest.git#packages/vitest</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/vitest-dev/vitest#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/vitest-dev/vitest/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/vitest/-/vitest-3.2.4.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">2d408fe5ebf7194443cac4d688fe3bc11454a4b28c39f3e1fb2293c779152048aee4a38c7aace99d836c2b23a856b50b8af47cb4b724b38fa581adf75a19fdd0</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:development">true</property>
        <property name="cdx:npm:package:path">node_modules/vitest</property>
      </properties>
      <components>
        <component type="library" bom-ref="openbb-platform@1.0.0|vitest@3.2.4|picomatch@4.0.3">
          <author>Jon Schlinkert</author>
          <name>picomatch</name>
          <version>4.0.3</version>
          <description>Blazing fast and accurate glob matcher written in JavaScript, with no dependencies and full support for standard and extended Bash glob features, including braces, extglobs, POSIX brackets, and regular expressions.</description>
          <licenses>
            <license acknowledgement="declared">
              <id>MIT</id>
            </license>
          </licenses>
          <purl>pkg:npm/picomatch@4.0.3</purl>
          <externalReferences>
            <reference type="vcs">
              <url>git+https://github.com/micromatch/picomatch.git</url>
              <comment>as detected from PackageJson property "repository.url"</comment>
            </reference>
            <reference type="website">
              <url>https://github.com/micromatch/picomatch</url>
              <comment>as detected from PackageJson property "homepage"</comment>
            </reference>
            <reference type="issue-tracker">
              <url>https://github.com/micromatch/picomatch/issues</url>
              <comment>as detected from PackageJson property "bugs.url"</comment>
            </reference>
            <reference type="distribution">
              <url>https://registry.npmjs.org/picomatch/-/picomatch-4.0.3.tgz</url>
              <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
              <hashes>
                <hash alg="SHA-512">e604e680463fb2a2ba8055cb22c40d1f5f6559be1e6cf0cb03849d2cfeddb169085c75a51baea83ee56f5d21853e9a58673f190d9ab475862b6c77c109551bd5</hash>
              </hashes>
            </reference>
          </externalReferences>
          <properties>
            <property name="cdx:npm:package:development">true</property>
            <property name="cdx:npm:package:path">node_modules/vitest/node_modules/picomatch</property>
          </properties>
          <evidence>
            <licenses>
              <license>
                <name>file: LICENSE</name>
                <text content-type="text/plain" encoding="base64">VGhlIE1JVCBMaWNlbnNlIChNSVQpCgpDb3B5cmlnaHQgKGMpIDIwMTctcHJlc2VudCwgSm9uIFNjaGxpbmtlcnQuCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCmFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KVEhFIFNPRlRXQVJFLgo=</text>
              </license>
            </licenses>
          </evidence>
        </component>
      </components>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE.md</name>
            <text content-type="text/markdown" encoding="base64">IyBWaXRlc3QgY29yZSBsaWNlbnNlClZpdGVzdCBpcyByZWxlYXNlZCB1bmRlciB0aGUgTUlUIGxpY2Vuc2U6CgpNSVQgTGljZW5zZQoKQ29weXJpZ2h0IChjKSAyMDIxLVByZXNlbnQgVml0ZXN0IFRlYW0KClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCgojIExpY2Vuc2VzIG9mIGJ1bmRsZWQgZGVwZW5kZW5jaWVzClRoZSBwdWJsaXNoZWQgVml0ZXN0IGFydGlmYWN0IGFkZGl0aW9uYWxseSBjb250YWlucyBjb2RlIHdpdGggdGhlIGZvbGxvd2luZyBsaWNlbnNlczoKQlNELTMtQ2xhdXNlLCBJU0MsIE1JVAoKIyBCdW5kbGVkIGRlcGVuZGVuY2llczoKIyMgQGFudGZ1L2luc3RhbGwtcGtnCkxpY2Vuc2U6IE1JVApCeTogQW50aG9ueSBGdQpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL2FudGZ1L2luc3RhbGwtcGtnLmdpdAoKPiBNSVQgTGljZW5zZQo+Cj4gQ29weXJpZ2h0IChjKSAyMDIxIEFudGhvbnkgRnUgPGh0dHBzOi8vZ2l0aHViLmNvbS9hbnRmdT4KPgo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPgo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAo+IGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4KPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFCj4gU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIEBzaW5vbmpzL2NvbW1vbnMKTGljZW5zZTogQlNELTMtQ2xhdXNlClJlcG9zaXRvcnk6IGdpdCtodHRwczovL2dpdGh1Yi5jb20vc2lub25qcy9jb21tb25zLmdpdAoKPiBCU0QgMy1DbGF1c2UgTGljZW5zZQo+Cj4gQ29weXJpZ2h0IChjKSAyMDE4LCBTaW5vbi5KUwo+IEFsbCByaWdodHMgcmVzZXJ2ZWQuCj4KPiBSZWRpc3RyaWJ1dGlvbiBhbmQgdXNlIGluIHNvdXJjZSBhbmQgYmluYXJ5IGZvcm1zLCB3aXRoIG9yIHdpdGhvdXQKPiBtb2RpZmljYXRpb24sIGFyZSBwZXJtaXR0ZWQgcHJvdmlkZWQgdGhhdCB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnMgYXJlIG1ldDoKPgo+ICogUmVkaXN0cmlidXRpb25zIG9mIHNvdXJjZSBjb2RlIG11c3QgcmV0YWluIHRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlLCB0aGlzCj4gICBsaXN0IG9mIGNvbmRpdGlvbnMgYW5kIHRoZSBmb2xsb3dpbmcgZGlzY2xhaW1lci4KPgo+ICogUmVkaXN0cmlidXRpb25zIGluIGJpbmFyeSBmb3JtIG11c3QgcmVwcm9kdWNlIHRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlLAo+ICAgdGhpcyBsaXN0IG9mIGNvbmRpdGlvbnMgYW5kIHRoZSBmb2xsb3dpbmcgZGlzY2xhaW1lciBpbiB0aGUgZG9jdW1lbnRhdGlvbgo+ICAgYW5kL29yIG90aGVyIG1hdGVyaWFscyBwcm92aWRlZCB3aXRoIHRoZSBkaXN0cmlidXRpb24uCj4KPiAqIE5laXRoZXIgdGhlIG5hbWUgb2YgdGhlIGNvcHlyaWdodCBob2xkZXIgbm9yIHRoZSBuYW1lcyBvZiBpdHMKPiAgIGNvbnRyaWJ1dG9ycyBtYXkgYmUgdXNlZCB0byBlbmRvcnNlIG9yIHByb21vdGUgcHJvZHVjdHMgZGVyaXZlZCBmcm9tCj4gICB0aGlzIHNvZnR3YXJlIHdpdGhvdXQgc3BlY2lmaWMgcHJpb3Igd3JpdHRlbiBwZXJtaXNzaW9uLgo+Cj4gVEhJUyBTT0ZUV0FSRSBJUyBQUk9WSURFRCBCWSBUSEUgQ09QWVJJR0hUIEhPTERFUlMgQU5EIENPTlRSSUJVVE9SUyAiQVMgSVMiCj4gQU5EIEFOWSBFWFBSRVNTIE9SIElNUExJRUQgV0FSUkFOVElFUywgSU5DTFVESU5HLCBCVVQgTk9UIExJTUlURUQgVE8sIFRIRQo+IElNUExJRUQgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFkgQU5EIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFSRQo+IERJU0NMQUlNRUQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBDT1BZUklHSFQgSE9MREVSIE9SIENPTlRSSUJVVE9SUyBCRSBMSUFCTEUKPiBGT1IgQU5ZIERJUkVDVCwgSU5ESVJFQ1QsIElOQ0lERU5UQUwsIFNQRUNJQUwsIEVYRU1QTEFSWSwgT1IgQ09OU0VRVUVOVElBTAo+IERBTUFHRVMgKElOQ0xVRElORywgQlVUIE5PVCBMSU1JVEVEIFRPLCBQUk9DVVJFTUVOVCBPRiBTVUJTVElUVVRFIEdPT0RTIE9SCj4gU0VSVklDRVM7IExPU1MgT0YgVVNFLCBEQVRBLCBPUiBQUk9GSVRTOyBPUiBCVVNJTkVTUyBJTlRFUlJVUFRJT04pIEhPV0VWRVIKPiBDQVVTRUQgQU5EIE9OIEFOWSBUSEVPUlkgT0YgTElBQklMSVRZLCBXSEVUSEVSIElOIENPTlRSQUNULCBTVFJJQ1QgTElBQklMSVRZLAo+IE9SIFRPUlQgKElOQ0xVRElORyBORUdMSUdFTkNFIE9SIE9USEVSV0lTRSkgQVJJU0lORyBJTiBBTlkgV0FZIE9VVCBPRiBUSEUgVVNFCj4gT0YgVEhJUyBTT0ZUV0FSRSwgRVZFTiBJRiBBRFZJU0VEIE9GIFRIRSBQT1NTSUJJTElUWSBPRiBTVUNIIERBTUFHRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgQHNpbm9uanMvZmFrZS10aW1lcnMKTGljZW5zZTogQlNELTMtQ2xhdXNlCkJ5OiBDaHJpc3RpYW4gSm9oYW5zZW4KUmVwb3NpdG9yeTogZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS9zaW5vbmpzL2Zha2UtdGltZXJzLmdpdAoKPiBDb3B5cmlnaHQgKGMpIDIwMTAtMjAxNCwgQ2hyaXN0aWFuIEpvaGFuc2VuLCBjaHJpc3RpYW5AY2pvaGFuc2VuLm5vLiBBbGwgcmlnaHRzIHJlc2VydmVkLgo+Cj4gUmVkaXN0cmlidXRpb24gYW5kIHVzZSBpbiBzb3VyY2UgYW5kIGJpbmFyeSBmb3Jtcywgd2l0aCBvciB3aXRob3V0IG1vZGlmaWNhdGlvbiwgYXJlIHBlcm1pdHRlZCBwcm92aWRlZCB0aGF0IHRoZSBmb2xsb3dpbmcgY29uZGl0aW9ucyBhcmUgbWV0Ogo+Cj4gMS4gUmVkaXN0cmlidXRpb25zIG9mIHNvdXJjZSBjb2RlIG11c3QgcmV0YWluIHRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlLCB0aGlzIGxpc3Qgb2YgY29uZGl0aW9ucyBhbmQgdGhlIGZvbGxvd2luZyBkaXNjbGFpbWVyLgo+Cj4gMi4gUmVkaXN0cmlidXRpb25zIGluIGJpbmFyeSBmb3JtIG11c3QgcmVwcm9kdWNlIHRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlLCB0aGlzIGxpc3Qgb2YgY29uZGl0aW9ucyBhbmQgdGhlIGZvbGxvd2luZyBkaXNjbGFpbWVyIGluIHRoZSBkb2N1bWVudGF0aW9uIGFuZC9vciBvdGhlciBtYXRlcmlhbHMgcHJvdmlkZWQgd2l0aCB0aGUgZGlzdHJpYnV0aW9uLgo+Cj4gMy4gTmVpdGhlciB0aGUgbmFtZSBvZiB0aGUgY29weXJpZ2h0IGhvbGRlciBub3IgdGhlIG5hbWVzIG9mIGl0cyBjb250cmlidXRvcnMgbWF5IGJlIHVzZWQgdG8gZW5kb3JzZSBvciBwcm9tb3RlIHByb2R1Y3RzIGRlcml2ZWQgZnJvbSB0aGlzIHNvZnR3YXJlIHdpdGhvdXQgc3BlY2lmaWMgcHJpb3Igd3JpdHRlbiBwZXJtaXNzaW9uLgo+Cj4gVEhJUyBTT0ZUV0FSRSBJUyBQUk9WSURFRCBCWSBUSEUgQ09QWVJJR0hUIEhPTERFUlMgQU5EIENPTlRSSUJVVE9SUyAiQVMgSVMiIEFORCBBTlkgRVhQUkVTUyBPUiBJTVBMSUVEIFdBUlJBTlRJRVMsIElOQ0xVRElORywgQlVUIE5PVCBMSU1JVEVEIFRPLCBUSEUgSU1QTElFRCBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSBBTkQgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQVJFIERJU0NMQUlNRUQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBDT1BZUklHSFQgSE9MREVSIE9SIENPTlRSSUJVVE9SUyBCRSBMSUFCTEUgRk9SIEFOWSBESVJFQ1QsIElORElSRUNULCBJTkNJREVOVEFMLCBTUEVDSUFMLCBFWEVNUExBUlksIE9SIENPTlNFUVVFTlRJQUwgREFNQUdFUyAoSU5DTFVESU5HLCBCVVQgTk9UIExJTUlURUQgVE8sIFBST0NVUkVNRU5UIE9GIFNVQlNUSVRVVEUgR09PRFMgT1IgU0VSVklDRVM7IExPU1MgT0YgVVNFLCBEQVRBLCBPUiBQUk9GSVRTOyBPUiBCVVNJTkVTUyBJTlRFUlJVUFRJT04pIEhPV0VWRVIgQ0FVU0VEIEFORCBPTiBBTlkgVEhFT1JZIE9GIExJQUJJTElUWSwgV0hFVEhFUiBJTiBDT05UUkFDVCwgU1RSSUNUIExJQUJJTElUWSwgT1IgVE9SVCAoSU5DTFVESU5HIE5FR0xJR0VOQ0UgT1IgT1RIRVJXSVNFKSBBUklTSU5HIElOIEFOWSBXQVkgT1VUIE9GIFRIRSBVU0UgT0YgVEhJUyBTT0ZUV0FSRSwgRVZFTiBJRiBBRFZJU0VEIE9GIFRIRSBQT1NTSUJJTElUWSBPRiBTVUNIIERBTUFHRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgYWNvcm4td2FsawpMaWNlbnNlOiBNSVQKQnk6IE1hcmlqbiBIYXZlcmJla2UsIEluZ3ZhciBTdGVwYW55YW4sIEFkcmlhbiBIZWluZQpSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vYWNvcm5qcy9hY29ybi5naXQKCj4gTUlUIExpY2Vuc2UKPgo+IENvcHlyaWdodCAoQykgMjAxMi0yMDIwIGJ5IHZhcmlvdXMgY29udHJpYnV0b3JzIChzZWUgQVVUSE9SUykKPgo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPgo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCj4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4KPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGJpcnBjCkxpY2Vuc2U6IE1JVApCeTogQW50aG9ueSBGdQpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL2FudGZ1L2JpcnBjLmdpdAoKPiBNSVQgTGljZW5zZQo+Cj4gQ29weXJpZ2h0IChjKSAyMDIxIEFudGhvbnkgRnUgPGh0dHBzOi8vZ2l0aHViLmNvbS9hbnRmdT4KPgo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPgo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAo+IGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4KPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFCj4gU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGNhYwpMaWNlbnNlOiBNSVQKQnk6IGVnb2lzdApSZXBvc2l0b3J5OiBlZ29pc3QvY2FjCgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+Cj4gQ29weXJpZ2h0IChjKSBFR09JU1QgPDB4MTQyODU3QGdtYWlsLmNvbT4gKGh0dHBzOi8vZ2l0aHViLmNvbS9lZ29pc3QpCj4KPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4KPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbgo+IGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOCj4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBjaGFpLXN1YnNldApMaWNlbnNlOiBNSVQKQnk6IEFuZHJpaSBTaHVtYWRhLCBSb2JlcnQgSGVyaG9sZApSZXBvc2l0b3J5OiBodHRwczovL2dpdGh1Yi5jb20vZGViaXRvb3IvY2hhaS1zdWJzZXQuZ2l0Cgo+IFRoZSBNSVQgTGljZW5zZSAoTUlUKQo+Cj4gQ29weXJpZ2h0IChjKSAyMDE0IAo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+Cj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgZmluZC11cApMaWNlbnNlOiBNSVQKQnk6IFNpbmRyZSBTb3JodXMKUmVwb3NpdG9yeTogc2luZHJlc29yaHVzL2ZpbmQtdXAKCj4gTUlUIExpY2Vuc2UKPgo+IENvcHlyaWdodCAoYykgU2luZHJlIFNvcmh1cyA8c2luZHJlc29yaHVzQGdtYWlsLmNvbT4gKGh0dHBzOi8vc2luZHJlc29yaHVzLmNvbSkKPgo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkgb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cyB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsIGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+Cj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4KPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIgTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGZsYXR0ZWQKTGljZW5zZTogSVNDCkJ5OiBBbmRyZWEgR2lhbW1hcmNoaQpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL1dlYlJlZmxlY3Rpb24vZmxhdHRlZC5naXQKCj4gSVNDIExpY2Vuc2UKPgo+IENvcHlyaWdodCAoYykgMjAxOC0yMDIwLCBBbmRyZWEgR2lhbW1hcmNoaSwgQFdlYlJlZmxlY3Rpb24KPgo+IFBlcm1pc3Npb24gdG8gdXNlLCBjb3B5LCBtb2RpZnksIGFuZC9vciBkaXN0cmlidXRlIHRoaXMgc29mdHdhcmUgZm9yIGFueQo+IHB1cnBvc2Ugd2l0aCBvciB3aXRob3V0IGZlZSBpcyBoZXJlYnkgZ3JhbnRlZCwgcHJvdmlkZWQgdGhhdCB0aGUgYWJvdmUKPiBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIGFwcGVhciBpbiBhbGwgY29waWVzLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIgQU5EIFRIRSBBVVRIT1IgRElTQ0xBSU1TIEFMTCBXQVJSQU5USUVTIFdJVEgKPiBSRUdBUkQgVE8gVEhJUyBTT0ZUV0FSRSBJTkNMVURJTkcgQUxMIElNUExJRUQgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFkKPiBBTkQgRklUTkVTUy4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFIEFVVEhPUiBCRSBMSUFCTEUgRk9SIEFOWSBTUEVDSUFMLCBESVJFQ1QsCj4gSU5ESVJFQ1QsIE9SIENPTlNFUVVFTlRJQUwgREFNQUdFUyBPUiBBTlkgREFNQUdFUyBXSEFUU09FVkVSIFJFU1VMVElORyBGUk9NCj4gTE9TUyBPRiBVU0UsIERBVEEgT1IgUFJPRklUUywgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIE5FR0xJR0VOQ0UKPiBPUiBPVEhFUiBUT1JUSU9VUyBBQ1RJT04sIEFSSVNJTkcgT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgVVNFIE9SCj4gUEVSRk9STUFOQ0UgT0YgVEhJUyBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMganMtdG9rZW5zCkxpY2Vuc2U6IE1JVApCeTogU2ltb24gTHlkZWxsClJlcG9zaXRvcnk6IGx5ZGVsbC9qcy10b2tlbnMKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4KPiBDb3B5cmlnaHQgKGMpIDIwMTQsIDIwMTUsIDIwMTYsIDIwMTcsIDIwMTgsIDIwMTksIDIwMjAsIDIwMjEsIDIwMjIsIDIwMjMsIDIwMjQgU2ltb24gTHlkZWxsCj4KPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4KPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbgo+IGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOCj4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBrbGV1cgpMaWNlbnNlOiBNSVQKQnk6IEx1a2UgRWR3YXJkcwpSZXBvc2l0b3J5OiBsdWtlZWQva2xldXIKCj4gVGhlIE1JVCBMaWNlbnNlIChNSVQpCj4KPiBDb3B5cmlnaHQgKGMpIEx1a2UgRWR3YXJkcyA8bHVrZS5lZHdhcmRzMDVAZ21haWwuY29tPiAobHVrZWVkLmNvbSkKPgo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPgo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluCj4gYWxsIGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4KPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4KPiBUSEUgU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIGxvY2FsLXBrZwpMaWNlbnNlOiBNSVQKQnk6IEFudGhvbnkgRnUKUmVwb3NpdG9yeTogZ2l0K2h0dHBzOi8vZ2l0aHViLmNvbS9hbnRmdS9sb2NhbC1wa2cuZ2l0Cgo+IE1JVCBMaWNlbnNlCj4KPiBDb3B5cmlnaHQgKGMpIDIwMjEgQW50aG9ueSBGdSA8aHR0cHM6Ly9naXRodWIuY29tL2FudGZ1Pgo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+Cj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgbG9jYXRlLXBhdGgKTGljZW5zZTogTUlUCkJ5OiBTaW5kcmUgU29yaHVzClJlcG9zaXRvcnk6IHNpbmRyZXNvcmh1cy9sb2NhdGUtcGF0aAoKPiBNSVQgTGljZW5zZQo+Cj4gQ29weXJpZ2h0IChjKSBTaW5kcmUgU29yaHVzIDxzaW5kcmVzb3JodXNAZ21haWwuY29tPiAoaHR0cHM6Ly9zaW5kcmVzb3JodXMuY29tKQo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4KPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgbWltZQpMaWNlbnNlOiBNSVQKQnk6IFJvYmVydCBLaWVmZmVyClJlcG9zaXRvcnk6IGh0dHBzOi8vZ2l0aHViLmNvbS9icm9vZmEvbWltZQoKPiBNSVQgTGljZW5zZQo+Cj4gQ29weXJpZ2h0IChjKSAyMDIzIFJvYmVydCBLaWVmZmVyCj4KPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4KPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQo+IFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBtbGx5CkxpY2Vuc2U6IE1JVApSZXBvc2l0b3J5OiB1bmpzL21sbHkKCj4gTUlUIExpY2Vuc2UKPgo+IENvcHlyaWdodCAoYykgUG9veWEgUGFyc2EgPHBvb3lhQHBpMC5pbz4KPgo+IFBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKPiBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAo+IGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKPiB0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCj4gY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCj4gZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPgo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbAo+IGNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCj4KPiBUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgo+IElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLAo+IEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQo+IEFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKPiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLAo+IE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFCj4gU09GVFdBUkUuCgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0KCiMjIHAtbGltaXQKTGljZW5zZTogTUlUCkJ5OiBTaW5kcmUgU29yaHVzClJlcG9zaXRvcnk6IHNpbmRyZXNvcmh1cy9wLWxpbWl0Cgo+IE1JVCBMaWNlbnNlCj4KPiBDb3B5cmlnaHQgKGMpIFNpbmRyZSBTb3JodXMgPHNpbmRyZXNvcmh1c0BnbWFpbC5jb20+IChodHRwczovL3NpbmRyZXNvcmh1cy5jb20pCj4KPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPgo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBwLWxvY2F0ZQpMaWNlbnNlOiBNSVQKQnk6IFNpbmRyZSBTb3JodXMKUmVwb3NpdG9yeTogc2luZHJlc29yaHVzL3AtbG9jYXRlCgo+IE1JVCBMaWNlbnNlCj4KPiBDb3B5cmlnaHQgKGMpIFNpbmRyZSBTb3JodXMgPHNpbmRyZXNvcmh1c0BnbWFpbC5jb20+IChodHRwczovL3NpbmRyZXNvcmh1cy5jb20pCj4KPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsIGluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMgdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMgZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKPgo+IFRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbCBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IgSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksIEZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRSBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sIE9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFIFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBwYWNrYWdlLW1hbmFnZXItZGV0ZWN0b3IKTGljZW5zZTogTUlUCkJ5OiBBbnRob255IEZ1ClJlcG9zaXRvcnk6IGdpdCtodHRwczovL2dpdGh1Yi5jb20vYW50ZnUtY29sbGVjdGl2ZS9wYWNrYWdlLW1hbmFnZXItZGV0ZWN0b3IuZ2l0Cgo+IE1JVCBMaWNlbnNlCj4KPiBDb3B5cmlnaHQgKGMpIDIwMjAtUFJFU0VOVCBBbnRob255IEZ1IDxodHRwczovL2dpdGh1Yi5jb20vYW50ZnU+Cj4KPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4KPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQo+IFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBwcm9tcHRzCkxpY2Vuc2U6IE1JVApCeTogVGVya2VsIEdqZXJ2aWcKUmVwb3NpdG9yeTogdGVya2VsZy9wcm9tcHRzCgo+IE1JVCBMaWNlbnNlCj4KPiBDb3B5cmlnaHQgKGMpIDIwMTggVGVya2VsIEdqZXJ2aWcgTmllbHNlbgo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+Cj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgcXVhbnN5bmMKTGljZW5zZTogTUlUCkJ5OiBBbnRob255IEZ1LCDkuInlkrLmmbrlrZAgS2V2aW4gRGVuZwpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL3F1YW5zeW5jLWRldi9xdWFuc3luYy5naXQKCj4gTUlUIExpY2Vuc2UKPgo+IENvcHlyaWdodCAoYykgMjAyNS1QUkVTRU5UIEFudGhvbnkgRnUgPGh0dHBzOi8vZ2l0aHViLmNvbS9hbnRmdT4gYW5kIEtldmluIERlbmcgPGh0dHBzOi8vZ2l0aHViLmNvbS9zeHp6Pgo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+Cj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgc2lzdGVyYW5zaQpMaWNlbnNlOiBNSVQKQnk6IFRlcmtlbCBHamVydmlnClJlcG9zaXRvcnk6IGh0dHBzOi8vZ2l0aHViLmNvbS90ZXJrZWxnL3Npc3RlcmFuc2kKCj4gTUlUIExpY2Vuc2UKPgo+IENvcHlyaWdodCAoYykgMjAxOCBUZXJrZWwgR2plcnZpZyBOaWVsc2VuCj4KPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cj4gb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKPiBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCj4gdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbAo+IGNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwo+IGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4KPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKPiBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKPiBBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCj4gTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKPiBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQo+IFNPRlRXQVJFLgoKLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tCgojIyBzdHJpcC1saXRlcmFsCkxpY2Vuc2U6IE1JVApCeTogQW50aG9ueSBGdQpSZXBvc2l0b3J5OiBnaXQraHR0cHM6Ly9naXRodWIuY29tL2FudGZ1L3N0cmlwLWxpdGVyYWwuZ2l0Cgo+IE1JVCBMaWNlbnNlCj4KPiBDb3B5cmlnaHQgKGMpIDIwMjIgQW50aG9ueSBGdSA8aHR0cHM6Ly9naXRodWIuY29tL2FudGZ1Pgo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+Cj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgdHlwZS1kZXRlY3QKTGljZW5zZTogTUlUCkJ5OiBKYWtlIEx1ZXIsIEtlaXRoIENpcmtlbCwgRGF2aWQgTG9zZXJ0LCBBbGVrc2V5IFNodmF5a2EsIEx1Y2FzIEZlcm5hbmRlcyBkYSBDb3N0YSwgR3JhbnQgU25vZGdyYXNzLCBKZXJlbXkgVGljZSwgRWR3YXJkIEJldHRzLCBkdmxzZywgQW1pbGEgV2VsaWhpbmRhLCBKYWtlIENoYW1waW9uLCBNaXJvc2xhdiBCYWp0b8WhClJlcG9zaXRvcnk6IGdpdCtzc2g6Ly9naXRAZ2l0aHViLmNvbS9jaGFpanMvdHlwZS1kZXRlY3QuZ2l0Cgo+IENvcHlyaWdodCAoYykgMjAxMyBKYWtlIEx1ZXIgPGpha2VAYWxvZ2ljYWxwYXJhZG94LmNvbT4gKGh0dHA6Ly9hbG9naWNhbHBhcmFkb3guY29tKQo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+Cj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4KPiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTgo+IFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgdWZvCkxpY2Vuc2U6IE1JVApSZXBvc2l0b3J5OiB1bmpzL3VmbwoKPiBNSVQgTGljZW5zZQo+Cj4gQ29weXJpZ2h0IChjKSBQb295YSBQYXJzYSA8cG9veWFAcGkwLmlvPgo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQo+IG9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCj4gaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwo+IHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKPiBjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKPiBmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgo+Cj4gVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCj4gY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCj4gSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCj4gRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCj4gQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgo+IExJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCj4gT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKPiBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgd3MKTGljZW5zZTogTUlUCkJ5OiBFaW5hciBPdHRvIFN0YW5ndmlrClJlcG9zaXRvcnk6IGdpdCtodHRwczovL2dpdGh1Yi5jb20vd2Vic29ja2V0cy93cy5naXQKCj4gQ29weXJpZ2h0IChjKSAyMDExIEVpbmFyIE90dG8gU3Rhbmd2aWsgPGVpbmFyb3NAZ21haWwuY29tPgo+IENvcHlyaWdodCAoYykgMjAxMyBBcm5vdXQgS2F6ZW1pZXIgYW5kIGNvbnRyaWJ1dG9ycwo+IENvcHlyaWdodCAoYykgMjAxNiBMdWlnaSBQaW5jYSBhbmQgY29udHJpYnV0b3JzCj4KPiBQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5IG9mCj4gdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwgaW4KPiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvCj4gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbCBjb3BpZXMgb2YKPiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcyBmdXJuaXNoZWQgdG8gZG8gc28sCj4gc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4KPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKPiBjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgo+Cj4gVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKPiBJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwgRklUTkVTUwo+IEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUgo+IENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSIExJQUJJTElUWSwgV0hFVEhFUgo+IElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwgT1VUIE9GIE9SIElOCj4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLQoKIyMgeW9jdG8tcXVldWUKTGljZW5zZTogTUlUCkJ5OiBTaW5kcmUgU29yaHVzClJlcG9zaXRvcnk6IHNpbmRyZXNvcmh1cy95b2N0by1xdWV1ZQoKPiBNSVQgTGljZW5zZQo+Cj4gQ29weXJpZ2h0IChjKSBTaW5kcmUgU29yaHVzIDxzaW5kcmVzb3JodXNAZ21haWwuY29tPiAoaHR0cHM6Ly9zaW5kcmVzb3JodXMuY29tKQo+Cj4gUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weSBvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbCBpbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzIHRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwgY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzIGZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6Cj4KPiBUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwgY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KPgo+IFRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|zod@3.25.76">
      <author>Colin McDonnell</author>
      <name>zod</name>
      <version>3.25.76</version>
      <description>TypeScript-first schema declaration and validation library with static type inference</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/zod@3.25.76</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/colinhacks/zod.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://zod.dev</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/colinhacks/zod/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/zod/-/zod-3.25.76.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">83352dfeab7cd675ec14628815c0b76277c4031e4d92e9c27e70e5bee0524854b4d9b717bb82e679ad001485306cb5b158fc7777da7c4b94286ae8ca70d43171</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/zod</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyNSBDb2xpbiBNY0Rvbm5lbGwKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-avatar@1.1.10">
      <group>@radix-ui</group>
      <name>react-avatar</name>
      <version>1.1.10</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-avatar@1.1.10</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-avatar/-/react-avatar-1.1.10.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">57ca6215f59aa4ce4e98d0974f355063e135ac36b9df363e310e18ef7e7abf87c5cfabea0b252d233dab503e3864477083bf3f8ca98c2478f4efe0bf67fadca2</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-avatar</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-checkbox@1.3.3">
      <group>@radix-ui</group>
      <name>react-checkbox</name>
      <version>1.3.3</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-checkbox@1.3.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-checkbox/-/react-checkbox-1.3.3.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">c016e9bfe3507ed1c3746f3a41cd292325e4e48477b4cf157749d62ca0dc5fc9cd9f89d714e170b0abaac36a2403fd43fe6a5a0249aeca776b3c94d80cd66d17</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-checkbox</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-dialog@1.1.15">
      <group>@radix-ui</group>
      <name>react-dialog</name>
      <version>1.1.15</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-dialog@1.1.15</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-dialog/-/react-dialog-1.1.15.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">4c2825551b7395f7d137144c132477e831812c9a5ebac15c80c543f4f644cc02a752cd65282817e6ef41982d9883e2cbf4c8190ee80516cd5597e269e2dfcf1b</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-dialog</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-dropdown-menu@2.1.16">
      <group>@radix-ui</group>
      <name>react-dropdown-menu</name>
      <version>2.1.16</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-dropdown-menu@2.1.16</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-dropdown-menu/-/react-dropdown-menu-2.1.16.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">d4f2c6404ca723fdce5ff7ed579e023a7fb74ae77f327f2f00b836ad69c12e745a1ad24376e356ff6d978e51a03dda5c21b890c632ad6fb0647233f4d27a9f27</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-dropdown-menu</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-label@2.1.7">
      <group>@radix-ui</group>
      <name>react-label</name>
      <version>2.1.7</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-label@2.1.7</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-label/-/react-label-2.1.7.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">613d46a8f48bf24267db47637a5317eff713469fd8f70e48647bdfc504d51eb3aa6b6c8c97b8bf51f32a29153957b984c8a4eb5158095e13503d5086f0f04ba1</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-label</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-popover@1.1.15">
      <group>@radix-ui</group>
      <name>react-popover</name>
      <version>1.1.15</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-popover@1.1.15</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-popover/-/react-popover-1.1.15.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">92bd17dbee98cbfbc9ccb60950f09911cf127d071ffb508e16802a6ae266ef8ba6421b5af4cee53491cfed0412def92f7062d051b5a9333c2b5d8c2b633b4728</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-popover</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-radio-group@1.3.8">
      <group>@radix-ui</group>
      <name>react-radio-group</name>
      <version>1.3.8</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-radio-group@1.3.8</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-radio-group/-/react-radio-group-1.3.8.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">541298218226039cecc4009d8ac350dc18c205f99b187de44259c556a956538b57c23cbb7065fcb5af3405cacef96257227e620729441f72ba65395e7bffe581</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-radio-group</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-select@2.2.6">
      <group>@radix-ui</group>
      <name>react-select</name>
      <version>2.2.6</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-select@2.2.6</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-select/-/react-select-2.2.6.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">237d11c9d3be6e79f63d0cedbe8db9b6cc0f1fec050637a1546b666a0914efcc8c7704f055fd76c2700e17e01e3fc4b637cc43fb950f6c686451f3f2bd3fa6c1</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-select</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-slot@1.2.3">
      <group>@radix-ui</group>
      <name>react-slot</name>
      <version>1.2.3</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-slot@1.2.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-slot/-/react-slot-1.2.3.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">69e3661e70716e2d92b746aee950550bb25716584b94e9ef20895e3cd9e2c943400a5ce6b4050463cfe90622b78878ee7ce97003e736d3ff239e0a3bc5cae0f0</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-slot</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-tabs@1.1.13">
      <group>@radix-ui</group>
      <name>react-tabs</name>
      <version>1.1.13</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-tabs@1.1.13</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-tabs/-/react-tabs-1.1.13.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">ef175c6ad83bfd4fbbf94772a23db3a1db48f47fc8228a6aa3e60e21c64eab59c9c1758167da7cc62bb99655e57a40db66471aefd6bf7e8cc46105c8038b16e8</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-tabs</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@radix-ui/react-tooltip@1.2.8">
      <group>@radix-ui</group>
      <name>react-tooltip</name>
      <version>1.2.8</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40radix-ui/react-tooltip@1.2.8</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/radix-ui/primitives.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://radix-ui.com/primitives</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/radix-ui/primitives/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@radix-ui/react-tooltip/-/react-tooltip-1.2.8.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">b58eec56dd722fda33231be66ed379aad987da4ad770109f8c488280a18baae9c91ef82f646d8f725da843791b7190116f50461077642f371818ef329d59627a</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@radix-ui/react-tooltip</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMiBXb3JrT1MKClBlcm1pc3Npb24gaXMgaGVyZWJ5IGdyYW50ZWQsIGZyZWUgb2YgY2hhcmdlLCB0byBhbnkgcGVyc29uIG9idGFpbmluZyBhIGNvcHkKb2YgdGhpcyBzb2Z0d2FyZSBhbmQgYXNzb2NpYXRlZCBkb2N1bWVudGF0aW9uIGZpbGVzICh0aGUgIlNvZnR3YXJlIiksIHRvIGRlYWwKaW4gdGhlIFNvZnR3YXJlIHdpdGhvdXQgcmVzdHJpY3Rpb24sIGluY2x1ZGluZyB3aXRob3V0IGxpbWl0YXRpb24gdGhlIHJpZ2h0cwp0byB1c2UsIGNvcHksIG1vZGlmeSwgbWVyZ2UsIHB1Ymxpc2gsIGRpc3RyaWJ1dGUsIHN1YmxpY2Vuc2UsIGFuZC9vciBzZWxsCmNvcGllcyBvZiB0aGUgU29mdHdhcmUsIGFuZCB0byBwZXJtaXQgcGVyc29ucyB0byB3aG9tIHRoZSBTb2Z0d2FyZSBpcwpmdXJuaXNoZWQgdG8gZG8gc28sIHN1YmplY3QgdG8gdGhlIGZvbGxvd2luZyBjb25kaXRpb25zOgoKVGhlIGFib3ZlIGNvcHlyaWdodCBub3RpY2UgYW5kIHRoaXMgcGVybWlzc2lvbiBub3RpY2Ugc2hhbGwgYmUgaW5jbHVkZWQgaW4gYWxsCmNvcGllcyBvciBzdWJzdGFudGlhbCBwb3J0aW9ucyBvZiB0aGUgU29mdHdhcmUuCgpUSEUgU09GVFdBUkUgSVMgUFJPVklERUQgIkFTIElTIiwgV0lUSE9VVCBXQVJSQU5UWSBPRiBBTlkgS0lORCwgRVhQUkVTUyBPUgpJTVBMSUVELCBJTkNMVURJTkcgQlVUIE5PVCBMSU1JVEVEIFRPIFRIRSBXQVJSQU5USUVTIE9GIE1FUkNIQU5UQUJJTElUWSwKRklUTkVTUyBGT1IgQSBQQVJUSUNVTEFSIFBVUlBPU0UgQU5EIE5PTklORlJJTkdFTUVOVC4gSU4gTk8gRVZFTlQgU0hBTEwgVEhFCkFVVEhPUlMgT1IgQ09QWVJJR0hUIEhPTERFUlMgQkUgTElBQkxFIEZPUiBBTlkgQ0xBSU0sIERBTUFHRVMgT1IgT1RIRVIKTElBQklMSVRZLCBXSEVUSEVSIElOIEFOIEFDVElPTiBPRiBDT05UUkFDVCwgVE9SVCBPUiBPVEhFUldJU0UsIEFSSVNJTkcgRlJPTSwKT1VUIE9GIE9SIElOIENPTk5FQ1RJT04gV0lUSCBUSEUgU09GVFdBUkUgT1IgVEhFIFVTRSBPUiBPVEhFUiBERUFMSU5HUyBJTiBUSEUKU09GVFdBUkUuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|class-variance-authority@0.7.1">
      <author>Joe Bell</author>
      <name>class-variance-authority</name>
      <version>0.7.1</version>
      <description>Class Variance Authority 🧬</description>
      <licenses>
        <license acknowledgement="declared">
          <id>Apache-2.0</id>
        </license>
      </licenses>
      <purl>pkg:npm/class-variance-authority@0.7.1</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/joe-bell/cva.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/joe-bell/cva#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/joe-bell/cva/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/class-variance-authority/-/class-variance-authority-0.7.1.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">29afbd4ebbadbfb1bc33a593e927a2456cfbf762b9a84a881841b35ca84013ac4e58063aa4f1fc53ef48637a0232fea4a9398bb2fed787fdb0d918a091e3ccb2</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/class-variance-authority</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgQXBhY2hlIExpY2Vuc2UKICAgICAgICAgICAgICAgICAgICAgICAgICAgVmVyc2lvbiAyLjAsIEphbnVhcnkgMjAwNAogICAgICAgICAgICAgICAgICAgICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvCgogICBURVJNUyBBTkQgQ09ORElUSU9OUyBGT1IgVVNFLCBSRVBST0RVQ1RJT04sIEFORCBESVNUUklCVVRJT04KCiAgIDEuIERlZmluaXRpb25zLgoKICAgICAgIkxpY2Vuc2UiIHNoYWxsIG1lYW4gdGhlIHRlcm1zIGFuZCBjb25kaXRpb25zIGZvciB1c2UsIHJlcHJvZHVjdGlvbiwKICAgICAgYW5kIGRpc3RyaWJ1dGlvbiBhcyBkZWZpbmVkIGJ5IFNlY3Rpb25zIDEgdGhyb3VnaCA5IG9mIHRoaXMgZG9jdW1lbnQuCgogICAgICAiTGljZW5zb3IiIHNoYWxsIG1lYW4gdGhlIGNvcHlyaWdodCBvd25lciBvciBlbnRpdHkgYXV0aG9yaXplZCBieQogICAgICB0aGUgY29weXJpZ2h0IG93bmVyIHRoYXQgaXMgZ3JhbnRpbmcgdGhlIExpY2Vuc2UuCgogICAgICAiTGVnYWwgRW50aXR5IiBzaGFsbCBtZWFuIHRoZSB1bmlvbiBvZiB0aGUgYWN0aW5nIGVudGl0eSBhbmQgYWxsCiAgICAgIG90aGVyIGVudGl0aWVzIHRoYXQgY29udHJvbCwgYXJlIGNvbnRyb2xsZWQgYnksIG9yIGFyZSB1bmRlciBjb21tb24KICAgICAgY29udHJvbCB3aXRoIHRoYXQgZW50aXR5LiBGb3IgdGhlIHB1cnBvc2VzIG9mIHRoaXMgZGVmaW5pdGlvbiwKICAgICAgImNvbnRyb2wiIG1lYW5zIChpKSB0aGUgcG93ZXIsIGRpcmVjdCBvciBpbmRpcmVjdCwgdG8gY2F1c2UgdGhlCiAgICAgIGRpcmVjdGlvbiBvciBtYW5hZ2VtZW50IG9mIHN1Y2ggZW50aXR5LCB3aGV0aGVyIGJ5IGNvbnRyYWN0IG9yCiAgICAgIG90aGVyd2lzZSwgb3IgKGlpKSBvd25lcnNoaXAgb2YgZmlmdHkgcGVyY2VudCAoNTAlKSBvciBtb3JlIG9mIHRoZQogICAgICBvdXRzdGFuZGluZyBzaGFyZXMsIG9yIChpaWkpIGJlbmVmaWNpYWwgb3duZXJzaGlwIG9mIHN1Y2ggZW50aXR5LgoKICAgICAgIllvdSIgKG9yICJZb3VyIikgc2hhbGwgbWVhbiBhbiBpbmRpdmlkdWFsIG9yIExlZ2FsIEVudGl0eQogICAgICBleGVyY2lzaW5nIHBlcm1pc3Npb25zIGdyYW50ZWQgYnkgdGhpcyBMaWNlbnNlLgoKICAgICAgIlNvdXJjZSIgZm9ybSBzaGFsbCBtZWFuIHRoZSBwcmVmZXJyZWQgZm9ybSBmb3IgbWFraW5nIG1vZGlmaWNhdGlvbnMsCiAgICAgIGluY2x1ZGluZyBidXQgbm90IGxpbWl0ZWQgdG8gc29mdHdhcmUgc291cmNlIGNvZGUsIGRvY3VtZW50YXRpb24KICAgICAgc291cmNlLCBhbmQgY29uZmlndXJhdGlvbiBmaWxlcy4KCiAgICAgICJPYmplY3QiIGZvcm0gc2hhbGwgbWVhbiBhbnkgZm9ybSByZXN1bHRpbmcgZnJvbSBtZWNoYW5pY2FsCiAgICAgIHRyYW5zZm9ybWF0aW9uIG9yIHRyYW5zbGF0aW9uIG9mIGEgU291cmNlIGZvcm0sIGluY2x1ZGluZyBidXQKICAgICAgbm90IGxpbWl0ZWQgdG8gY29tcGlsZWQgb2JqZWN0IGNvZGUsIGdlbmVyYXRlZCBkb2N1bWVudGF0aW9uLAogICAgICBhbmQgY29udmVyc2lvbnMgdG8gb3RoZXIgbWVkaWEgdHlwZXMuCgogICAgICAiV29yayIgc2hhbGwgbWVhbiB0aGUgd29yayBvZiBhdXRob3JzaGlwLCB3aGV0aGVyIGluIFNvdXJjZSBvcgogICAgICBPYmplY3QgZm9ybSwgbWFkZSBhdmFpbGFibGUgdW5kZXIgdGhlIExpY2Vuc2UsIGFzIGluZGljYXRlZCBieSBhCiAgICAgIGNvcHlyaWdodCBub3RpY2UgdGhhdCBpcyBpbmNsdWRlZCBpbiBvciBhdHRhY2hlZCB0byB0aGUgd29yawogICAgICAoYW4gZXhhbXBsZSBpcyBwcm92aWRlZCBpbiB0aGUgQXBwZW5kaXggYmVsb3cpLgoKICAgICAgIkRlcml2YXRpdmUgV29ya3MiIHNoYWxsIG1lYW4gYW55IHdvcmssIHdoZXRoZXIgaW4gU291cmNlIG9yIE9iamVjdAogICAgICBmb3JtLCB0aGF0IGlzIGJhc2VkIG9uIChvciBkZXJpdmVkIGZyb20pIHRoZSBXb3JrIGFuZCBmb3Igd2hpY2ggdGhlCiAgICAgIGVkaXRvcmlhbCByZXZpc2lvbnMsIGFubm90YXRpb25zLCBlbGFib3JhdGlvbnMsIG9yIG90aGVyIG1vZGlmaWNhdGlvbnMKICAgICAgcmVwcmVzZW50LCBhcyBhIHdob2xlLCBhbiBvcmlnaW5hbCB3b3JrIG9mIGF1dGhvcnNoaXAuIEZvciB0aGUgcHVycG9zZXMKICAgICAgb2YgdGhpcyBMaWNlbnNlLCBEZXJpdmF0aXZlIFdvcmtzIHNoYWxsIG5vdCBpbmNsdWRlIHdvcmtzIHRoYXQgcmVtYWluCiAgICAgIHNlcGFyYWJsZSBmcm9tLCBvciBtZXJlbHkgbGluayAob3IgYmluZCBieSBuYW1lKSB0byB0aGUgaW50ZXJmYWNlcyBvZiwKICAgICAgdGhlIFdvcmsgYW5kIERlcml2YXRpdmUgV29ya3MgdGhlcmVvZi4KCiAgICAgICJDb250cmlidXRpb24iIHNoYWxsIG1lYW4gYW55IHdvcmsgb2YgYXV0aG9yc2hpcCwgaW5jbHVkaW5nCiAgICAgIHRoZSBvcmlnaW5hbCB2ZXJzaW9uIG9mIHRoZSBXb3JrIGFuZCBhbnkgbW9kaWZpY2F0aW9ucyBvciBhZGRpdGlvbnMKICAgICAgdG8gdGhhdCBXb3JrIG9yIERlcml2YXRpdmUgV29ya3MgdGhlcmVvZiwgdGhhdCBpcyBpbnRlbnRpb25hbGx5CiAgICAgIHN1Ym1pdHRlZCB0byBMaWNlbnNvciBmb3IgaW5jbHVzaW9uIGluIHRoZSBXb3JrIGJ5IHRoZSBjb3B5cmlnaHQgb3duZXIKICAgICAgb3IgYnkgYW4gaW5kaXZpZHVhbCBvciBMZWdhbCBFbnRpdHkgYXV0aG9yaXplZCB0byBzdWJtaXQgb24gYmVoYWxmIG9mCiAgICAgIHRoZSBjb3B5cmlnaHQgb3duZXIuIEZvciB0aGUgcHVycG9zZXMgb2YgdGhpcyBkZWZpbml0aW9uLCAic3VibWl0dGVkIgogICAgICBtZWFucyBhbnkgZm9ybSBvZiBlbGVjdHJvbmljLCB2ZXJiYWwsIG9yIHdyaXR0ZW4gY29tbXVuaWNhdGlvbiBzZW50CiAgICAgIHRvIHRoZSBMaWNlbnNvciBvciBpdHMgcmVwcmVzZW50YXRpdmVzLCBpbmNsdWRpbmcgYnV0IG5vdCBsaW1pdGVkIHRvCiAgICAgIGNvbW11bmljYXRpb24gb24gZWxlY3Ryb25pYyBtYWlsaW5nIGxpc3RzLCBzb3VyY2UgY29kZSBjb250cm9sIHN5c3RlbXMsCiAgICAgIGFuZCBpc3N1ZSB0cmFja2luZyBzeXN0ZW1zIHRoYXQgYXJlIG1hbmFnZWQgYnksIG9yIG9uIGJlaGFsZiBvZiwgdGhlCiAgICAgIExpY2Vuc29yIGZvciB0aGUgcHVycG9zZSBvZiBkaXNjdXNzaW5nIGFuZCBpbXByb3ZpbmcgdGhlIFdvcmssIGJ1dAogICAgICBleGNsdWRpbmcgY29tbXVuaWNhdGlvbiB0aGF0IGlzIGNvbnNwaWN1b3VzbHkgbWFya2VkIG9yIG90aGVyd2lzZQogICAgICBkZXNpZ25hdGVkIGluIHdyaXRpbmcgYnkgdGhlIGNvcHlyaWdodCBvd25lciBhcyAiTm90IGEgQ29udHJpYnV0aW9uLiIKCiAgICAgICJDb250cmlidXRvciIgc2hhbGwgbWVhbiBMaWNlbnNvciBhbmQgYW55IGluZGl2aWR1YWwgb3IgTGVnYWwgRW50aXR5CiAgICAgIG9uIGJlaGFsZiBvZiB3aG9tIGEgQ29udHJpYnV0aW9uIGhhcyBiZWVuIHJlY2VpdmVkIGJ5IExpY2Vuc29yIGFuZAogICAgICBzdWJzZXF1ZW50bHkgaW5jb3Jwb3JhdGVkIHdpdGhpbiB0aGUgV29yay4KCiAgIDIuIEdyYW50IG9mIENvcHlyaWdodCBMaWNlbnNlLiBTdWJqZWN0IHRvIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZgogICAgICB0aGlzIExpY2Vuc2UsIGVhY2ggQ29udHJpYnV0b3IgaGVyZWJ5IGdyYW50cyB0byBZb3UgYSBwZXJwZXR1YWwsCiAgICAgIHdvcmxkd2lkZSwgbm9uLWV4Y2x1c2l2ZSwgbm8tY2hhcmdlLCByb3lhbHR5LWZyZWUsIGlycmV2b2NhYmxlCiAgICAgIGNvcHlyaWdodCBsaWNlbnNlIHRvIHJlcHJvZHVjZSwgcHJlcGFyZSBEZXJpdmF0aXZlIFdvcmtzIG9mLAogICAgICBwdWJsaWNseSBkaXNwbGF5LCBwdWJsaWNseSBwZXJmb3JtLCBzdWJsaWNlbnNlLCBhbmQgZGlzdHJpYnV0ZSB0aGUKICAgICAgV29yayBhbmQgc3VjaCBEZXJpdmF0aXZlIFdvcmtzIGluIFNvdXJjZSBvciBPYmplY3QgZm9ybS4KCiAgIDMuIEdyYW50IG9mIFBhdGVudCBMaWNlbnNlLiBTdWJqZWN0IHRvIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZgogICAgICB0aGlzIExpY2Vuc2UsIGVhY2ggQ29udHJpYnV0b3IgaGVyZWJ5IGdyYW50cyB0byBZb3UgYSBwZXJwZXR1YWwsCiAgICAgIHdvcmxkd2lkZSwgbm9uLWV4Y2x1c2l2ZSwgbm8tY2hhcmdlLCByb3lhbHR5LWZyZWUsIGlycmV2b2NhYmxlCiAgICAgIChleGNlcHQgYXMgc3RhdGVkIGluIHRoaXMgc2VjdGlvbikgcGF0ZW50IGxpY2Vuc2UgdG8gbWFrZSwgaGF2ZSBtYWRlLAogICAgICB1c2UsIG9mZmVyIHRvIHNlbGwsIHNlbGwsIGltcG9ydCwgYW5kIG90aGVyd2lzZSB0cmFuc2ZlciB0aGUgV29yaywKICAgICAgd2hlcmUgc3VjaCBsaWNlbnNlIGFwcGxpZXMgb25seSB0byB0aG9zZSBwYXRlbnQgY2xhaW1zIGxpY2Vuc2FibGUKICAgICAgYnkgc3VjaCBDb250cmlidXRvciB0aGF0IGFyZSBuZWNlc3NhcmlseSBpbmZyaW5nZWQgYnkgdGhlaXIKICAgICAgQ29udHJpYnV0aW9uKHMpIGFsb25lIG9yIGJ5IGNvbWJpbmF0aW9uIG9mIHRoZWlyIENvbnRyaWJ1dGlvbihzKQogICAgICB3aXRoIHRoZSBXb3JrIHRvIHdoaWNoIHN1Y2ggQ29udHJpYnV0aW9uKHMpIHdhcyBzdWJtaXR0ZWQuIElmIFlvdQogICAgICBpbnN0aXR1dGUgcGF0ZW50IGxpdGlnYXRpb24gYWdhaW5zdCBhbnkgZW50aXR5IChpbmNsdWRpbmcgYQogICAgICBjcm9zcy1jbGFpbSBvciBjb3VudGVyY2xhaW0gaW4gYSBsYXdzdWl0KSBhbGxlZ2luZyB0aGF0IHRoZSBXb3JrCiAgICAgIG9yIGEgQ29udHJpYnV0aW9uIGluY29ycG9yYXRlZCB3aXRoaW4gdGhlIFdvcmsgY29uc3RpdHV0ZXMgZGlyZWN0CiAgICAgIG9yIGNvbnRyaWJ1dG9yeSBwYXRlbnQgaW5mcmluZ2VtZW50LCB0aGVuIGFueSBwYXRlbnQgbGljZW5zZXMKICAgICAgZ3JhbnRlZCB0byBZb3UgdW5kZXIgdGhpcyBMaWNlbnNlIGZvciB0aGF0IFdvcmsgc2hhbGwgdGVybWluYXRlCiAgICAgIGFzIG9mIHRoZSBkYXRlIHN1Y2ggbGl0aWdhdGlvbiBpcyBmaWxlZC4KCiAgIDQuIFJlZGlzdHJpYnV0aW9uLiBZb3UgbWF5IHJlcHJvZHVjZSBhbmQgZGlzdHJpYnV0ZSBjb3BpZXMgb2YgdGhlCiAgICAgIFdvcmsgb3IgRGVyaXZhdGl2ZSBXb3JrcyB0aGVyZW9mIGluIGFueSBtZWRpdW0sIHdpdGggb3Igd2l0aG91dAogICAgICBtb2RpZmljYXRpb25zLCBhbmQgaW4gU291cmNlIG9yIE9iamVjdCBmb3JtLCBwcm92aWRlZCB0aGF0IFlvdQogICAgICBtZWV0IHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKCiAgICAgIChhKSBZb3UgbXVzdCBnaXZlIGFueSBvdGhlciByZWNpcGllbnRzIG9mIHRoZSBXb3JrIG9yCiAgICAgICAgICBEZXJpdmF0aXZlIFdvcmtzIGEgY29weSBvZiB0aGlzIExpY2Vuc2U7IGFuZAoKICAgICAgKGIpIFlvdSBtdXN0IGNhdXNlIGFueSBtb2RpZmllZCBmaWxlcyB0byBjYXJyeSBwcm9taW5lbnQgbm90aWNlcwogICAgICAgICAgc3RhdGluZyB0aGF0IFlvdSBjaGFuZ2VkIHRoZSBmaWxlczsgYW5kCgogICAgICAoYykgWW91IG11c3QgcmV0YWluLCBpbiB0aGUgU291cmNlIGZvcm0gb2YgYW55IERlcml2YXRpdmUgV29ya3MKICAgICAgICAgIHRoYXQgWW91IGRpc3RyaWJ1dGUsIGFsbCBjb3B5cmlnaHQsIHBhdGVudCwgdHJhZGVtYXJrLCBhbmQKICAgICAgICAgIGF0dHJpYnV0aW9uIG5vdGljZXMgZnJvbSB0aGUgU291cmNlIGZvcm0gb2YgdGhlIFdvcmssCiAgICAgICAgICBleGNsdWRpbmcgdGhvc2Ugbm90aWNlcyB0aGF0IGRvIG5vdCBwZXJ0YWluIHRvIGFueSBwYXJ0IG9mCiAgICAgICAgICB0aGUgRGVyaXZhdGl2ZSBXb3JrczsgYW5kCgogICAgICAoZCkgSWYgdGhlIFdvcmsgaW5jbHVkZXMgYSAiTk9USUNFIiB0ZXh0IGZpbGUgYXMgcGFydCBvZiBpdHMKICAgICAgICAgIGRpc3RyaWJ1dGlvbiwgdGhlbiBhbnkgRGVyaXZhdGl2ZSBXb3JrcyB0aGF0IFlvdSBkaXN0cmlidXRlIG11c3QKICAgICAgICAgIGluY2x1ZGUgYSByZWFkYWJsZSBjb3B5IG9mIHRoZSBhdHRyaWJ1dGlvbiBub3RpY2VzIGNvbnRhaW5lZAogICAgICAgICAgd2l0aGluIHN1Y2ggTk9USUNFIGZpbGUsIGV4Y2x1ZGluZyB0aG9zZSBub3RpY2VzIHRoYXQgZG8gbm90CiAgICAgICAgICBwZXJ0YWluIHRvIGFueSBwYXJ0IG9mIHRoZSBEZXJpdmF0aXZlIFdvcmtzLCBpbiBhdCBsZWFzdCBvbmUKICAgICAgICAgIG9mIHRoZSBmb2xsb3dpbmcgcGxhY2VzOiB3aXRoaW4gYSBOT1RJQ0UgdGV4dCBmaWxlIGRpc3RyaWJ1dGVkCiAgICAgICAgICBhcyBwYXJ0IG9mIHRoZSBEZXJpdmF0aXZlIFdvcmtzOyB3aXRoaW4gdGhlIFNvdXJjZSBmb3JtIG9yCiAgICAgICAgICBkb2N1bWVudGF0aW9uLCBpZiBwcm92aWRlZCBhbG9uZyB3aXRoIHRoZSBEZXJpdmF0aXZlIFdvcmtzOyBvciwKICAgICAgICAgIHdpdGhpbiBhIGRpc3BsYXkgZ2VuZXJhdGVkIGJ5IHRoZSBEZXJpdmF0aXZlIFdvcmtzLCBpZiBhbmQKICAgICAgICAgIHdoZXJldmVyIHN1Y2ggdGhpcmQtcGFydHkgbm90aWNlcyBub3JtYWxseSBhcHBlYXIuIFRoZSBjb250ZW50cwogICAgICAgICAgb2YgdGhlIE5PVElDRSBmaWxlIGFyZSBmb3IgaW5mb3JtYXRpb25hbCBwdXJwb3NlcyBvbmx5IGFuZAogICAgICAgICAgZG8gbm90IG1vZGlmeSB0aGUgTGljZW5zZS4gWW91IG1heSBhZGQgWW91ciBvd24gYXR0cmlidXRpb24KICAgICAgICAgIG5vdGljZXMgd2l0aGluIERlcml2YXRpdmUgV29ya3MgdGhhdCBZb3UgZGlzdHJpYnV0ZSwgYWxvbmdzaWRlCiAgICAgICAgICBvciBhcyBhbiBhZGRlbmR1bSB0byB0aGUgTk9USUNFIHRleHQgZnJvbSB0aGUgV29yaywgcHJvdmlkZWQKICAgICAgICAgIHRoYXQgc3VjaCBhZGRpdGlvbmFsIGF0dHJpYnV0aW9uIG5vdGljZXMgY2Fubm90IGJlIGNvbnN0cnVlZAogICAgICAgICAgYXMgbW9kaWZ5aW5nIHRoZSBMaWNlbnNlLgoKICAgICAgWW91IG1heSBhZGQgWW91ciBvd24gY29weXJpZ2h0IHN0YXRlbWVudCB0byBZb3VyIG1vZGlmaWNhdGlvbnMgYW5kCiAgICAgIG1heSBwcm92aWRlIGFkZGl0aW9uYWwgb3IgZGlmZmVyZW50IGxpY2Vuc2UgdGVybXMgYW5kIGNvbmRpdGlvbnMKICAgICAgZm9yIHVzZSwgcmVwcm9kdWN0aW9uLCBvciBkaXN0cmlidXRpb24gb2YgWW91ciBtb2RpZmljYXRpb25zLCBvcgogICAgICBmb3IgYW55IHN1Y2ggRGVyaXZhdGl2ZSBXb3JrcyBhcyBhIHdob2xlLCBwcm92aWRlZCBZb3VyIHVzZSwKICAgICAgcmVwcm9kdWN0aW9uLCBhbmQgZGlzdHJpYnV0aW9uIG9mIHRoZSBXb3JrIG90aGVyd2lzZSBjb21wbGllcyB3aXRoCiAgICAgIHRoZSBjb25kaXRpb25zIHN0YXRlZCBpbiB0aGlzIExpY2Vuc2UuCgogICA1LiBTdWJtaXNzaW9uIG9mIENvbnRyaWJ1dGlvbnMuIFVubGVzcyBZb3UgZXhwbGljaXRseSBzdGF0ZSBvdGhlcndpc2UsCiAgICAgIGFueSBDb250cmlidXRpb24gaW50ZW50aW9uYWxseSBzdWJtaXR0ZWQgZm9yIGluY2x1c2lvbiBpbiB0aGUgV29yawogICAgICBieSBZb3UgdG8gdGhlIExpY2Vuc29yIHNoYWxsIGJlIHVuZGVyIHRoZSB0ZXJtcyBhbmQgY29uZGl0aW9ucyBvZgogICAgICB0aGlzIExpY2Vuc2UsIHdpdGhvdXQgYW55IGFkZGl0aW9uYWwgdGVybXMgb3IgY29uZGl0aW9ucy4KICAgICAgTm90d2l0aHN0YW5kaW5nIHRoZSBhYm92ZSwgbm90aGluZyBoZXJlaW4gc2hhbGwgc3VwZXJzZWRlIG9yIG1vZGlmeQogICAgICB0aGUgdGVybXMgb2YgYW55IHNlcGFyYXRlIGxpY2Vuc2UgYWdyZWVtZW50IHlvdSBtYXkgaGF2ZSBleGVjdXRlZAogICAgICB3aXRoIExpY2Vuc29yIHJlZ2FyZGluZyBzdWNoIENvbnRyaWJ1dGlvbnMuCgogICA2LiBUcmFkZW1hcmtzLiBUaGlzIExpY2Vuc2UgZG9lcyBub3QgZ3JhbnQgcGVybWlzc2lvbiB0byB1c2UgdGhlIHRyYWRlCiAgICAgIG5hbWVzLCB0cmFkZW1hcmtzLCBzZXJ2aWNlIG1hcmtzLCBvciBwcm9kdWN0IG5hbWVzIG9mIHRoZSBMaWNlbnNvciwKICAgICAgZXhjZXB0IGFzIHJlcXVpcmVkIGZvciByZWFzb25hYmxlIGFuZCBjdXN0b21hcnkgdXNlIGluIGRlc2NyaWJpbmcgdGhlCiAgICAgIG9yaWdpbiBvZiB0aGUgV29yayBhbmQgcmVwcm9kdWNpbmcgdGhlIGNvbnRlbnQgb2YgdGhlIE5PVElDRSBmaWxlLgoKICAgNy4gRGlzY2xhaW1lciBvZiBXYXJyYW50eS4gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yCiAgICAgIGFncmVlZCB0byBpbiB3cml0aW5nLCBMaWNlbnNvciBwcm92aWRlcyB0aGUgV29yayAoYW5kIGVhY2gKICAgICAgQ29udHJpYnV0b3IgcHJvdmlkZXMgaXRzIENvbnRyaWJ1dGlvbnMpIG9uIGFuICJBUyBJUyIgQkFTSVMsCiAgICAgIFdJVEhPVVQgV0FSUkFOVElFUyBPUiBDT05ESVRJT05TIE9GIEFOWSBLSU5ELCBlaXRoZXIgZXhwcmVzcyBvcgogICAgICBpbXBsaWVkLCBpbmNsdWRpbmcsIHdpdGhvdXQgbGltaXRhdGlvbiwgYW55IHdhcnJhbnRpZXMgb3IgY29uZGl0aW9ucwogICAgICBvZiBUSVRMRSwgTk9OLUlORlJJTkdFTUVOVCwgTUVSQ0hBTlRBQklMSVRZLCBvciBGSVRORVNTIEZPUiBBCiAgICAgIFBBUlRJQ1VMQVIgUFVSUE9TRS4gWW91IGFyZSBzb2xlbHkgcmVzcG9uc2libGUgZm9yIGRldGVybWluaW5nIHRoZQogICAgICBhcHByb3ByaWF0ZW5lc3Mgb2YgdXNpbmcgb3IgcmVkaXN0cmlidXRpbmcgdGhlIFdvcmsgYW5kIGFzc3VtZSBhbnkKICAgICAgcmlza3MgYXNzb2NpYXRlZCB3aXRoIFlvdXIgZXhlcmNpc2Ugb2YgcGVybWlzc2lvbnMgdW5kZXIgdGhpcyBMaWNlbnNlLgoKICAgOC4gTGltaXRhdGlvbiBvZiBMaWFiaWxpdHkuIEluIG5vIGV2ZW50IGFuZCB1bmRlciBubyBsZWdhbCB0aGVvcnksCiAgICAgIHdoZXRoZXIgaW4gdG9ydCAoaW5jbHVkaW5nIG5lZ2xpZ2VuY2UpLCBjb250cmFjdCwgb3Igb3RoZXJ3aXNlLAogICAgICB1bmxlc3MgcmVxdWlyZWQgYnkgYXBwbGljYWJsZSBsYXcgKHN1Y2ggYXMgZGVsaWJlcmF0ZSBhbmQgZ3Jvc3NseQogICAgICBuZWdsaWdlbnQgYWN0cykgb3IgYWdyZWVkIHRvIGluIHdyaXRpbmcsIHNoYWxsIGFueSBDb250cmlidXRvciBiZQogICAgICBsaWFibGUgdG8gWW91IGZvciBkYW1hZ2VzLCBpbmNsdWRpbmcgYW55IGRpcmVjdCwgaW5kaXJlY3QsIHNwZWNpYWwsCiAgICAgIGluY2lkZW50YWwsIG9yIGNvbnNlcXVlbnRpYWwgZGFtYWdlcyBvZiBhbnkgY2hhcmFjdGVyIGFyaXNpbmcgYXMgYQogICAgICByZXN1bHQgb2YgdGhpcyBMaWNlbnNlIG9yIG91dCBvZiB0aGUgdXNlIG9yIGluYWJpbGl0eSB0byB1c2UgdGhlCiAgICAgIFdvcmsgKGluY2x1ZGluZyBidXQgbm90IGxpbWl0ZWQgdG8gZGFtYWdlcyBmb3IgbG9zcyBvZiBnb29kd2lsbCwKICAgICAgd29yayBzdG9wcGFnZSwgY29tcHV0ZXIgZmFpbHVyZSBvciBtYWxmdW5jdGlvbiwgb3IgYW55IGFuZCBhbGwKICAgICAgb3RoZXIgY29tbWVyY2lhbCBkYW1hZ2VzIG9yIGxvc3NlcyksIGV2ZW4gaWYgc3VjaCBDb250cmlidXRvcgogICAgICBoYXMgYmVlbiBhZHZpc2VkIG9mIHRoZSBwb3NzaWJpbGl0eSBvZiBzdWNoIGRhbWFnZXMuCgogICA5LiBBY2NlcHRpbmcgV2FycmFudHkgb3IgQWRkaXRpb25hbCBMaWFiaWxpdHkuIFdoaWxlIHJlZGlzdHJpYnV0aW5nCiAgICAgIHRoZSBXb3JrIG9yIERlcml2YXRpdmUgV29ya3MgdGhlcmVvZiwgWW91IG1heSBjaG9vc2UgdG8gb2ZmZXIsCiAgICAgIGFuZCBjaGFyZ2UgYSBmZWUgZm9yLCBhY2NlcHRhbmNlIG9mIHN1cHBvcnQsIHdhcnJhbnR5LCBpbmRlbW5pdHksCiAgICAgIG9yIG90aGVyIGxpYWJpbGl0eSBvYmxpZ2F0aW9ucyBhbmQvb3IgcmlnaHRzIGNvbnNpc3RlbnQgd2l0aCB0aGlzCiAgICAgIExpY2Vuc2UuIEhvd2V2ZXIsIGluIGFjY2VwdGluZyBzdWNoIG9ibGlnYXRpb25zLCBZb3UgbWF5IGFjdCBvbmx5CiAgICAgIG9uIFlvdXIgb3duIGJlaGFsZiBhbmQgb24gWW91ciBzb2xlIHJlc3BvbnNpYmlsaXR5LCBub3Qgb24gYmVoYWxmCiAgICAgIG9mIGFueSBvdGhlciBDb250cmlidXRvciwgYW5kIG9ubHkgaWYgWW91IGFncmVlIHRvIGluZGVtbmlmeSwKICAgICAgZGVmZW5kLCBhbmQgaG9sZCBlYWNoIENvbnRyaWJ1dG9yIGhhcm1sZXNzIGZvciBhbnkgbGlhYmlsaXR5CiAgICAgIGluY3VycmVkIGJ5LCBvciBjbGFpbXMgYXNzZXJ0ZWQgYWdhaW5zdCwgc3VjaCBDb250cmlidXRvciBieSByZWFzb24KICAgICAgb2YgeW91ciBhY2NlcHRpbmcgYW55IHN1Y2ggd2FycmFudHkgb3IgYWRkaXRpb25hbCBsaWFiaWxpdHkuCgogICBFTkQgT0YgVEVSTVMgQU5EIENPTkRJVElPTlMKCiAgIENvcHlyaWdodCAyMDIyIEpvZSBCZWxsCgogICBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKICAgeW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgogICBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKCiAgICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKCiAgIFVubGVzcyByZXF1aXJlZCBieSBhcHBsaWNhYmxlIGxhdyBvciBhZ3JlZWQgdG8gaW4gd3JpdGluZywgc29mdHdhcmUKICAgZGlzdHJpYnV0ZWQgdW5kZXIgdGhlIExpY2Vuc2UgaXMgZGlzdHJpYnV0ZWQgb24gYW4gIkFTIElTIiBCQVNJUywKICAgV0lUSE9VVCBXQVJSQU5USUVTIE9SIENPTkRJVElPTlMgT0YgQU5ZIEtJTkQsIGVpdGhlciBleHByZXNzIG9yIGltcGxpZWQuCiAgIFNlZSB0aGUgTGljZW5zZSBmb3IgdGhlIHNwZWNpZmljIGxhbmd1YWdlIGdvdmVybmluZyBwZXJtaXNzaW9ucyBhbmQKICAgbGltaXRhdGlvbnMgdW5kZXIgdGhlIExpY2Vuc2UuCg==</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|tailwind-merge@2.6.0">
      <author>Dany Castillo</author>
      <name>tailwind-merge</name>
      <version>2.6.0</version>
      <description>Merge Tailwind CSS classes without style conflicts</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/tailwind-merge@2.6.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/dcastil/tailwind-merge.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/dcastil/tailwind-merge</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/dcastil/tailwind-merge/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/tailwind-merge/-/tailwind-merge-2.6.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">3fe56ed6a5dfcde7628ab987382df1286018799b4f715f60efa5fec60d850f8b58811ef57b0300df9637b02cf7ce188dfddc1e7d1a495f4c81720c22d5f5cd40</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/tailwind-merge</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE.md</name>
            <text content-type="text/markdown" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMSBEYW55IENhc3RpbGxvCgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tanstack/history@1.132.31">
      <author>Tanner Linsley</author>
      <group>@tanstack</group>
      <name>history</name>
      <version>1.132.31</version>
      <description>Modern and scalable routing for React applications</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40tanstack/history@1.132.31#packages/history</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/TanStack/router.git#packages/history</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://tanstack.com/router</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/TanStack/router/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tanstack/history/-/history-1.132.31.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">5021ccdae4b4b7fb92b33a8f128f920524a8415790f8b94e580541979480efe01e75e01b29a7c83e3167f21b9909734b0186f458a576fb0113afb9432bdbb3ee</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tanstack/history</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMS1wcmVzZW50IFRhbm5lciBMaW5zbGV5CgpQZXJtaXNzaW9uIGlzIGhlcmVieSBncmFudGVkLCBmcmVlIG9mIGNoYXJnZSwgdG8gYW55IHBlcnNvbiBvYnRhaW5pbmcgYSBjb3B5Cm9mIHRoaXMgc29mdHdhcmUgYW5kIGFzc29jaWF0ZWQgZG9jdW1lbnRhdGlvbiBmaWxlcyAodGhlICJTb2Z0d2FyZSIpLCB0byBkZWFsCmluIHRoZSBTb2Z0d2FyZSB3aXRob3V0IHJlc3RyaWN0aW9uLCBpbmNsdWRpbmcgd2l0aG91dCBsaW1pdGF0aW9uIHRoZSByaWdodHMKdG8gdXNlLCBjb3B5LCBtb2RpZnksIG1lcmdlLCBwdWJsaXNoLCBkaXN0cmlidXRlLCBzdWJsaWNlbnNlLCBhbmQvb3Igc2VsbApjb3BpZXMgb2YgdGhlIFNvZnR3YXJlLCBhbmQgdG8gcGVybWl0IHBlcnNvbnMgdG8gd2hvbSB0aGUgU29mdHdhcmUgaXMKZnVybmlzaGVkIHRvIGRvIHNvLCBzdWJqZWN0IHRvIHRoZSBmb2xsb3dpbmcgY29uZGl0aW9uczoKClRoZSBhYm92ZSBjb3B5cmlnaHQgbm90aWNlIGFuZCB0aGlzIHBlcm1pc3Npb24gbm90aWNlIHNoYWxsIGJlIGluY2x1ZGVkIGluIGFsbApjb3BpZXMgb3Igc3Vic3RhbnRpYWwgcG9ydGlvbnMgb2YgdGhlIFNvZnR3YXJlLgoKVEhFIFNPRlRXQVJFIElTIFBST1ZJREVEICJBUyBJUyIsIFdJVEhPVVQgV0FSUkFOVFkgT0YgQU5ZIEtJTkQsIEVYUFJFU1MgT1IKSU1QTElFRCwgSU5DTFVESU5HIEJVVCBOT1QgTElNSVRFRCBUTyBUSEUgV0FSUkFOVElFUyBPRiBNRVJDSEFOVEFCSUxJVFksCkZJVE5FU1MgRk9SIEEgUEFSVElDVUxBUiBQVVJQT1NFIEFORCBOT05JTkZSSU5HRU1FTlQuIElOIE5PIEVWRU5UIFNIQUxMIFRIRQpBVVRIT1JTIE9SIENPUFlSSUdIVCBIT0xERVJTIEJFIExJQUJMRSBGT1IgQU5ZIENMQUlNLCBEQU1BR0VTIE9SIE9USEVSCkxJQUJJTElUWSwgV0hFVEhFUiBJTiBBTiBBQ1RJT04gT0YgQ09OVFJBQ1QsIFRPUlQgT1IgT1RIRVJXSVNFLCBBUklTSU5HIEZST00sCk9VVCBPRiBPUiBJTiBDT05ORUNUSU9OIFdJVEggVEhFIFNPRlRXQVJFIE9SIFRIRSBVU0UgT1IgT1RIRVIgREVBTElOR1MgSU4gVEhFClNPRlRXQVJFLgo=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tanstack/react-store@0.7.7">
      <author>Tanner Linsley</author>
      <group>@tanstack</group>
      <name>react-store</name>
      <version>0.7.7</version>
      <description>Framework agnostic type-safe store w/ reactive framework adapters</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40tanstack/react-store@0.7.7#packages/react-store</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/TanStack/store.git#packages/react-store</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://tanstack.com/store</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/TanStack/store/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tanstack/react-store/-/react-store-0.7.7.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">aaa4f4b9f7a01510c64a87fd0ff56a699823360a78b513c764826adbe4081e4314b478da274958aeb5e3788509be39d36e03df483d5780e304b7496600d9fa66</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tanstack/react-store</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMSBUYW5uZXIgTGluc2xleQoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|isbot@5.1.31">
      <name>isbot</name>
      <version>5.1.31</version>
      <description>🤖/👨‍🦰 Recognise bots/crawlers/spiders using the user agent string.</description>
      <licenses>
        <license acknowledgement="declared">
          <id>Unlicense</id>
        </license>
      </licenses>
      <purl>pkg:npm/isbot@5.1.31</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/omrilotan/isbot.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://isbot.js.org</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/omrilotan/isbot/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/isbot/-/isbot-5.1.31.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">0cf810b217a112b1c0a9208a0dbdeb356d37a5adb04bfbf97afbd4aadc6de934e71d1a801bc15dcdc49226cf7ae7aa4ae98f8d4fb2bd47869c1185cb1d87e951</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/isbot</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">IyBVbmxpY2Vuc2UKClRoaXMgaXMgZnJlZSBhbmQgdW5lbmN1bWJlcmVkIHNvZnR3YXJlIHJlbGVhc2VkIGludG8gdGhlIHB1YmxpYyBkb21haW4uCgpBbnlvbmUgaXMgZnJlZSB0byBjb3B5LCBtb2RpZnksIHB1Ymxpc2gsIHVzZSwgY29tcGlsZSwgc2VsbCwgb3IKZGlzdHJpYnV0ZSB0aGlzIHNvZnR3YXJlLCBlaXRoZXIgaW4gc291cmNlIGNvZGUgZm9ybSBvciBhcyBhIGNvbXBpbGVkCmJpbmFyeSwgZm9yIGFueSBwdXJwb3NlLCBjb21tZXJjaWFsIG9yIG5vbi1jb21tZXJjaWFsLCBhbmQgYnkgYW55Cm1lYW5zLgoKSW4ganVyaXNkaWN0aW9ucyB0aGF0IHJlY29nbml6ZSBjb3B5cmlnaHQgbGF3cywgdGhlIGF1dGhvciBvciBhdXRob3JzCm9mIHRoaXMgc29mdHdhcmUgZGVkaWNhdGUgYW55IGFuZCBhbGwgY29weXJpZ2h0IGludGVyZXN0IGluIHRoZQpzb2Z0d2FyZSB0byB0aGUgcHVibGljIGRvbWFpbi4gV2UgbWFrZSB0aGlzIGRlZGljYXRpb24gZm9yIHRoZSBiZW5lZml0Cm9mIHRoZSBwdWJsaWMgYXQgbGFyZ2UgYW5kIHRvIHRoZSBkZXRyaW1lbnQgb2Ygb3VyIGhlaXJzIGFuZApzdWNjZXNzb3JzLiBXZSBpbnRlbmQgdGhpcyBkZWRpY2F0aW9uIHRvIGJlIGFuIG92ZXJ0IGFjdCBvZgpyZWxpbnF1aXNobWVudCBpbiBwZXJwZXR1aXR5IG9mIGFsbCBwcmVzZW50IGFuZCBmdXR1cmUgcmlnaHRzIHRvIHRoaXMKc29mdHdhcmUgdW5kZXIgY29weXJpZ2h0IGxhdy4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELApFWFBSRVNTIE9SIElNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YKTUVSQ0hBTlRBQklMSVRZLCBGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULgpJTiBOTyBFVkVOVCBTSEFMTCBUSEUgQVVUSE9SUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUgpPVEhFUiBMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwKQVJJU0lORyBGUk9NLCBPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SCk9USEVSIERFQUxJTkdTIElOIFRIRSBTT0ZUV0FSRS4KCkZvciBtb3JlIGluZm9ybWF0aW9uLCBwbGVhc2UgcmVmZXIgdG8gPGh0dHA6Ly91bmxpY2Vuc2Uub3JnLz4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|tiny-warning@1.0.3">
      <author>Alex Reardon</author>
      <name>tiny-warning</name>
      <version>1.0.3</version>
      <description>A tiny warning function</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/tiny-warning@1.0.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/alexreardon/tiny-warning.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/alexreardon/tiny-warning#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/alexreardon/tiny-warning/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/tiny-warning/-/tiny-warning-1.0.3.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">94137dccb37fa007faf28df335762b742b7590ff16b22196f0ea3691ae356f620ce492ff4b5093c97d6b5b499bff34ae26e9f4654ac3c71e2caaf612d855b33c</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/tiny-warning</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAxOSBBbGV4YW5kZXIgUmVhcmRvbgoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4=</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|@tanstack/store@0.7.7">
      <author>Tanner Linsley</author>
      <group>@tanstack</group>
      <name>store</name>
      <version>0.7.7</version>
      <description>Framework agnostic type-safe store w/ reactive framework adapters</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/%40tanstack/store@0.7.7#packages/store</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/TanStack/store.git#packages/store</url>
          <comment>as detected from PackageJson property "repository.url" and "repository.directory"</comment>
        </reference>
        <reference type="website">
          <url>https://tanstack.com/store</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/TanStack/store/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/@tanstack/store/-/store-0.7.7.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">c5aea94da9f56dc6aa6034bd043a52892eb7a9ae84a0390f37d46c45ac47b837550cd9edceadf137047960a4d4fd5dd2912c82f53e1854e3e1db34503749e121</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/@tanstack/store</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvcHlyaWdodCAoYykgMjAyMSBUYW5uZXIgTGluc2xleQoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|cookie-es@2.0.0">
      <name>cookie-es</name>
      <version>2.0.0</version>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/cookie-es@2.0.0</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/unjs/cookie-es.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/unjs/cookie-es#readme</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/unjs/cookie-es/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/cookie-es/-/cookie-es-2.0.0.tgz</url>
          <comment>as detected from npm-ls property "resolved" and property "integrity"</comment>
          <hashes>
            <hash alg="SHA-512">4408f8138db5518460aa890a526a2da80c2ea65630d79aad7577d8fa11b380227f3018c2559712a072bf907f64a1c7e3463703304ec8883591ff5597d533363e</hash>
          </hashes>
        </reference>
      </externalReferences>
      <properties>
        <property name="cdx:npm:package:path">node_modules/cookie-es</property>
      </properties>
      <evidence>
        <licenses>
          <license>
            <name>file: LICENSE</name>
            <text content-type="text/plain" encoding="base64">TUlUIExpY2Vuc2UKCkNvb2tpZS1lcyBjb3B5cmlnaHQgKGMpIFBvb3lhIFBhcnNhIDxwb295YUBwaTAuaW8+CgpDb29raWUgcGFyc2luZyBiYXNlZCBvbiBodHRwczovL2dpdGh1Yi5jb20vanNodHRwL2Nvb2tpZQpDb3B5cmlnaHQgKGMpIDIwMTItMjAxNCBSb21hbiBTaHR5bG1hbiA8c2h0eWxtYW5AZ21haWwuY29tPgpDb3B5cmlnaHQgKGMpIDIwMTUgRG91Z2xhcyBDaHJpc3RvcGhlciBXaWxzb24gPGRvdWdAc29tZXRoaW5nZG91Zy5jb20+CgpTZXQtQ29va2llIHBhcnNpbmcgYmFzZWQgb24gaHR0cHM6Ly9naXRodWIuY29tL25mcmllZGx5L3NldC1jb29raWUtcGFyc2VyCkNvcHlyaWdodCAoYykgMjAxNSBOYXRoYW4gRnJpZWRseSA8bmF0aGFuQG5mcmllZGx5LmNvbT4gKGh0dHA6Ly9uZnJpZWRseS5jb20vKQoKUGVybWlzc2lvbiBpcyBoZXJlYnkgZ3JhbnRlZCwgZnJlZSBvZiBjaGFyZ2UsIHRvIGFueSBwZXJzb24gb2J0YWluaW5nIGEgY29weQpvZiB0aGlzIHNvZnR3YXJlIGFuZCBhc3NvY2lhdGVkIGRvY3VtZW50YXRpb24gZmlsZXMgKHRoZSAiU29mdHdhcmUiKSwgdG8gZGVhbAppbiB0aGUgU29mdHdhcmUgd2l0aG91dCByZXN0cmljdGlvbiwgaW5jbHVkaW5nIHdpdGhvdXQgbGltaXRhdGlvbiB0aGUgcmlnaHRzCnRvIHVzZSwgY29weSwgbW9kaWZ5LCBtZXJnZSwgcHVibGlzaCwgZGlzdHJpYnV0ZSwgc3VibGljZW5zZSwgYW5kL29yIHNlbGwKY29waWVzIG9mIHRoZSBTb2Z0d2FyZSwgYW5kIHRvIHBlcm1pdCBwZXJzb25zIHRvIHdob20gdGhlIFNvZnR3YXJlIGlzCmZ1cm5pc2hlZCB0byBkbyBzbywgc3ViamVjdCB0byB0aGUgZm9sbG93aW5nIGNvbmRpdGlvbnM6CgpUaGUgYWJvdmUgY29weXJpZ2h0IG5vdGljZSBhbmQgdGhpcyBwZXJtaXNzaW9uIG5vdGljZSBzaGFsbCBiZSBpbmNsdWRlZCBpbiBhbGwKY29waWVzIG9yIHN1YnN0YW50aWFsIHBvcnRpb25zIG9mIHRoZSBTb2Z0d2FyZS4KClRIRSBTT0ZUV0FSRSBJUyBQUk9WSURFRCAiQVMgSVMiLCBXSVRIT1VUIFdBUlJBTlRZIE9GIEFOWSBLSU5ELCBFWFBSRVNTIE9SCklNUExJRUQsIElOQ0xVRElORyBCVVQgTk9UIExJTUlURUQgVE8gVEhFIFdBUlJBTlRJRVMgT0YgTUVSQ0hBTlRBQklMSVRZLApGSVRORVNTIEZPUiBBIFBBUlRJQ1VMQVIgUFVSUE9TRSBBTkQgTk9OSU5GUklOR0VNRU5ULiBJTiBOTyBFVkVOVCBTSEFMTCBUSEUKQVVUSE9SUyBPUiBDT1BZUklHSFQgSE9MREVSUyBCRSBMSUFCTEUgRk9SIEFOWSBDTEFJTSwgREFNQUdFUyBPUiBPVEhFUgpMSUFCSUxJVFksIFdIRVRIRVIgSU4gQU4gQUNUSU9OIE9GIENPTlRSQUNULCBUT1JUIE9SIE9USEVSV0lTRSwgQVJJU0lORyBGUk9NLApPVVQgT0YgT1IgSU4gQ09OTkVDVElPTiBXSVRIIFRIRSBTT0ZUV0FSRSBPUiBUSEUgVVNFIE9SIE9USEVSIERFQUxJTkdTIElOIFRIRQpTT0ZUV0FSRS4K</text>
          </license>
        </licenses>
      </evidence>
    </component>
    <component type="library" bom-ref="openbb-platform@1.0.0|seroval-plugins@1.3.3">
      <author>Alexis Munsayac</author>
      <name>seroval-plugins</name>
      <version>1.3.3</version>
      <description>Stringify JS values</description>
      <licenses>
        <license acknowledgement="declared">
          <id>MIT</id>
        </license>
      </licenses>
      <purl>pkg:npm/seroval-plugins@1.3.3</purl>
      <externalReferences>
        <reference type="vcs">
          <url>git+https://github.com/lxsmnsyc/seroval.git</url>
          <comment>as detected from PackageJson property "repository.url"</comment>
        </reference>
        <reference type="website">
          <url>https://github.com/lxsmnsyc/seroval/tree/main/packages/plugins</url>
          <comment>as detected from PackageJson property "homepage"</comment>
        </reference>
        <reference type="issue-tracker">
          <url>https://github.com/lxsmnsyc/seroval/issues</url>
          <comment>as detected from PackageJson property "bugs.url"</comment>
        </reference>
        <reference type="distribution">
          <url>https://registry.npmjs.org/seroval-plugins/-/seroval-plugins-1.3.3.tgz</url>
          <comment>as detected from npm-ls p
... [truncated]
```

## High-Level Overview

This is a .xml file containing 35787 lines of code.

## Detailed Structure

Standard text file.

## Key Components

No major components extracted.

## Usage & Examples

See source code for usage details.

## Related Files

- `CSS`

## Notes
- Generated: 2025-11-18T07:54:34.956007
- Generator: World's Best Repo Book Generator v1.0.0
