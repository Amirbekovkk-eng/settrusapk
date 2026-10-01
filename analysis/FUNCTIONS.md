# Functions inferred from static evidence

- Main UI: `MainActivity`, launcher activity.
- Settings: `SettingsActivity`, with ADB label/control and links to Android, engineering and keyboard settings.
- Application management: `AppsActivity` lists packages, computes sizes, detects protected apps, and exposes install/uninstall/enable/disable-style actions.
- Boot/background: `BootReceiver` plus foreground `WarnFixService`; manifest describes background time sync and keyboard guard on a vehicle head unit.
- Time: `TimeSync`, NTP strings including `ru.pool.ntp.org`, timezone and system time APIs.
- Input/keyboard: `KeyboardGuard`, keyboard settings and input-related privileged permissions.
- Display/overlay/system: package name and permissions indicate overlay/system configuration functions.
- scrcpy: embedded server JAR, bridge/start/restart strings, port 8099 and ADB forwarding text.
- Localization: Russian UI label `Q07 Русификатор`, RuStore/forum/QR assets.

These are static findings; runtime behavior and success conditions were not tested on a head unit.
