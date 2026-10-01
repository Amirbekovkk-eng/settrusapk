# ADB / USB forensic finding

## Confirmed

1. `AndroidManifest.xml` sets `android:sharedUserId="android.uid.system"`.
2. It requests `android.permission.WRITE_SECURE_SETTINGS`, `WRITE_SETTINGS`, and other privileged capabilities.
3. DEX string evidence includes `adbBtn`, `adbLabel`, `adbOn`, `setAdb`, `setProp`, `setPropSh`, `setprop`, `setprop usb.role.state`, `usb.role.state`, and `SystemProperties.set(`.
4. `MainActivity`, `SettingsActivity`, `UsbMode`, and `BootReceiver` classes are present. `BootReceiver` is registered for BOOT_COMPLETED, LOCKED_BOOT_COMPLETED, MY_PACKAGE_REPLACED and USER_PRESENT.
5. Embedded scrcpy server and UI strings show an ADB/scrcpy feature, including `adb forward` and `scrcpy-server.jar`.

## Not found

Static manifest and string evidence contains no `ACTION_USB_DEVICE_ATTACHED`, `ACTION_USB_ACCESSORY_ATTACHED`, `ACTION_MEDIA_MOUNTED`, `ACTION_MEDIA_UNMOUNTED`, `UsbManager`, `StorageVolume`, `/storage/`, `/sdcard/`, removable-media path, or `settings put`. The manifest has no USB/removable-storage receiver. Thus no automatic “USB flash drive insertion → enable ADB” trigger is demonstrated.

## Exact conclusion

The APK contains a privileged ADB control path likely reachable from an on-screen button and implemented through Android system-property access, including the USB-role property name `usb.role.state`. The supplied static evidence does **not** establish the exact property value or prove that the code enables ADB over USB; it establishes only the property-setting symbols and related UI/classes. A USB flash drive is not used as a trigger in the manifest or visible string set.

Evidence: `analysis/artifacts/AndroidManifest.print.xml`, `classes.dex.strings.txt`, `inventory.json`.
