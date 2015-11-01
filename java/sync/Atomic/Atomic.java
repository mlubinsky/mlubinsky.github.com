public class Atomic {
	
    private AtomicCounter counter = new AtomicCounter();
	public static void main(String[] args) {
		Atomic a = new Atomic();
		a.run();
	}
 
	private  void run() {
		
		for (int i = 0; i < 100; i++) {
			new Thread(new Increment()).start();
			new Thread(new Decrement()).start();
			new Thread(new Increment()).start();
		}
		
		try {
			Thread.sleep(10000);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
 
		System.out.println("Final Counter " + counter.getCount());
 
	}
 
	private class Increment implements Runnable {
 
		@Override
		public void run() {
			try {
				Thread.sleep(10);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			counter.increment();
		}
	}
 
	private class Decrement implements Runnable {
		@Override
		public void run() {
			try {
				Thread.sleep(10);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
			counter.decrement();
		}
	}
 
}