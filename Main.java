/* Do Not Modify RuleType */
enum RuleType {
	ComputeLength,
	Encrypt,
	ConvertCase
}

/*
 * Do Not Modify RuleProcessor
 * Create separate RuleProcessor implementation for each rule type.
 */
interface RuleProcessor {
	RuleType getType();

	String process(String input);
}

/*
 * Do Not Modify.
 * Implement the following interface to return different RuleProcessor based on
 * the Rule type. Use factory pattern and singleton pattern.
 */
interface ProcessorEngineFactory {
	RuleProcessor getEngine(RuleType type);
}

/* Rename this class using your role and name */
public class Main {

	/* Implement following function */
	private static ProcessorEngineFactory getFactory() {

	}

	/* DO NOT MODIFY main() method */
	public static void main(String[] args) {
		ProcessorEngineFactory factory = getFactory();
		RuleProcessor processor;
		String input, output;

		processor = factory.getEngine(RuleType.ComputeLength);
		input = "sedutperspiciatisundeomnisistenatuserrorsitvolu";
		output = processor.process(input);
		System.out.println("ComputeLength - output: " + output + "\n\n");

		processor = factory.getEngine(RuleType.ConvertCase);
		input = "KJBLlkjbLBLJBHlkBlBVLKJjblkbjlKhblKGuyTghvgDTghkJL";
		output = processor.process(input);
		System.out.println("ConvertCase - output: " + output + "\n\n");

		processor = factory.getEngine(RuleType.Encrypt);
		input = "sedutperspiciatisundeomnisisten";
		output = processor.process(input);
		System.out.println("Encrypt - output: " + output + "\n\n");
	}

}
