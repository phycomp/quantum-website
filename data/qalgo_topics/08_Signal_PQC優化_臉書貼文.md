# Facebook 貼文：Signal 協定 PQC 優化

## 貼文內容

🔒 Signal 協定的後量子密碼學強化

Signal 作為全球安全通訊指標，正在進行 PQC 強化：

KEM 混合建構：
• ML-KEM-768（後量子）+ X25519（傳統 ECDH）
• 密鑰組合：KDF-256(SS_ml-kem ‖ SS_x25519 ‖ Ciphertexts)
• 安全等級：取兩者較高者（後量子安全）

ML-DSA 數位簽章：
• NIST 等級 3（AES-192 對等）
• 公鑰 1,952 B、簽章 3,293 B
• 混合簽章：Sig_ed25519(m) ‖ Sig_ml-dsa(m)

Signal 協定重新建構：
• 群組金鑰樹（二叉樹結構，O(log n) 更新）
• 雙棘輪升級（DH Ratchet + Symmetric Ratchet + KEM Ratchet）
• 群組管理優化（批次更新、延遲重新加密、快取策略）

安全性提升：
• 機密性：傳統安全 → 後量子安全
• 前向保密：有限期間 → 長期保護
• 不可否認性：Ed25519 → 雙重保障

#Signal #PQC #後量子密碼學 #MLKEM #MLDSA #加密通訊 #端到端加密