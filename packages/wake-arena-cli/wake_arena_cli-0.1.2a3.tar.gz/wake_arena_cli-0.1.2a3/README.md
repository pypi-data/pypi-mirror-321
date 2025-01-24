# Wake Arena CLI
Wake Arena command line interface to operate projects and vulnerability checks based on [Wake](https://github.com/Ackee-Blockchain/wake) testing tool.


## Quick start 🚀
1. Initialize the CLI
```shell
wake-arena init
```
2. Perform security audit using remote Wake execution
```shell
wake-arena check
```

## Env parameters 🚩
| Env                   | Description                                                      |
|-----------------------|------------------------------------------------------------------|
| `WAKE_ARENA_API_KEY`  | Uses api key instead of configured authentication                |
| `WAKE_ARENA_PROJECT`  | Project id. CLI will use this project instead of configured one  |
| `WAKE_ARENA_API_URL`  | Development only, replaces Wake Arena API endpoint for cli       |
| `WAKE_ARENA_WEB_URL`  | Development only, replaces Wake Arena WEB url for cli            |