# Ollama and Open-WebUI Docker Setup

This guide provides detailed instructions on how to set up and run the Ollama and Open-WebUI services using Docker Compose. Additionally, it explains how to download models inside the Ollama container.

## Prerequisites

- Docker installed on your machine
- Docker Compose installed on your machine

## Docker Compose File

The `dockercompose.yml` file defines two services: `ollama` and `open-webui`. The `ollama` service uses the `ollama/ollama` image, and the `open-webui` service uses the `ghcr.io/open-webui/open-webui:ollama` image. Both services share a volume named `ollama`.

## Instructions

1. **Clone the repository** (if you haven't already):

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Navigate to the directory containing the `dockercompose.yml` file**:

    ```sh
    cd ollama
    ```

3. **Start the services using Docker Compose**:

    ```sh
    docker-compose up -d
    ```

    This command will start the [ollama](http://_vscodecontentref_/0) and `open-webui` services in detached mode.

4. **Verify that the services are running**:

    ```sh
    docker-compose ps
    ```

    You should see both [ollama](http://_vscodecontentref_/1) and `open-webui` services listed as running.

5. **Download models inside the Ollama container**:

    To download a model inside the [ollama](http://_vscodecontentref_/2) container, use the following command:

    ```sh
    docker exec -it ollama ollama run <model name:byte tag>
    ```

    Replace `<model name:byte tag>` with the actual model name and byte tag you want to download.

    ## Example

    Here is an example of how to download a model named `deepseek-r1` with a byte tag `1.5b`:

    ```sh
    docker exec -it ollama ollama run deepseek-r1:1.5b

## Reference

1. https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image
2. https://ollama.com/library?sort=popular&q=llama
3. https://docs.openwebui.com/getting-started/quick-start/