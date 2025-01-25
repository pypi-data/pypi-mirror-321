# Mirinae

마고 프레임워크를 사용할 수 있는 CLI 도구입니다.

## 마고 서비스

- [Audion](https://audion.mago52.com)

## 설치

- Python 3.9 이상이 필요합니다.

```bash
pip install mirinae
```

## 기본 동작 방법

### 사용자 등록

사용자 등록은 `Audion` 홈페이지에서 진행할 수 있습니다.
또는 galois@holamago.com 으로 이메일을 보내주세요.

### Login

```bash
mirinae user login -v -e <email> -w <password>
```

### 프로젝트 생성하기

마고에서 프로덕트를 제공하고 있습니다. 프로젝트를 생성하고 사용하려면 프로젝트 ID가 필요합니다.

현재 지원하고 있는 프로덕트는 다음과 같습니다.

| 프로덕트 | 프로젝트 ID |
| --- | --- |
| Subtitle Generation | Audion_0001 |
| Voice Separation | Audion_0002 |
| Music Source Separation | Audion_0003 |

프로젝트는 프로덕트 ID를 사용하여 생성할 수 있습니다.

```bash
mirinae project create -v --prod-id <product_id>
```

생성된 프로젝트는 아래와 같이 확인할 수 있습니다.

```bash
mirinae project get -v
```

### 미디어 파일로 프로젝트 사용하기

다음 3가지 방법으로 미디어 파일을 프로젝트에 사용할 수 있습니다.

| 입력 타입 | 설명 |
| url | URL을 사용하여 미디어 파일을 사용합니다. |
| file | 로컬에 있는 미디어 파일을 사용합니다. |
| uri | 마고 서비스에 있는 미디어 파일을 사용합니다. |

#### URL을 사용하기

```bash
mirinae pipeline proj -v --proj-id <project_id> --it url -i <url>
```

#### 로컬 파일을 사용하기

```bash
mirinae pipeline proj -v --proj-id <project_id> --it file -i <file_path>
```

#### 마고 서비스에 있는 파일을 사용하기

```bash
mirinae pipeline proj -v --proj-id <project_id> --it uri -i <uri>
```
