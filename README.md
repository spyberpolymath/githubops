# GitHub Ops Protocol

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A cyberpunk-styled command-line and web-based tool for managing multiple GitHub repositories with advanced automation features. Streamline your GitHub workflow with neon aesthetics, powerful operations, and an intuitive web dashboard.

## 🌟 Features

- **🔍 Multi-Repository Management**: Scan and manage multiple Git repositories in your workspace
- **🎯 Selective Pushing**: Choose specific repositories or push to all with intelligent selection
- **🔄 Change Detection**: Automatically detect repositories with uncommitted changes
- **🌈 Cyberpunk UI**: Immersive terminal interface with neon colors and glitch effects
- **�️ Web Dashboard**: Modern web interface for repository management and monitoring
- **🧷 GitHub Integration**: Seamless integration with GitHub API for repository operations
- **⚡ Batch Operations**: Perform operations on multiple repositories simultaneously
- **📊 Status Monitoring**: Real-time status updates and progress tracking
- **🛡️ Error Handling**: Robust error handling with detailed feedback

## 🚀 Installation

### 📋 Prerequisites

- 🐍 Python 3.7 or higher
- 📚 Git installed and configured
- 👤 GitHub account (for API operations)

### 🛠️ Setup

1. **📥 Clone the repository:**
   ```bash
   git clone https://github.com/spyberpolymath/githubops.git
   cd githubops
   ```

2. **📦 Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **🔧 Configure environment variables:**
   Create a `.env` file in the root directory:
   ```env
   GITHUB_TOKEN=your_github_personal_access_token
   GITHUB_USERNAME=your_github_username
   ```

## 📖 Usage

### 🎮 Basic Commands

1. **🚀 Initialize the tool:**
   ```bash
   python githubops.py
   ```

2. **🔍 Scan repositories:**
   The tool automatically scans your current directory and subdirectories for Git repositories.

3. **🎯 Select repositories:**
   Choose repositories to operate on using various selection methods:
   - 🔸 Single repository: Enter the number (e.g., `1`)
   - 🔹 Multiple repositories: Enter comma/space separated numbers (e.g., `1,3,5` or `1 3 5`)
   - 🔄 All repositories: Enter `all`
   - ⚡ Only changed repositories: Enter `changed`

### 🚀 Advanced Features

- **📁 Repository Structure Display**: View your repositories organized by visibility (public/private)
- **🔄 Change Tracking**: Identify repositories with pending commits
- **📤 Batch Push Operations**: Push changes to multiple repositories at once
- **📊 Progress Monitoring**: Real-time progress bars and status updates

## ⚙️ Configuration

### 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GITHUB_TOKEN` | 🔑 GitHub Personal Access Token | ✅ Yes |
| `GITHUB_USERNAME` | 👤 Your GitHub username | ✅ Yes |

### 🔑 GitHub Token Setup

1. 🌐 Go to [GitHub Settings > Developer settings > Personal access tokens (classic)](https://github.com/settings/tokens)
2. 🆕 Generate a new token with `repo` scope
3. 💾 Add the token to your `.env` file

## 🏗️ Project Structure

```
githubops/
├── 📄 githubops.py          # Main application script
├── 🪪 LICENSE               # MIT LICENSE
├── 📋 requirements.txt      # Python dependencies
├── 🔧 .env                  # Environment configuration (create this)
└── 📖 README.md             # This file
```

## 🔧 Dependencies

- 📡 `requests` - HTTP library for API calls
- 🔐 `python-dotenv` - Environment variable management
- 🛡️ `certifi` - SSL certificate verification
- 🔤 `charset-normalizer` - Character encoding detection
- 🌐 `urllib3` - HTTP connection pooling

## 🤝 Contributing

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔄 Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## � Future Features & Roadmap

We're continuously evolving GitHub Ops Protocol with exciting new capabilities. Here's what's planned for future releases:

### 🚀 Upcoming Features

- **🔄 Pull Request Management**: Create, review, and merge PRs across multiple repositories
- **📋 Issue Tracking**: Automated issue creation, assignment, and status monitoring
- **📊 Repository Analytics**: Detailed insights into repository health, activity, and contributions
- **💾 Automated Backups**: Scheduled repository backups with cloud storage integration
- **🔗 CI/CD Integration**: Seamless integration with GitHub Actions, Jenkins, and other CI/CD platforms
- **🌿 Advanced Branch Management**: Smart branch creation, merging strategies, and cleanup automation
- **👥 Collaboration Tools**: Team productivity features with shared workflows and templates
- **🖥️ Web Dashboard**: Modern web interface for repository management and monitoring
- **🔌 API Endpoints**: RESTful API for third-party integrations and automation
- **🧩 Plugin System**: Extensible architecture with community-contributed plugins

### 🔧 Platform Integrations

- **🐙 GitHub Enterprise**: Support for GitHub Enterprise Server instances
- **🏢 GitLab Integration**: Cross-platform repository management
- **🐺 Bitbucket Support**: Atlassian Bitbucket repository operations
- **☁️ Cloud Storage**: AWS S3, Google Cloud Storage, Azure Blob Storage for backups
- **📧 Notification Services**: Slack, Discord, Microsoft Teams, and email notifications
- **🔐 Security Tools**: Integration with security scanning tools (SonarQube, Snyk, etc.)

### 📈 Advanced Analytics & Reporting

- **📊 Contribution Metrics**: Detailed contributor statistics and activity reports
- **📈 Repository Insights**: Code quality metrics, language distribution, and growth trends
- **⏰ Time-based Analytics**: Historical data analysis and trend forecasting
- **🎯 Performance Monitoring**: Repository performance metrics and optimization suggestions
- **📋 Custom Reports**: Generate tailored reports for different stakeholder needs

### 🤖 Automation & AI Features

- **🧠 Smart Suggestions**: AI-powered recommendations for repository management
- **⚡ Auto-optimization**: Intelligent suggestions for repository structure and workflows
- **🔍 Code Analysis**: Automated code review suggestions and best practices
- **📝 Auto-documentation**: Generate README files and documentation automatically
- **🎨 Theme Customization**: Additional UI themes and personalization options

### 🛡️ Enterprise Features

- **🔐 SSO Integration**: Single Sign-On support for enterprise environments
- **👥 Team Management**: Advanced team collaboration and permission management
- **📊 Audit Logs**: Comprehensive logging and audit trails for compliance
- **🔒 Security Policies**: Enforce security standards across all repositories
- **📋 Compliance Tools**: Automated compliance checking and reporting

### 🌟 Quality of Life Improvements

- **⌨️ Keyboard Shortcuts**: Enhanced CLI shortcuts for power users
- **🎨 Custom Themes**: Additional cyberpunk and retro themes
- **🌍 Multi-language Support**: Internationalization and localization
- **📱 Mobile Companion**: Mobile app for on-the-go repository management
- **🔔 Smart Notifications**: Intelligent notification filtering and prioritization

### 💡 Community Requested Features

- **🔗 Repository Templates**: Create and manage repository templates
- **📦 Package Management**: Integration with package registries (npm, PyPI, etc.)
- **🔄 Migration Tools**: Repository migration between platforms
- **📸 Screenshots & Demos**: Automated screenshot generation for repositories
- **🎥 Video Tutorials**: Integrated help system with video guides

---

*Have a feature request? [Open an issue](https://github.com/spyberpolymath/githubops/issues) or contribute to the development!*

---

## 🏷️ Footer

<div align="center">

**👨‍💻 Aman Anil** (aka **SpyberPolymath**)

*Crafting digital experiences with passion and precision*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-spyberpolymath-blue)](https://linkedin.com/in/spyberpolymath)
[![GitHub](https://img.shields.io/badge/GitHub-spyberpolymath-black)](https://github.com/spyberpolymath)
[![Kaggle](https://img.shields.io/badge/Kaggle-spyberpolymath-orange)](https://kaggle.com/spyberpolymath)

**📧 projects@spyberpolymath.com** | **🌐 [spyberpolymath.com](https://spyberpolymath.com)**

---

*Made with ❤️ by Aman Anil aka (SpyberPolymath)* ✨

</div>