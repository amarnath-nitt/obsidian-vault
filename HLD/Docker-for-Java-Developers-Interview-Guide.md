---
title: Docker for Java Developers — Interview Revision Guide
tags: [docker, java, spring-boot, interview-prep, devops]
source: https://www.youtube.com/watch?v=lpKwgOpxpqg
channel: Telusko
published: 2025-07-29
updated: 2026-08-13
type: revision-notes
---

> [!note] Current practice
> Use `docker compose` (not the legacy `docker-compose` command), multi-stage builds, non-root runtime users, pinned base-image digests in CI, and container-aware JVM memory settings. Containers package an application; they do not replace health checks, observability, secrets management, or resource limits.

# 🐳 Docker for Java Developers — Interview Revision Guide

> [!info] About this note Based on the chapter structure of the Telusko YouTube course **"Docker for Java Developers"**. Content compiled independently from standard Docker/Spring Boot practice, organized around the video's topic outline. No transcript was available — notes are written from established Docker/Java knowledge matching each chapter.

## 📑 Table of Contents

- [[#1 Docker Introduction and The Problem It Solves]]
- [[#2 Virtualization vs Containerization]]
- [[#3 What is Docker]]
- [[#4 Docker Setup]]
- [[#5 Running Your First Container and Core Docker Commands]]
- [[#6 Docker Architecture]]
- [[#7 Running a JDK Container and Packaging a Spring Boot App]]
- [[#8 Dockerfile and Building Custom Images]]
- [[#9 Web App with PostgreSQL]]
- [[#10 Docker Compose]]
- [[#11 Running Multiple Containers]]
- [[#12 Docker Volumes]]
- [[#⚡ Rapid-Fire Revision]]

---

## 1. Docker Introduction and The Problem It Solves

### 📝 Revision Notes

- "Works on my machine" problem: app behaves differently across dev, test, and production due to differing OS versions, JDK versions, library versions, or missing environment variables.
- Manually replicating environments (installing exact JDK, DB, OS patches on every machine) is slow, error-prone, and doesn't scale across teams.
- Docker solves this by packaging the application with its entire runtime environment (code, JDK, libraries, config) into one portable unit called an **image**.
- Goal: **build once, run anywhere** — identical behavior on a developer laptop, CI server, and production host.

### 💬 Interview Q&A

> [!question] What real-world problem does Docker primarily solve? It eliminates the "it works on my machine" problem by packaging an application with its exact dependencies (OS libraries, JDK version, config) so it behaves identically across dev, test, and production environments.

> [!question] Why can't teams just document setup steps instead of using Docker? Manual setup instructions drift out of date, are error-prone to follow by hand, don't guarantee identical versions of every dependency, and don't scale when you have many services or many environments.

---

## 2. Virtualization vs Containerization

### 📝 Revision Notes

- **Virtual Machines (VMs)** run a full Guest OS on top of a **Hypervisor**, which sits on the Host OS/hardware — each VM duplicates an entire operating system.
- Hypervisor types: **Type 1** (bare-metal, e.g., VMware ESXi, Hyper-V) runs directly on hardware; **Type 2** (hosted, e.g., VirtualBox, VMware Workstation) runs on top of a host OS.
- VMs give strong isolation but are heavyweight: slow to boot (minutes), large disk footprint (GBs per VM), and duplicate OS-level resources.
- **Containers** share the host machine's OS kernel and only isolate the application layer (process, filesystem, network) using OS features like **namespaces** and **cgroups** (on Linux).
- Containers are lightweight: start in seconds, use MBs instead of GBs, and many containers can run efficiently on one host.
- Trade-off: containers have slightly weaker isolation than VMs (shared kernel) but are far more efficient for running many app instances/microservices.

### 💬 Interview Q&A

> [!question] What is the fundamental architectural difference between a VM and a container? A VM virtualizes hardware and runs a complete guest OS via a hypervisor, so each VM has its own kernel. A container virtualizes at the OS level — all containers on a host share the same host kernel, isolated from each other using namespaces and control groups, so they don't need a separate guest OS.

> [!question] Why do containers start in seconds while VMs take minutes? A VM boot has to start an entire guest operating system from scratch. A container just starts a process using an already-running host kernel — closer to launching a regular process than booting a machine.

> [!question] Is Docker less secure than a VM because of the shared kernel? It can offer weaker isolation than a VM in theory, since a kernel-level vulnerability could affect multiple containers — but in practice Docker uses namespaces, cgroups, and can be hardened further with tools like seccomp, AppArmor, or lightweight VM-based runtimes (gVisor, Kata Containers).

---

## 3. What is Docker

### 📝 Revision Notes

- Docker is an open-source **containerization platform** that lets you build, ship, and run applications inside lightweight, portable containers.
- Core building blocks: **Dockerfile** (instructions to build an image) → **Docker Image** (read-only template/snapshot) → **Docker Container** (a running instance of an image).
- **Docker Hub** is the default public registry for storing and distributing images (like GitHub, but for images).
- Key benefits: portability, consistency across environments, isolation between apps, faster startup than VMs, and easy horizontal scaling of microservices.

### 💬 Interview Q&A

> [!question] What is the difference between a Docker image and a Docker container? An image is a read-only, immutable template containing the application, its dependencies, and instructions on how to run it. A container is a running (or stopped) instance created from that image — many containers can be created from the same single image.

> [!question] What is Docker Hub? A cloud-based public registry where Docker images are stored and shared. You can `docker pull` official or community images from it, or `docker push` your own images to it.

---

## 4. Docker Setup

### 📝 Revision Notes

- **Docker Desktop** is the standard way to install Docker on Windows and Mac; on Linux, install the Docker Engine directly (e.g., via `apt` on Ubuntu).
- After installation, verify with `docker version` (client + server/daemon versions) and `docker info` (system-wide details).
- On Windows, Docker Desktop typically uses the **WSL2** backend for better performance than the older Hyper-V backend.

### 💬 Interview Q&A

> [!question] How do you verify Docker was installed correctly? Run `docker version` to confirm both the client and the daemon (server) respond, and optionally `docker run hello-world` to confirm you can pull and run a container end-to-end.

---

## 5. Running Your First Container and Core Docker Commands

### 📝 Revision Notes

- `docker run <image>` pulls the image (if not present locally) and starts a new container from it.
- `docker ps` shows running containers; `docker ps -a` shows all containers including stopped ones.
- Common lifecycle commands: create, start, stop, pause/unpause, restart, and rm (remove) a container.
- Detached vs. foreground: `-d` runs a container in the background; without it, the container runs attached to your terminal.
- Useful flags: `-p host:container` maps ports, `-e` sets environment variables, `--name` names the container, `-v` mounts a volume.

### 🖥️ Command Cheat Sheet

|Command|Purpose|
|---|---|
|`docker search <name>`|Search Docker Hub for an image|
|`docker pull <image>`|Download an image without running it|
|`docker images`|List locally downloaded images|
|`docker run <image>`|Create + start a container from an image|
|`docker run -d -p 8080:8080 <image>`|Run detached, mapping host:container ports|
|`docker ps` / `docker ps -a`|List running / all containers|
|`docker stop <id>`|Gracefully stop a running container|
|`docker start <id>`|Start an existing stopped container|
|`docker exec -it <id> bash`|Open an interactive shell inside a running container|
|`docker logs <id>`|View container logs|
|`docker rm <id>` / `docker rmi <image>`|Remove a container / remove an image|
|`docker build -t <name> .`|Build an image from a Dockerfile in the current directory|

### 💬 Interview Q&A

> [!question] What's the difference between `docker stop` and `docker kill`? `docker stop` sends SIGTERM and waits (default ~10s) for graceful shutdown before forcing a SIGKILL. `docker kill` sends SIGKILL immediately, terminating the container without letting it clean up.

> [!question] What's the difference between `docker run` and `docker start`? `docker run` creates a brand-new container from an image and starts it. `docker start` restarts an already-created (but stopped) container, reusing its existing filesystem and configuration.

> [!question] How would you get a shell inside a running container to debug it? `docker exec -it <container_id_or_name> bash` (or `sh` if bash isn't available) opens an interactive terminal session inside the already-running container.

---

## 6. Docker Architecture

### 📝 Revision Notes

- Docker uses a **client-server architecture**: the Docker Client (CLI) sends commands to the Docker Daemon (`dockerd`), which does the actual work.
- The daemon manages Docker objects: images, containers, networks, and volumes, and communicates with registries (like Docker Hub) to pull/push images.
- Client and daemon can run on the same host or communicate remotely via REST API / Unix socket.
- Under the hood on Linux, Docker relies on kernel features: **namespaces** (process/network/filesystem isolation) and **cgroups** (resource limits like CPU/memory).

### 💬 Interview Q&A

> [!question] Explain Docker's client-server architecture. The Docker CLI (client) is what the user interacts with; it sends REST API requests to the Docker daemon (`dockerd`), which runs in the background and does the actual building, running, and management of images and containers. They can run on the same machine or the client can connect to a remote daemon.

> [!question] What Linux kernel features make containerization possible? Namespaces provide isolation (each container gets its own view of processes, network interfaces, mounts, hostname, users), and control groups (cgroups) limit and account for resource usage like CPU, memory, and I/O per container.

---

## 7. Running a JDK Container and Packaging a Spring Boot App

### 📝 Revision Notes

- You can run a JDK container directly (e.g., `docker run -it eclipse-temurin:17 bash`) to get an isolated Java environment without installing Java locally.
- To containerize a Spring Boot app: first package it as an executable JAR (`mvn clean package` or `./mvnw package`), producing a fat JAR with an embedded server (Tomcat by default).
- That JAR is then `COPY`ed into a Docker image built `FROM` a JDK/JRE base image, and run with `ENTRYPOINT ["java","-jar","app.jar"]`.
- Prefer a **JRE** (or slim JDK) base image for the final runtime layer to keep the image smaller, since you only need to run the JAR, not compile it.

### 💬 Interview Q&A

> [!question] Why use a JRE base image instead of a full JDK for the final container? The JRE contains everything needed to run a compiled Java app, while the JDK also bundles compilers and development tools that are unnecessary at runtime. Using JRE (or a slim JDK) reduces image size and shrinks the attack surface.

> [!question] What does `mvn clean package` produce, and why does it matter for Docker? It compiles the code and packages it into an executable (fat) JAR containing the app plus an embedded servlet container like Tomcat. That single JAR is what gets copied into the Docker image, so the container doesn't need a separately installed application server.

---

## 8. Dockerfile and Building Custom Images

### 📝 Revision Notes

- A **Dockerfile** is a text file of instructions Docker reads top-to-bottom to build an image.
- Key instructions: `FROM` (base image), `WORKDIR` (working directory inside image), `COPY`/`ADD` (copy files in), `RUN` (execute a command at build time), `EXPOSE` (document a port), `ENV` (set environment variable), `ENTRYPOINT`/`CMD` (define the container's default startup command).
- Each instruction creates a new cached **layer**; Docker reuses unchanged layers on rebuild — copy dependency files (like `pom.xml`) and resolve dependencies _before_ copying the rest of the source code to maximize cache hits.
- `docker build -t myapp:1.0 .` builds an image from the Dockerfile in the current directory (`.` = build context).
- `CMD` provides default arguments that can be overridden at `docker run` time; `ENTRYPOINT` defines the fixed executable that always runs (`CMD` can supply its default args).

### 📄 Sample Dockerfile for a Spring Boot App

```dockerfile
FROM eclipse-temurin:17-jre
WORKDIR /app
COPY target/myapp.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### 💬 Interview Q&A

> [!question] What is the difference between ENTRYPOINT and CMD? ENTRYPOINT sets the fixed command that always runs when the container starts. CMD sets default arguments/command that can be overridden by anything passed after the image name in `docker run`. They're often combined: ENTRYPOINT defines the executable, CMD supplies default arguments.

> [!question] Why does instruction order in a Dockerfile matter? Docker caches each layer; if a layer's instruction or its inputs haven't changed, Docker reuses the cached layer instead of rebuilding it. Placing rarely-changing steps (like installing dependencies) before frequently-changing steps (like copying source code) means code changes don't invalidate the dependency-install layer, speeding up rebuilds.

> [!question] What's the difference between COPY and ADD? COPY simply copies files/directories from the build context into the image. ADD does that too, but also supports extracting local tar archives automatically and fetching remote URLs. Best practice is to prefer COPY unless you specifically need ADD's extra behavior.

> [!question] What is a multi-stage build and why use it for Java apps? A multi-stage Dockerfile uses multiple `FROM` statements — one stage (with a full JDK + Maven/Gradle) builds/compiles the app, and a later, smaller stage (JRE only) copies just the final JAR from the build stage. This keeps the final production image small since build tools aren't shipped in it.

---

## 9. Web App with PostgreSQL

### 📝 Revision Notes

- A Spring Boot app and its database are typically run as **separate containers**, not bundled into one image — this follows the single-responsibility/one-process-per-container principle.
- Containers on the same Docker network can reach each other **by container name** (Docker's embedded DNS), e.g., a Spring app's `application.properties` can point its datasource URL to `jdbc:postgresql://postgres-container:5432/mydb`.
- Official Postgres image supports environment variables like `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB` to initialize the database on first run.
- Without a custom network, standalone containers can't resolve each other by name — use `docker network create` or rely on Docker Compose, which creates a network automatically.

### 💬 Interview Q&A

> [!question] How does a Spring Boot container talk to a Postgres container by name? If both containers are attached to the same user-defined Docker network, Docker's built-in DNS resolves the Postgres container's name to its internal IP, so the Spring app's JDBC URL can simply use the container name as the host instead of an IP address.

> [!question] Why shouldn't you run the app and the database in the same container? Docker's best practice is one primary process per container. Separating them lets you scale, update, restart, and manage each independently, reuse the same database image across projects, and keeps images smaller and easier to reason about.

---

## 10. Docker Compose

### 📝 Revision Notes

- Docker Compose lets you define and run **multi-container applications** using a single declarative YAML file (`docker-compose.yml`).
- Each service (e.g., `app`, `db`) is defined with its image (or build context), ports, environment variables, volumes, and dependencies.
- `depends_on` controls startup order between services — note: it does **not** wait for the dependency to be fully "ready", only "started".
- Compose automatically creates a shared network so services can reach each other by their service name.
- Key commands: `docker compose up` (start all services, add `-d` for detached), `docker compose down` (stop and remove containers/network), `docker compose logs`, `docker compose ps`.

### 📄 Sample docker-compose.yml

```yaml
version: "3.8"
services:
  app:
    build: .
    ports:
      - "8080:8080"
    depends_on:
      - db
    environment:
      - SPRING_DATASOURCE_URL=jdbc:postgresql://db:5432/mydb
  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=admin
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:
```

### 💬 Interview Q&A

> [!question] Why use Docker Compose instead of multiple `docker run` commands? Compose lets you declare the entire multi-container setup (services, ports, env vars, volumes, networks) in one version-controlled YAML file, and bring the whole stack up or down with a single command instead of manually running and networking each container.

> [!question] Does `depends_on` guarantee the database is ready before the app starts? No — by default `depends_on` only waits for the dependency container to _start_, not for the application inside it (e.g., Postgres) to be _ready_ to accept connections. For true readiness checks, add a healthcheck and `depends_on: condition: service_healthy`, or handle retries in the app itself.

---

## 11. Running Multiple Containers

### 📝 Revision Notes

- Multiple containers can be started individually with `docker run`, or together via Compose — Compose is preferred for anything beyond a couple of related services.
- Docker networks (`bridge`, `host`, `none`, or custom user-defined bridge) control how containers communicate with each other and the outside world.
- A **custom user-defined bridge network** is recommended over the default bridge because it provides automatic DNS resolution by container/service name.

### 💬 Interview Q&A

> [!question] What are the main Docker network drivers and when would you use each? **Bridge** (default, isolated network on the host — good for standalone multi-container apps on one host), **host** (container shares the host's network stack directly — no port mapping needed, less isolation), **none** (no networking), and **overlay** (used in Docker Swarm/multi-host setups for cross-host container communication).

---

## 12. Docker Volumes

### 📝 Revision Notes

- Containers are **ephemeral** by design — any data written inside a container's writable layer is lost when the container is removed.
- **Volumes** provide persistent storage that lives outside the container's lifecycle, managed by Docker (stored under Docker's own storage area, e.g., `/var/lib/docker/volumes` on Linux).
- **Bind mounts** map a specific host directory/file directly into the container — useful for local development (e.g., live-reloading source code) but tie you to the host's filesystem layout.
- **Named volumes** (`docker volume create`, or declared in Compose) are the recommended way to persist data like database files, since Docker manages their location and lifecycle.
- Commands: `docker volume ls`, `docker volume create <name>`, `docker volume inspect <name>`, `docker volume rm <name>`; mount with `-v myvolume:/path/in/container` or the newer `--mount` syntax.

### 💬 Interview Q&A

> [!question] Why would a Postgres container need a volume? Without a volume, all database files live in the container's writable layer, so removing or recreating the container wipes the entire database. Mounting a named volume at Postgres's data directory (`/var/lib/postgresql/data`) ensures the data persists independently of the container's lifecycle.

> [!question] What's the difference between a named volume and a bind mount? A named volume is fully managed by Docker (Docker chooses and controls the storage location) and is the recommended approach for persistent app/database data. A bind mount links a specific path on the host filesystem into the container, giving direct access/control but making the container dependent on that host path — commonly used for mounting local source code during development.

> [!question] If you run `docker rm` on a container, does its named volume get deleted too? No. Named volumes are decoupled from the container lifecycle by design and persist after the container is removed, unless explicitly removed with `docker volume rm`, or `docker rm -v` is used to also delete anonymous volumes attached to that container.

---

## ⚡ Rapid-Fire Revision

> [!success] Image vs Container? Image = blueprint (read-only). Container = running instance of that blueprint.

> [!success] Dockerfile vs docker-compose.yml? Dockerfile builds one image. docker-compose.yml orchestrates multiple containers/services together.

> [!success] CMD vs ENTRYPOINT? CMD = default, overridable args. ENTRYPOINT = fixed executable.

> [!success] Bridge network purpose? Default isolated network for containers on a single host to communicate.

> [!success] Why are containers faster than VMs? They share the host kernel — no separate OS boot required.

> [!success] How to persist DB data? Use a Docker named volume mounted to the DB's data directory.

> [!success] How to check container logs? `docker logs <container_id>`

> [!success] How to reduce final Java image size? Use a JRE (not JDK) base image, and/or a multi-stage Dockerfile.

---

## 🔗 Related

- #docker #java #spring-boot #interview-prep #devops
