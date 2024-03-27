/*
Build three rule processor classes (which implements RuleProcessor interface)
for the three rule types: ComputeLength, Encrypt, and ConvertCase. Then implement the
ProcessorEngineFactory interface to return the processor class based on rule type. Follow
Factory pattern to return the processor class. Also, follow the singleton pattern when
creating the processor class instances. Look into the attached Java file for boilerplate. Do
not modify the main function. Follow the comment in the code file for more instructions.

Processor classes will call the process function as following:
	1. For RuleType.ComputeLength, return the number of unique characters in the input
	string. Ignore the case.
	2. For RuleType.Encrypt, replace each character T, replace it with T+n. Where n = (
	Last two digits of your roll ) % 13. Example:
	a. Say your roll is 15, then n = 15%13 = 2
	b. If T is ‘b’, then replace it with ‘b’+2 = ‘d’
	c. If T is ‘z’ then replace it with ‘z’+2=’b’
	d. The string “abyc” will become “cdae” (for n=2)
	3. For RuleType.ConvertCase, reverse the case of all characters. For example:
	“dEayRk” will become: “DeAYrK”
*/

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
