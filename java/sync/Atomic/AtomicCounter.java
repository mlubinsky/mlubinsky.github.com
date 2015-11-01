import java.util.concurrent.atomic.AtomicInteger;
public class AtomicCounter {
 
	private final AtomicInteger counter = new AtomicInteger(0);

	public int getCount() {
		return counter.get();
	}
	

	public final int increment(){
		return counter.incrementAndGet();
	}
	
	public final int decrement(){
		return counter.decrementAndGet();
	}
 
}
