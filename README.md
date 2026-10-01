# settrusapk — Q07 Русификатор forensic analysis

This repository contains a read-only forensic analysis of the APK supplied by the operator. The APK itself is **not** committed. Only its source path, size and SHA-256 are recorded.

## Result

The APK is a privileged/system Android application (`ru.q07.overlays`, `android.uid.system`) and contains an in-app ADB control path based on privileged property access. Evidence includes DEX symbols/strings `setAdb`, `setProp`, `setprop`, `usb.role.state`, and `SystemProperties.set(`. The manifest grants `WRITE_SECURE_SETTINGS` and declares only boot/package/user-present broadcasts. No USB/removable-storage receiver, `ACTION_USB_*` or `ACTION_MEDIA_*` trigger, `settings put`, or USB-file trigger was found in the supplied APK evidence.

Therefore the requested “enable ADB when a USB flash drive is inserted” mechanism is **not present as an automatic flash-drive detector**. The likely supported path is a UI button calling privileged property-setting code; exact runtime property values require decompilation or device execution, neither of which is asserted by this static evidence.

See `ANALYSIS/ADB_USB.md` for the evidence chain and limitations.
