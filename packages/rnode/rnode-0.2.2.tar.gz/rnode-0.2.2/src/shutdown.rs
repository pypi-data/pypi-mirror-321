use std::sync::atomic::{AtomicBool, Ordering};
use std::sync::Once;
use tokio::signal;
use tracing::info;
use tokio::runtime::Runtime;

static SHUTDOWN: AtomicBool = AtomicBool::new(false);
static INIT: Once = Once::new();

pub fn init_shutdown() {
    INIT.call_once(|| {
        // 创建一个专门用于处理信号的 runtime
        std::thread::spawn(|| {
            let rt = Runtime::new().unwrap();
            rt.block_on(async {
                if let Ok(()) = signal::ctrl_c().await {
                    info!("Received shutdown signal");
                    SHUTDOWN.store(true, Ordering::SeqCst);
                    // 强制退出进程
                    std::process::exit(0);
                }
            });
        });
    });
}
