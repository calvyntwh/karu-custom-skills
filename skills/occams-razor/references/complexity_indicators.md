# complexity_indicators.md - The Smell of Bloat

Use this list to spot "Complexity Creep". If you see these, apply the Razor immediately.

## 1. Dependency Obesity
*   **The "One Function" Import:** Importing a 5MB library just to check `isEmpty` or `leftPad`. -> *Fix:* Write the 1-line helper function yourself.
*   **The "Wrapper" Wrapper:** A library that wraps another library that wraps a native API. -> *Fix:* Use the native API directly.

## 2. Abstraction Theater
*   **Passthrough Layers:** `Controller` calls `Service` calls `Repository` calls `Dao` calls `Database`. If `Service` just returns `Repository.get()`, it is useless. -> *Fix:* Collapse layers.
*   **Interface Explosion:** `IUser`, `IUserImpl`, `AbstractUser`, `BaseUser`. Do you actually have 2 implementations? -> *Fix:* Delete the Interface until you actually need a second implementation (YAGNI).
*   **DTO Mirroring:** Creating a separate `UserDTO` that is identical to `UserEntity`. -> *Fix:* Use one model until they *must* diverge.

## 3. Configuration Hell
*   **XML/JSON Overload:** 500 lines of config to start a "Hello World" server.
*   **Environment Paranoia:** `ENV.VAR_FOR_EVERY_STRING`. Is `APP_NAME` really going to change at runtime? -> *Fix:* Hardcode constants that are constant.

## 4. Premature Optimization
*   **Caching First:** Adding Redis/Memcached before you even know if the DB is slow. -> *Fix:* Code it simply. Profile it. Cache only if slow.
*   **Microservices First:** Splitting a startup into 10 services before you have 10 users. -> *Fix:* Build a Monolith. Split it when it hurts.
