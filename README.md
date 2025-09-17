# FaithLog 📖✨

*A Bible Reading + Mini-Game Web Application*

[English](#english) | [中文](#中文)

---

## English

### 🎯 Project Overview

**FaithLog** is a modern web application that combines daily Bible reading with gamification elements to encourage consistent spiritual growth. Built with Django and following agile development principles, it starts with a minimal viable product (MVP) and iteratively adds features.

### ✨ Core Features

1. **📚 Reading Plan Management** - Set up Bible reading schedules and track daily progress
2. **🎮 Reward System** - Mini-games and badges after completing daily readings
3. **👥 Social Sharing** - Share progress and reflections with friends
4. **💬 Ask Pastor** - Private messaging system to connect with group leaders and pastors

### 🛠️ Technology Stack

- **Backend**: Django 5 + Django REST Framework + Django Channels
- **Frontend**: Django Templates + HTMX + Tailwind CSS
- **Database**: SQLite (MVP) → PostgreSQL (Production)
- **Deployment**: SSH + Gunicorn (MVP) → Docker Compose (Production)
- **Real-time**: WebSocket (Django Channels + Redis)

### 🚀 Development Approach

We follow an **agile development methodology** starting with an ultra-thin MVP:

#### Phase 1: Ultra-thin MVP (1-2 days)
- Single user (no social features)
- Fixed reading plan (Psalms 1-7 for one week)
- Basic check-in + reflection functionality
- Simple completion rewards (badge display)
- Ask Pastor form (non-real-time)
- SQLite + single-node deployment

#### Phase 2: Feature Enhancement (2-3 weeks)
- Customizable reading plans
- Friend system and social sharing
- Enhanced reflection sharing with visibility controls
- Upgraded Ask Pastor with private messaging
- Mini-games and achievement system

#### Phase 3: Production Ready (1 week)
- PostgreSQL migration
- Docker containerization
- Performance optimization
- Security hardening
- Monitoring and backup systems

### 📋 Project Milestones

- **v0.1**: Ultra-thin MVP
- **v0.2**: Customizable reading plans
- **v0.3**: Basic social features
- **v0.4**: Reflection sharing & visibility
- **v0.5**: Ask Pastor upgrade
- **v0.6**: Mini-games & achievements
- **v0.7**: Management & moderation
- **v1.0**: Production ready

### 🏗️ Project Structure

```
faithlog/
├── docs/                    # Project documentation
├── testing_codes/          # Test scripts and utilities
├── backend/                # Django application (to be created)
├── deploy/                 # Deployment configurations
└── README.md              # This file
```

### 🚦 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/david2004kang/faithlog.git
   cd faithlog
   ```

2. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

### 📖 Documentation

- [Project Milestones](docs/project_milestones.md)
- [Task List](docs/project_tasklist.md)

### 🤝 Contributing

This project follows agile development principles. Please check the GitHub Issues and Milestones for current tasks and priorities.

### 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 中文

### 🎯 專案概述

**FaithLog** 是一個結合每日讀經與遊戲化元素的現代網路應用程式，旨在鼓勵持續的靈性成長。使用 Django 建構並遵循敏捷開發原則，從最小可行產品（MVP）開始，逐步迭代增加功能。

### ✨ 核心功能

1. **📚 讀經計劃管理** - 設定聖經讀經進度和每日計劃
2. **🎮 獎勵機制** - 完成每日讀經後的小遊戲和徽章獎勵
3. **👥 社交分享** - 與朋友分享進度和讀經感想
4. **💬 問問牧者** - 私密訊息功能，可詢問小組長或牧師

### 🛠️ 技術架構

- **後端**: Django 5 + Django REST Framework + Django Channels
- **前端**: Django Templates + HTMX + Tailwind CSS
- **資料庫**: SQLite (MVP) → PostgreSQL (生產環境)
- **部署**: SSH + Gunicorn (MVP) → Docker Compose (生產環境)
- **即時通訊**: WebSocket (Django Channels + Redis)

### 🚀 開發方法

我們採用**敏捷開發方法**，從超薄 MVP 開始：

#### 第一階段：超薄 MVP (1-2 天)
- 單人使用（無社交功能）
- 固定讀經計劃（一週詩篇 1-7）
- 基本打卡 + 心得功能
- 簡單完成獎勵（徽章顯示）
- Ask 牧者表單（非即時）
- SQLite + 單節點部署

#### 第二階段：功能增強 (2-3 週)
- 可自訂讀經計劃
- 好友系統和社交分享
- 增強的心得分享與可見度控制
- 升級的 Ask 牧者私訊功能
- 小遊戲和成就系統

#### 第三階段：生產就緒 (1 週)
- PostgreSQL 遷移
- Docker 容器化
- 效能優化
- 安全性強化
- 監控和備份系統

### 📋 專案里程碑

- **v0.1**: 超薄 MVP
- **v0.2**: 可設定讀經計劃
- **v0.3**: 簡單社交功能
- **v0.4**: 心得分享與可見度
- **v0.5**: Ask 牧者升級
- **v0.6**: 小遊戲與成就系統
- **v0.7**: 管理與審核
- **v1.0**: 生產環境就緒

### 🏗️ 專案結構

```
faithlog/
├── docs/                    # 專案文檔
├── testing_codes/          # 測試腳本和工具
├── backend/                # Django 應用程式（待建立）
├── deploy/                 # 部署配置
└── README.md              # 本檔案
```

### 🚦 開始使用

1. **複製儲存庫**
   ```bash
   git clone https://github.com/david2004kang/faithlog.git
   cd faithlog
   ```

2. **設定環境**
   ```bash
   cp .env.example .env
   # 編輯 .env 檔案，填入你的資料庫憑證
   ```

3. **安裝相依套件**
   ```bash
   pip install -r requirements.txt
   ```

4. **執行資料庫遷移**
   ```bash
   python manage.py migrate
   ```

5. **啟動開發伺服器**
   ```bash
   python manage.py runserver
   ```

### 📖 文檔

- [專案里程碑](docs/project_milestones.md)
- [任務清單](docs/project_tasklist.md)

### 🤝 貢獻

本專案遵循敏捷開發原則。請查看 GitHub Issues 和 Milestones 了解目前的任務和優先順序。

### 📄 授權

本專案為開源專案，採用 [MIT 授權條款](LICENSE)。

---

## 🔗 Links

- **GitHub Repository**: [https://github.com/david2004kang/faithlog](https://github.com/david2004kang/faithlog)
- **Documentation**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/david2004kang/faithlog/issues)
- **Milestones**: [GitHub Milestones](https://github.com/david2004kang/faithlog/milestones)
