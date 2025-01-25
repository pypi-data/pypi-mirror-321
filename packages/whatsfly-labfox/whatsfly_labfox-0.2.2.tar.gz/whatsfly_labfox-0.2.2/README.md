# WhatsFly
[![Build](https://github.com/Labfox/whatsfly/actions/workflows/build.yml/badge.svg)](https://github.com/Labfox/whatsfly/actions/workflows/build.yml)
## Just run and have fun. Just try and go fly. 

> [!NOTE]  
> There currently isn't active development, but the project is still maintained. If you want a feature, please create an issue, I'll try to implement it as soon as possible (I usually respond withing 1-2 weeks).


WhatsApp web wrapper in Python. No selenium nor gecko web driver needed. 

Setting up browser driver is tricky for python newcomers, and thus it makes your code so 'laggy' while using lots of ram.

## Documentation

https://whatsfly.labfox.fr

## Supported machines

The library theoretically support every machine with go and cgo, but if the builds fails on your machine, there are pre-built binaries auto-downloaded for the following architectures:

| Architecture   | Status            |
|----------------|-------------------|
| Linux amd64    | ✅                 |
| Linux ARM64    | GH Worlflow error |
| Linux 686      | GH Worlflow error |
| Linux 386      | GH Worlflow error |
| Windows amd64  | ✅                 |
| Windows 32 bit | GH Worlflow error |
| OSX arm64      | ✅                 |
| OSX amd64      | ✅                 |

## Contributing
> If you'd like to support my work, please consider making a pull request to help fix any issues with the code.
> I would like to extend my gratitude to the open-source developers behind tls-client, tiktoken, and whatsmeow. Their work has inspired me greatly and helped me to create this project.
