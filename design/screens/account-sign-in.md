# Account: Sign in

- **Status:** draft (example screen)
- **Task:** PHO-4
- **Kind:** low-fi wireframe

This is an example. It shows the pattern for screen files. It is not
a screen the team has agreed to build.

## Who and why

A returning user who already has an account. They want to get back
to their work quickly, with as few steps as possible.

## Wireframe

```
+--------------------------------------------------+
|  [Logo]                                          |
+--------------------------------------------------+
|                                                  |
|              Sign in to your account             |
|                                                  |
|   Email                                          |
|   +------------------------------------------+   |
|   | name@example.com                         |   |
|   +------------------------------------------+   |
|                                                  |
|   Password                       Forgot it?      |
|   +------------------------------------------+   |
|   | ••••••••                          [Show] |   |
|   +------------------------------------------+   |
|                                                  |
|   [x] Keep me signed in                          |
|                                                  |
|   +------------------------------------------+   |
|   |                 [Sign in]                |   |
|   +------------------------------------------+   |
|                                                  |
|          New here?  Create an account            |
|                                                  |
+--------------------------------------------------+
```

## Parts

- **Email**: text field. Typed in lowercase; spaces are trimmed.
- **Password**: hidden by default. `[Show]` reveals it.
- **Forgot it?**: link to the reset password screen.
- **Keep me signed in**: on by default for personal devices.
- **[Sign in]**: the one main action. Pressing Enter does the same.
- **Create an account**: link to the sign-up screen.

## States

- **Empty**: `[Sign in]` stays active. Missing fields show a message
  when pressed, not before.
- **Loading**: the button reads "Signing in…" and can't be pressed twice.
- **Wrong details**: one message above the form: "Email or password
  is not right." Don't say which one.
- **Locked out**: after too many tries, explain how long to wait and
  point to "Forgot it?".

## Open questions

- Do we offer sign-in with Google or another provider?
- Should "Keep me signed in" be on or off by default?
- Where does the user land after signing in?
