# Reasongraph 0.5.0 Release Notes

## 🎉 Major Release: Distance Intelligence & Ontology Hub Complete

**Release Date:** May 11, 2026  
**Version:** 0.5.0  

---

## 🚀 **MAJOR HIGHLIGHTS**

### **Distance Intelligence Framework** (PR #502, @KaifAhmad1)
- **Embedding Cache Optimization**: Per-session graph revision-based caching for 10x+ performance improvement
- **Advanced UI Features**: Ego mode, overlays, heatmap, and path inspector
- **Semantic Neighborhood Search**: Context-aware similarity with proximity metrics
- **Distance Matrix API**: N×N semantic distance calculations with caching

### **Complete Ontology Hub Suite** (PR #517, @KaifAhmad1 @ZohaibHassan16)
- **Alignments Tab** (PR #524): Cross-ontology alignment authoring with ML suggestions
- **Health Dashboard** (PR #524): Quality scoring across 5 dimensions with issue tracking
- **SHACL Studio** (PR #524): Interactive shape generation and validation
- **Visual Editor** (PR #519): Canvas-based ontology authoring without hand-coding
- **Registry & Search** (PR #518): Comprehensive ontology management and discovery

### **Security Hardening** (Security Enhancement PR, @KaifAhmad1)
- **12 Critical Vulnerabilities Fixed**: Eval injection, XXE, SQL injection, and more
- **SSRF Protection**: Comprehensive URL validation and hostname resolution
- **Input Validation**: Enhanced file upload restrictions and format detection
- **CORS & Headers**: Proper security headers and WebSocket protection

---

## 📊 **BY THE NUMBERS**

- **12 Major Features** ✅ Tested & Verified
- **16 Ontology Hub API Endpoints** ✅ Production Ready  
- **57 New Distance Intelligence Tests** ✅ All Passing
- **32 Parquet Ingestion Tests** ✅ All Passing
- **12 Security Vulnerabilities** ✅ All Patched
- **100% Test Coverage** ✅ Core Features Verified

---

## 🔧 **NEW FEATURES**

### **Performance & Architecture**
- **Distance Intelligence Embedding Cache** (PR #502, @KaifAhmad1): Thread-safe per-session caching with automatic invalidation
- **Parquet File Ingestion** (PR #548, @Luffy2208): PyArrow backend with column selection and partition support
- **Indexed Search** (PR #481, @ZohaibHassan16): O(log n) search for large graphs (118k nodes: 24ms → 0.004ms)

### **Ontology Hub Suite**
- **Cross-ontology Alignments** (PR #524, @KaifAhmad1 @ZohaibHassan16): ML-powered suggestions with confidence scoring
- **Quality Health Dashboard** (PR #524, @KaifAhmad1 @ZohaibHassan16): 5-dimension scoring with actionable issue tracking
- **SHACL Studio** (PR #524, @KaifAhmad1 @ZohaibHassan16): Interactive shape authoring with Monaco editor
- **Visual Ontology Editor** (PR #519, @KaifAhmad1): Drag-and-drop ontology construction
- **16 Backend Endpoints** (PRs #518, #519, #524, @KaifAhmad1 @ZohaibHassan16): Complete CRUD and analysis capabilities

### **UI & User Experience**
- **Distance Intelligence UI** (PR #502, @KaifAhmad1 @ZohaibHassan16): Ego mode, overlays, heatmap, path inspector
- **Explorer Redesign** (PR #516, @ZohaibHassan16): Modern hero section with live metrics
- **Graph Workspace Declutter** (PR #483, @ZohaibHassan16): Improved visualization for dense graphs
- **Bidirectional Path Finding** (PR #469, @KaifAhmad1): Undirected traversal support

### **Platform Compatibility**
- **Windows Installation Fixes** (PR #532, @KaifAhmad1): Removed faiss-gpu from [all], Unicode console support
- **Cross-platform Dependencies** (PR #527, @ZohaibHassan16): Proper optional dependency management
- **MCP Server Package Structure** (PR #541, @KaifAhmad1): Fixed pipx installation issues

### **Algorithm Enhancements**
- **DuplicateDetector Result Limiting** (PR #534, @KaifAhmad1): Ranking, sorting, and incremental detection features
- **ConflictDetector Parameter Handling** (PR #533, @KaifAhmad1): Method parameter validation and error handling

---

## 🛡️ **SECURITY IMPROVEMENTS** (Security Enhancement PR, @KaifAhmad1)

### **Critical Fixes**
- **Eval Injection** (CWE-95): Replaced with `fractions.Fraction` in media parser
- **Pickle Deserialization** (CWE-502): Switched to JSON with migration support
- **SQL Injection** (CWE-89): Parameterized queries and input validation
- **XXE Protection** (CWE-611): `defusedxml` hardening for all RDF parsing

### **Web Security**
- **SSRF Protection**: URL validation with hostname resolution
- **CORS Hardening**: Narrowed origins and WebSocket limits
- **Security Headers**: HSTS, X-Content-Type-Options, X-Frame-Options
- **Path Traversal**: `Path.resolve().relative_to()` protection

### **Input Validation**
- **File Upload Restrictions**: Extension allowlist and size limits
- **SPARQL Limits**: Row caps, timeouts, and concurrency controls
- **ReDoS Prevention**: Eliminated polynomial regex patterns

---

## 🔍 **QUALITY ASSURANCE**

### **Testing Coverage**
- **Distance Intelligence**: 57 new tests, 100% passing
- **Parquet Ingestion**: 32 tests, comprehensive coverage
- **Security Fixes**: 14 vulnerability-specific tests
- **UI Components**: All major features verified
- **Platform Tests**: Windows, Linux compatibility confirmed

### **Performance Benchmarks**
- **Embedding Cache**: 10x+ improvement in repeated requests
- **Search Performance**: 6,000x faster for large graphs
- **Memory Efficiency**: Lazy loading and optional dependencies
- **Concurrent Operations**: Thread-safe caching with locks

---

## 🔄 **BREAKING CHANGES**

### **Dependencies**
- **Windows Users**: `faiss-gpu` removed from `[all]` - install `[gpu]` explicitly if needed
- **Optional Dependencies**: Now lazy-loaded to improve import performance

### **API Changes**
- **ConflictDetector**: Fixed duplicate method definitions with proper parameter handling
- **DuplicateDetector**: New result limiting and ranking options

---

## 📚 **DOCUMENTATION**

- **Comprehensive Changelog**: Detailed feature descriptions and credits
- **API Documentation**: All new endpoints documented
- **Security Advisory**: Complete vulnerability disclosure and fixes
- **Migration Guide**: Breaking changes and upgrade instructions

---

## 🚀 **INSTALLATION**

```bash
# Standard installation
pip install reasongraph==0.5.0

# With all optional dependencies (cross-platform)
pip install "reasongraph[all]==0.5.0"

# With GPU acceleration (Linux only)
pip install "reasongraph[gpu]==0.5.0"

# With Parquet support
pip install "reasongraph[ingest-parquet]==0.5.0"
```

---

## 📈 **WHAT'S NEXT FOR 0.5.0**

The 0.5.0 release establishes Reasongraph as a production-ready framework for:

- **Enterprise Knowledge Engineering** with comprehensive ontology management
- **Advanced Analytics** through distance intelligence and semantic search  
- **Security-First Design** with comprehensive vulnerability protection
- **Cross-Platform Compatibility** supporting diverse deployment environments

**Immediate next steps for 0.5.0:**
- PyPI package publication and distribution
- Docker image updates with new features
- Documentation website deployment with updated guides
- Community outreach and feature announcements
- Integration testing across different deployment scenarios

---

**🎯 Reasongraph 0.5.0: Production-Ready Knowledge Engineering Platform**
