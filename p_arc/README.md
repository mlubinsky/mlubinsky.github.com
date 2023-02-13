- Functional Requirements (Features)
- Non-Functional Requirements (Scale, Latency, Availability, Security, Reliability)
- Traffic & Capacity Estimates
- Choice of Database
- Bottlenecks & tradeoffs

### Caching

```
𝐒𝐮𝐢𝐭𝐚𝐛𝐥𝐞 𝐒𝐜𝐞𝐧𝐚𝐫𝐢𝐨𝐬:
- In-memory solution
- Read heavy system
- Data is not frequently updated

𝐂𝐚𝐜𝐡𝐢𝐧𝐠 𝐓𝐞𝐜𝐡𝐧𝐢𝐪𝐮𝐞𝐬:
- Cache aside
- Write-through
- Read-through
- Write-around
- Write-back

𝐂𝐚𝐜𝐡𝐞 𝐄𝐯𝐢𝐜𝐭𝐢𝐨𝐧 𝐀𝐥𝐠𝐨𝐫𝐢𝐭𝐡𝐦𝐬:
- Least Recently Used (LRU)
- Least Frequently Used (LFU)
- First-in First-out (FIFO)
- Random Replacement (RR)

𝐊𝐞𝐲 𝐌𝐞𝐭𝐫𝐢𝐜𝐬:
- Cache Hit Ratio
- Latency
- Throughput
- Invalidation Rate
- Memory Usage
- CPU usage
- Network usage

𝐎𝐭𝐡𝐞𝐫 𝐢𝐬𝐬𝐮𝐞𝐬:
- Thunder herd on cold start
- Time-to-live (TTL)
```



https://cloud.google.com/blog/topics/developers-practitioners/what-data-pipeline-architecture-should-i-use/

https://engineering.fb.com/2023/01/31/production-engineering/meta-asynchronous-computing/

https://cloud.google.com/docs/tutorials?doctype=embeddedtutorial Google Cloud
