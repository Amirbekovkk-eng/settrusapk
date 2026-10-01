# DEX/native analysis

The APK has one `classes.dex` (76304 bytes) and no `.so` native libraries. `apkanalyzer dex packages` reports 314 classes / 663 methods / 39515 references, principally package `ru.q07.overlays`.

Important classes: `MainActivity`, `SettingsActivity`, `AppsActivity`, `BootReceiver`, `UsbMode`, `Sys`, `Scrcpy`, `TimeSync`, `KeyboardGuard`, `WarnFixService`, `Installer` and `Installers`.

The DEX string table contains privileged/system-property indicators and scrcpy integration. No native code is present. Raw strings are preserved in `analysis/artifacts/classes.dex.strings.txt`; this is evidence, not decompiled source. Exact control flow and property values remain unverified because no decompiler was available in the analysis environment.
