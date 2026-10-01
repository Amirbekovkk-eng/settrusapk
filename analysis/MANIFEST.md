# Manifest analysis

Decoded manifest: `analysis/artifacts/AndroidManifest.print.xml`.

Package `ru.q07.overlays`, version `1.24.1`, minSdk 28, targetSdk 34. Launcher: `.MainActivity`. Non-exported activities: `.AppsActivity`, `.SettingsActivity`. Service: `.WarnFixService`, foreground special-use. Exported receiver: `.BootReceiver` for boot, locked boot, package replacement and user-present events.

Notable permissions: INSTALL_PACKAGES, DELETE_PACKAGES, QUERY_ALL_PACKAGES, CHANGE_OVERLAY_PACKAGES, WRITE_SECURE_SETTINGS, WRITE_SETTINGS, SYSTEM_ALERT_WINDOW, ADD_TRUSTED_DISPLAY, MANAGE_ACTIVITY_TASKS, REAL_GET_TASKS, MONITOR_INPUT, INJECT_EVENTS, foreground service, RECEIVE_BOOT_COMPLETED, SET_TIME, SET_TIME_ZONE, INTERNET and package/app-op management permissions.
