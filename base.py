import logging

class Xembly:
    # Get logger.
    @staticmethod
    def log():
        if not hasattr(Xembly, 'logger'):
            Xembly.logger = logging.getLogger()
            Xembly.logger.setLevel(logging.ERROR)
            formatter = logging.Formatter('%(levelname)s: %(message)s')
            handler = logging.StreamHandler()
            handler.setFormatter(formatter)
            Xembly.logger.addHandler(handler)
        return Xembly.logger

    # Code base abstraction
    class Base:
        # Ctor.
        # +opts+:: Options
        def __init__(self, opts):
            self.opts = opts
            if self.opts.verbose:
                Xembly.log().setLevel(logging.INFO)
            Xembly.log().info("my version is {}".format(Xembly.VERSION))
            Xembly.log().info("Python version is {} at {}".format(sys.version, sys.platform))

        # Generate XML.
        def xml(self):
            if self.opts.xml:
                with open(self.opts.xml, 'r') as file:
                    xml = file.read()
                Xembly.log().info("reading {}".format(self.opts.xml))
            else:
                xml = sys.stdin.read()
                Xembly.log().info('reading STDIN')
            if self.opts.dirs:
                with open(self.opts.dirs, 'r') as file:
                    dirs = file.read()
                Xembly.log().info("reading directives from {}".format(self.opts.dirs))
            else:
                Xembly.log().info("{} directives in command line".format(len(self.opts.arguments)))
                dirs = ''.join(self.opts.arguments)
            return Xembler(Directives(dirs)).apply(xml).to_xml()

