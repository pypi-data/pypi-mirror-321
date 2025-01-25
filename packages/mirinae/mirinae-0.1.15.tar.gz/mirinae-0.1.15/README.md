# Mirinae

![MAGO](https://img.shields.io/badge/MAGO-INC-red)
![audion](https://img.shields.io/badge/audion-service-blue)
![python](https://img.shields.io/badge/python-3.10-green)

마고 프레임워크를 사용할 수 있는 CLI 도구입니다.

## 마고 서비스

- [audion](https://audion.magovoice.com)
- 문의: contact@holamago.com

## 설치

- Python 3.9 이상이 필요합니다.

```bash
pip install mirinae
```

- mirinae는 /home/user/.mirinae 디렉토리에 설정 파일을 저장합니다.
- mirinae를 사용하기 위해서는 `PATH` 환경 변수에 /home/user/.local/bin 디렉토리를 추가해야 합니다.

```bash
echo 'export PATH=$PATH:/home/galois/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

zsh를 사용하는 경우에는 ~/.zshrc 파일을 수정해야 합니다.

```bash
echo 'export PATH=$PATH:/home/galois/.local/bin' >> ~/.zshrc
source ~/.zshrc
```

## 기본 동작 방법

### 사용자 등록

- 사용자가 mirinae-cli를 사용하여 마고 서비스를 사용하기 위해서는 사용자 등록이 필요합니다.
- 사용자 등록은 [audion home](https://audion.magovoice.com)에서 진행할 수 있습니다.

### 로그인

```bash
mirinae user login -v -e <email> -w <password>
```

- 로그인을 하면 access token과 refresh token이 발급됩니다.
- tokens은 /home/user/.mirinae 에서 관리됩니다.
- access token은 15분 동안 유효하며, refresh token은 access token을 갱신할 때 사용됩니다. refresh token은 7일 동안 유효합니다.
- access token이 만료되면 refresh token을 사용하여 access token을 갱신할 수 있습니다.

```bash
mirinae user refresh -v
```

## Flow

audion에서 제공하는 서비스는 flow를 사용하여 서비스를 제공합니다. flow는 사용자가 사용하고 싶은 서비스를 선태하고 curation을 통해 사용자 맞춤형 flow를 생성합니다. 그리고 한 줄의 명령어로 flow를 실행할 수 있습니다.

### Flow 생성

#### Product

- 마고에서는 사용자가 손쉽게 서비스를 사용할 수 있도록 기본적인 flow를 제공합니다.
- 기본적으로 제공되는 flow는 product 형태로 제공이 되고, 이미 마고에서 기본적으로 몇 개의 product를 제공하고 있습니다. 사용자가 새로운 product를 생성하여 마고에 등록 요청을 하면, 검토를 거쳐 마고에서 product를 등록해 드립니다.
- 현재 지원하고 있는 프로덕트는 다음과 같습니다.

| 프로덕트 | 프로젝트 ID |
| --- | --- |
| Subtitle Generation | audion_sg |
| Voice Separation | audion_vs |
| Music Source Separation | audion_mss |

#### Project

- flow를 실행하기 위해서는 project가 필요합니다.
- project는 product를 사용하여 생성할 수 있습니다.

```bash
mirinae project create -v -id <product_id>
```

- 생성된 project는 project 목록조회를 통해 확인할 수 있습니다.

```bash
mirinae project get -v
```

- 또한, project ID와 이름을 사용해서 project를 확인할 수 있습니다.

```bash
mirinae project get -v -id <project_id>
mirinae project get -v --name "audion_sg"
```

### Flow 실행

이제 당신은 flow를 실행할 준비가 되었습니다. flow를 실행하기 위해서는 project ID를 알아야 합니다. project ID는 project를 생성할 때 확인할 수 있고, 또는 project 목록을 확인하여 project ID를 확인할 수 있습니다.

#### 미디어 파일로 프로젝트 사용하기

다음 3가지 방법으로 미디어 파일을 프로젝트에 사용할 수 있습니다.

| 입력 타입 | 설명 |
| url | URL을 사용하여 미디어 파일을 사용합니다. |
| file | 로컬에 있는 미디어 파일을 사용합니다. |
| uri | 마고 서버에 있는 미디어 파일을 사용합니다. |

- **uri**: 사용자 flow를 실행 후 받은 결과 데이터에 있는 파일 경로를 uri로 사용할 수 있습니다. 결과물을 다운로드 받아서 사용할 수도 있지만, uri를 사용하면 마고 서버에 있는 파일을 그대로 사용할 수 있습니다.

#### URL을 사용하기

```bash
mirinae flow run -v --id <project_id> --it url -i <url>
```

#### 로컬 파일을 사용하기

```bash
mirinae flow run -v --id <project_id> --it file -i <file_path>
```

#### 마고 서비스에 있는 파일을 사용하기

```bash
mirinae flow run -v --id <project_id> --it uri -i <uri>
```
