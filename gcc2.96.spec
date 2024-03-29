
# PLEASE READ BEFORE BUILDING!
# (anssi) 2007-09-16, FIXME/TODO
# This package is not buildable with current gcc, but it can be built
# either with itself or with gcc3.3. It needs a patch for new bison or
# an older bison bundled. However, when built with glibc 2.4/2.6, the
# shared object file libstdc++-libc6.2-2.so.3 will contain undefined
# symbols. You can test for this with, for example, old Mozilla Phoenix
# prereleases which are linked against this lirary. It builds correctly
# with 2006.0 glibc 2.3. This has not been investigated further, yet.

%define _unpackaged_files_terminate_build 0
# RH-118, DB-5
%define name			gcc%{package_suffix}
%define branch			2.96
%define cvsversion		20000731
%define oversion		2.95.2
%define libstdc_version		2.10.0
%define color_gcc_version	1.3.2
%define gcc_version		2.96
%define gcc_release		0.83mdk
%define gcc_target_platform	%{_target_platform}

# Define old libgcj release tag before phagocytation + 1
%define old_libgcj_release	%mkrel 9

# Actually where libgcj.jar should go
%define gcc_datadir             %{_datadir}/gcc-%{version}


%define system_compiler		0
%if %{system_compiler}
# Priorities for Mandrake Linux 9.0 are:
# gcc-3.2     : 10 (default)
# gcc-"2.96"  :  6
# gcc-3.0.X   :  5
%define alternative_priority	10
%define package_suffix		%{nil}
%define program_suffix		%{nil}
%else
%define alternative_priority	6
%define package_suffix		%{branch}
%define program_suffix		-%{version}
%endif

%define build_debug		0
%define build_testsuite		0
%if %{system_compiler}
%define build_colorgcc		1
%define build_doc		1
%define build_pdf_doc		0
%define build_fortran		1
%define build_objc		1
%define build_java		1
%else
# I don't want the doc subpackage
%define build_colorgcc		0
%define build_doc		0
%define build_pdf_doc		0
%define build_fortran		0
%define build_objc		0
%define build_java		0
%endif

# Allow --with[out] <feature> at rpm command line build
%{?_without_PDF: %{expand: %%define build_pdf_doc 0}}
%{?_without_DEBUG: %{expand: %%define build_debug 0}}
%{?_with_PDF: %{expand: %%define build_pdf_doc 1}}
%{?_with_DEBUG: %{expand: %%define build_debug 1}}

# Allow --without <front-end> at rpm command line build
%{?_with_F77: %{expand: %%define build_fortran 1}}
%{?_with_JAVA: %{expand: %%define build_java 1}}
%{?_with_OBJC: %{expand: %%define build_objc 1}}

# Allow --with <front-end> at rpm command line build
%{?_without_F77: %{expand: %%define build_fortran 0}}
%{?_without_JAVA: %{expand: %%define build_java 0}}
%{?_without_OBJC: %{expand: %%define build_objc 0}}

%{expand:%%define mdk_version %(A=$(awk '{print $4}' /etc/mandrake-release); if [ -n "$A" ];then echo $A;else echo Cooker;fi)}

Summary:	Various compilers (C, C++, Objective-C, ...)
Name:		%{name}
Version:	%{gcc_version}
Release:	%{gcc_release}
License:	GPL
Group:		Development/C

# Sources
Source0:	ftp://ftp.gnu.org/pub/gnu/gcc/gcc-%{oversion}.tar.bz2
Source2:	libgcj-%{version}.tar.bz2
Source3:	boehm-gc-3.1-20020314.tar.bz2
Source5:	egcs-libstdc++-compat.tar.bz2

# Red Hat patches
patch0: gcc-2.96-cvs-update-%{cvsversion}.patch
Patch2: gcc-new-abi.patch
Patch4: gcc-c++-typedef.patch
Patch5: gcc-no-warn-trigraphs.patch
Patch6: gcc-incomplete-struct.patch
Patch8: gcc-libstdc++-v3-wnoerror.patch
Patch9: gcc-string-crash.patch
Patch10: gcc-sparc64-subreg-byte.patch
Patch11: gcc-sparc64-reload.patch
Patch12: gcc-sparc64-startfile.patch
Patch13: gcc-sparc64-decloffset.patch
Patch14: gcc-sparc64-uname.patch
Patch15: gcc-sparc32-vaarg.patch
Patch16: gcc-sparc64-hwint.patch
Patch18: gcc-java-jword.patch
Patch19: gcc-align-memcpy.patch
Patch20: gcc-sparcv9-hack.patch
Patch21: gcc-stmtexpr.patch
Patch22: gcc-sparc32-hack.patch
Patch23: gcc-sparc32-hack2.patch
Patch25: gcc-clear-hack.patch
Patch28: gcc-loop.patch
Patch29: gcc-alpha-addressof.patch
Patch31: gcc-regmove-asm.patch
Patch33: gcc-cpplib.patch
Patch35: gcc-cpp0.patch
Patch36: gcc-canon-cond.patch
Patch37: gcc-bogus-subreg.patch
Patch38: gcc-cp-ii.patch
Patch39: gcc-subreg-gcse.patch
Patch40: gcc-subregbyte-gcse.patch
Patch41: gcc-combine-comparison.patch
Patch42: gcc-loop-noopt.patch
Patch43: gcc-loop-unroll.patch
Patch44: gcc-loop-test1.patch
Patch45: gcc-loop-test2.patch
Patch46: gcc-loop-scanloop.patch
Patch48: gcc-i386-ashlsilea.patch
Patch49: gcc-i386-lea.patch
Patch50: gcc-lowpart-test.patch
Patch51: gcc-loop-noopt2.patch
Patch52: gcc-i386-sibcall.patch
Patch53: gcc-cpp-warn.patch
Patch54: gcc-wint_t.patch
Patch55: gcc-format-checking.patch
Patch56: gcc-strftime.patch
Patch57: gcc-xopen.patch
Patch58: gcc-c99.patch
Patch59: gcc-iso-not-ansi.patch
Patch60: gcc-sibcall.patch
Patch61: gcc-Os-testcase.patch
Patch62: gcc-java-misc.patch
Patch63: gcc-java-bytecode.patch
Patch64: gcc-java-pg.patch
Patch65: gcc-commutative.patch
Patch66: gcc-relational.patch
Patch67: gcc-f-include.patch
Patch68: gcc-unroll.patch
Patch69: gcc-i386-strops.patch
Patch70: gcc-simplify-relational.patch
Patch71: gcc-alias.patch
Patch72: gcc-jsm1.patch
Patch73: gcc-jsm2.patch
Patch74: gcc-jsm3.patch
Patch75: gcc-scanf.patch
Patch76: gcc-jsm4.patch
Patch77: gcc-jsm5.patch
Patch78: gcc-jsm6.patch
Patch79: gcc-jsm7.patch
Patch80: gcc-jsm8.patch
Patch81: gcc-loop-hack.patch
Patch82: gcc-cpp-warnpaste.patch
Patch83: gcc-float-condmove.patch
Patch84: gcc-i386-call.patch
Patch85: gcc-i386-call2.patch
Patch86: gcc-i386-call-test.patch
Patch87: gcc-i386-arith.patch
Patch88: gcc-i386-ge_geu.patch
Patch89: gcc-i386-gotoff.patch
Patch90: gcc-java-catchup.patch
Patch91: gcc-java-no-super-layout.patch
Patch92: gcc-make-extraction.patch
Patch93: gcc-segv1.patch
Patch94: gcc-segv2.patch
Patch95: gcc-sparc-copy-leaf-remappable.patch
Patch96: gcc-wchar-const.patch
Patch97: gcc-libio.patch
Patch98: gcc-alpha-tune.patch
Patch99: gcc-alpha-unaligned.patch
Patch100: gcc-cpp-warnpaste2.patch
Patch101: gcc-loop-giv.patch
Patch102: gcc-real-value.patch
Patch103: gcc-sparc-const-pool.patch
Patch104: gcc-sparc64-timode.patch
Patch105: gcc-callersave-segv.patch
Patch106: gcc-libio-printf_fp.patch
Patch107: gcc-pt-enum.patch
Patch108: gcc-sparc-pic.patch
Patch109: gcc-subreg-byte-expmed.patch
Patch110: gcc-test-991206-1.patch
Patch111: gcc-alpha-mi-thunk.patch
Patch112: gcc-c++-pmf.patch
Patch113: gcc-f77-fdebug.patch
Patch114: gcc-libio-endl.patch
Patch115: gcc-i386-compare-test.patch
Patch116: gcc-sparc-may-trap.patch
Patch117: gcc-sparc-mi-thunk.patch
Patch118: gcc-c++-inline16-test.patch
Patch119: gcc-c++-named-return-value.patch
Patch120: gcc-c++-walk-tree.patch
Patch121: gcc-i386-reload-test.patch
Patch122: gcc-i386-reload.patch
Patch123: gcc-sibcall-unchanging.patch
Patch124: gcc-segv3.patch
Patch125: gcc-c++-crash24.patch
Patch126: gcc-do-store-flag.patch
Patch127: gcc-i386-address-cost.patch
Patch128: gcc-i386-arith2.patch
Patch129: gcc-i386-constraint-N.patch
Patch130: gcc-incomplete-aggregate-alias.patch
Patch131: gcc-sibcall-eh2.patch
Patch132: gcc-cpp-assert-crash.patch
Patch133: gcc-c++-undefined-method.patch
Patch134: gcc-sparc-4096.patch
Patch135: gcc-sparc64-reload-test.patch
Patch136: gcc-sparc64-reload2.patch
Patch137: gcc-subreg-byte-operand-subword.patch
Patch139: gcc-c++-static-class.patch
Patch140: gcc-c++-testset1.patch
Patch141: gcc-c++-testset2.patch
Patch142: gcc-place-field.patch
Patch143: gcc-sparc-output-formatting.patch
Patch144: gcc-sparc64-mi-thunk.patch
Patch145: gcc-sparc64-namedret.patch
Patch146: gcc-sparc64-nested-fn.patch
Patch147: gcc-c++-ice.patch
Patch148: gcc-alpha-fold-const.patch
Patch149: gcc-alpha-recog.patch
Patch150: gcc-c++-pointer-to-member-test.patch
Patch151: gcc-c++-sizetype.patch
Patch152: gcc-cpp-64k.patch
Patch153: gcc-cpp-empty-header.patch
Patch154: gcc-i386-regelim.patch
Patch155: gcc-sparc-builtin-setjmp.patch
Patch156: gcc-test-loop-7.patch
Patch157: gcc-c++-dump-expr.patch
Patch158: gcc-c++-inline-cmp.patch
Patch159: gcc-c++-inline-return.patch
Patch160: gcc-c++-label-scope.patch
Patch161: gcc-c++-ptm.patch
Patch162: gcc-c++-qual-error.patch
Patch163: gcc-const-fold.patch
Patch164: gcc-cpp-error-directive.patch
Patch165: gcc-i386-truncxfsf.patch
Patch166: gcc-integrate-clobber.patch
Patch167: gcc-libf2c-mkstemp.patch
Patch168: gcc-local-alloc.patch
Patch169: gcc-loop-hoistmem.patch
Patch170: gcc-sibcall-const.patch
Patch171: gcc-sibcall-emit-queue.patch
Patch172: gcc-unroll-iterations.patch
Patch173: gcc-volatile-local-var.patch
Patch174: gcc-c++-sizetype2.patch
Patch175: gcc-error-diagnostic.patch
Patch176: gcc-aggregate-mode.patch
Patch177: gcc-c++-addressof.patch
Patch178: gcc-aggregate-mode2.patch
Patch179: gcc-c++-addressof2.patch
Patch180: gcc-c++-inline-cmp2.patch
Patch181: gcc-cpp-fno-operator-names.patch
Patch182: gcc-c++-ggc-input.patch
Patch183: gcc-alpha-unaligned2.patch
Patch184: gcc-alpha-ze_and_ne.patch
Patch185: gcc-c++-wchar_t.patch
Patch186: gcc-cpp-arg-loop.patch
Patch187: gcc-cpp-fno-operator-names2.patch
Patch188: gcc-cpp-g3.patch
Patch189: gcc-fshort-wchar.patch
Patch190: gcc-max-strlen.patch
Patch191: gcc-stabs.patch
Patch192: gcc-subreg-byte-gcse2.patch
Patch193: gcc-tradcpp-MD.patch
Patch194: gcc-alpha-expand-block-move.patch
Patch195: gcc-c++-decl-needed.patch
Patch196: gcc-c++-nomods_initdcl0.patch
Patch197: gcc-cpp-MD.patch
Patch198: gcc-fixup-var-refs.patch
Patch199: gcc-frame-related.patch
Patch200: gcc-i386-cmpqi.patch
Patch201: gcc-i386-const-call-address.patch
Patch202: gcc-i386-fcmov.patch
Patch203: gcc-i386-sar.patch
Patch204: gcc-c++-extern-c.patch
Patch205: gcc-c++-inline-static.patch
Patch206: gcc-c++-inline-static2.patch
Patch207: gcc-cpp-M-include.patch
Patch208: gcc-integrate-compare.patch

Source209: gcc-cpp-20010126.tar.bz2
Patch209: gcc-cpp-20010126.patch
Patch210: gcc-objc-cpp-lineno.patch
Patch211: gcc-cpp-paste-avoid.patch
Patch212: gcc-cpp-paste-avoid2.patch

Patch213: gcc-c++-inline-modify_expr.patch
Patch214: gcc-i386-testqi_1.patch
Patch215: gcc-c++-anon-union.patch
Patch216: gcc-extract_bit_field.patch
Patch217: gcc-c++-overload-warn.patch
Patch218: gcc-cpp-implicit-extern-c.patch
Patch219: gcc-cpp-paste-avoid3.patch
Patch220: gcc-packed-enum-bitfield.patch
Patch221: gcc-variable-size.patch

# ia64 jumbo patch
Patch222: gcc-ia64.patch
Patch223: gcc-ia64-errata.patch

Patch224: gcc-cpp-defined-diag.patch
Patch225: gcc-cpp-paste-avoid4.patch
Patch226: gcc-dwarf2out-ice.patch
Patch227: gcc-g++.jason-2371.patch
Patch228: gcc-lex-line.patch
Patch229: gcc-alpha-unaligned3.patch
Patch230: gcc-consistency-test.patch
Source230: gcc-consistency-test.tar.bz2
Patch231: gcc-nested-parm.patch
Patch232: gcc-alpha-reload.patch
Patch233: gcc-alpha-shift.patch
Patch234: gcc-c++-init-copy-aggr.patch
Patch235: gcc-c++-inline-loop.patch
Patch236: gcc-c++-lookup.patch
Patch237: gcc-c++-taking-address-error.patch
Patch238: gcc-objc-gc.patch
Patch239: gcc-objc-test.patch
Patch240: gcc-reload-hardreg-free.patch
Patch241: gcc-cpp-20010222.patch
Patch242: gcc-expr-safety.patch
Patch243: gcc-debug-static-local.patch
Patch244: gcc-fixup-var-refs2.patch
Patch245: gcc-fold-const-div.patch
Patch246: gcc-g77-unused.patch
Patch247: gcc-ia64-flushrs.patch
Patch248: gcc-ia64-syscall-linkage.patch
Patch249: gcc-recog-addressof.patch
Patch250: gcc-cpp-20010309.patch
Patch251: gcc-cant-combine.patch
Patch252: gcc-i386-crtendS.patch
Patch253: gcc-reg-stack-clobber.patch
Patch254: gcc-reg-stack.patch
Patch255: gcc-store-expr.patch
Patch256: gcc-target-expr.patch
Patch257: gcc-c++-anonaggr-copy.patch
Patch258: gcc-c++-asmspec.patch
Patch259: gcc-c++-static-local.patch
Patch260: gcc-f77-line.patch
Patch261: gcc-libstdc++-getline.patch
Patch262: gcc-no-new-abi.patch
Patch263: gcc-regrename.patch
Patch264: gcc-subreg-byte-gcse3.patch
Patch265: gcc-wshadow-doc.patch
Patch266: gcc-c++-D__EXCEPTIONS.patch
Patch267: gcc-c++-throttle-inline.patch
Patch268: gcc-fold-pointer-cmp.patch
Patch269: gcc-ifcvt-strict-low-part.patch
Patch270: gcc-gcse-reg-equiv.patch
Patch271: gcc-null-pointer-check.patch
Patch272: gcc-local-inline.patch
Patch273: gcc-cpp-Wcomment.patch
Patch274: gcc-cselib-mode.patch
Patch275: gcc-dwarf2-O0-crash.patch
Patch276: gcc-dwarf2out-splice-child.patch
Patch277: gcc-i386-movcc.patch
Patch278: gcc-ia64-xdata.patch
Patch279: gcc-subregbyte-hard-regno.patch
Patch280: gcc-tradtradcpp0.patch
Patch281: gcc-flow-autoinc.patch
Patch282: gcc-ia64-constconst.patch
Patch283: gcc-ia64-G.patch
Patch284: gcc-integrate-error.patch
Patch285: gcc-MD-nodot.patch
Patch286: gcc-store-constructor-field.patch
Patch287: gcc-ia64-except.patch
Patch288: gcc-ia64-loc79.patch
Patch289: gcc-ia64-bstep.patch
Patch290: gcc-c++-templ-arg.patch
Patch291: gcc-frame-state-for-compat.patch
Patch292: gcc-sibcall-catch.patch
Patch293: gcc-tradcpp-define.patch
Patch294: gcc-c++-inline-method.patch
Patch295: gcc-gcse-trapping.patch
Patch296: gcc-nested-expr-stmt.patch
Patch297: gcc-__NO_INLINE__.patch
Patch298: gcc-bogus-inline.patch
Patch299: gcc-c++-defarg.patch
Patch300: gcc-c++-instantiate.patch
Patch301: gcc-c++-static-ctordtor.patch
Patch302: gcc-c++-templ-arg2.patch
Patch303: gcc-c++-ucs.patch
Patch304: gcc-fsyntax-only.patch
Patch305: gcc-g77-unsigned-char.patch
Patch306: gcc-hash-ident.patch
Patch307: gcc-jump-threading.patch
Patch308: gcc-regmove-unchanging.patch
Patch309: gcc-ia64-complex-float.patch
Patch310: gcc-ia64-movcc-fail.patch
Patch311: gcc-ia64-stop-bit.patch
Patch312: gcc-c++-friend.patch
Patch313: gcc-i386-stack-adjust.patch
Patch314: gcc-SHF_MERGE.patch
Patch315: gcc-dwarf2-filenames.patch
Patch316: gcc-k6-loop.patch
Patch317: gcc-libobjc-3.0.patch
Patch318: gcc-texinfo-texconfig.patch
Patch319: gcc-c++-complext.patch
Patch320: gcc-c++-conv-cv-ptr.patch
Patch321: gcc-c++-sstream-warn.patch
Patch322: gcc-f77-ffixed.patch
Patch323: gcc-invalid-stabs.patch
Patch324: gcc-libio-test.patch
Patch325: gcc-alpha-function-sections.patch
Patch326: gcc-alpha-vtable-gc.patch
Patch327: gcc-c++-anontypename.patch
Patch328: gcc-c++-array-cast.patch
Patch329: gcc-c++-colonequal.patch
Patch330: gcc-c++-cond-ovl.patch
Patch331: gcc-c++-weak-address.patch
Patch332: gcc-libio-input-float.patch
Patch333: gcc-subreg-byte-stabs.patch
Patch334: gcc-c++-array-side-effects.patch
Patch335: gcc-cpp-memleak.patch
Patch336: gcc-c++-template-throw.patch
Patch337: gcc-c++-tsubst-friend-class.patch
Patch338: gcc-dwarf2-debug-line.patch
Patch339: gcc-ifcvt-eh.patch
Patch340: gcc-ia64-vararg.patch
Patch341: gcc-gcse-hoist.patch
Patch342: gcc-ia64-eh.patch
Patch343: gcc-libio-stdstream-offset.patch
Patch344: gcc-objc-class-ref.patch
Patch345: gcc-tail-recurse.patch
Patch346: gcc-c++-sstream-seek.patch
Patch347: gcc-loop-combine-givs.patch
Patch348: gcc-alpha-asm-input.patch
Patch349: gcc-c++-anon-union2.patch
Patch350: gcc-c++-inline-sizeof-char.patch
Patch351: gcc-cpp-run-directive.patch
Patch352: gcc-reload-optional.patch
Patch353: gcc-fde-merge-compat.patch
Patch354: gcc-flow-setjmp.patch
Patch355: gcc-pure-reload.patch
Patch356: gcc-sparc-float.patch
Patch357: gcc-sparc-movdf.patch
Patch358: gcc-c++-member-init.patch
Patch359: gcc-autoconf-2.52.patch
Patch360: gcc-makej.patch
Patch361: gcc-ia64-bitfield-return.patch
Patch362: gcc-ia64-NaT.patch
Patch363: gcc-sparc-libcall.patch
Patch364: gcc-c++-preexpand-calls.patch
Patch365: gcc-libio-stdstreams-vptr.patch
Patch366: gcc-sparc-return.patch
Patch367: gcc-sparc64-nonzero-bits.patch
Patch368: gcc-below-sp.patch
Patch369: gcc-c++-setup-vtbl-ptr.patch
Patch370: gcc-reload-ofp.patch
Patch371: gcc-bitop-shorten.patch
Patch372: gcc-c++-ptrintsum.patch
Patch373: gcc-i386-fxch.patch
Patch374: gcc-i386-regparm-struct.patch
Patch375: gcc-ia64-encode-section-info.patch
Patch376: gcc-attr-visibility.patch
Patch377: gcc-store_field-expand_and.patch
Patch378: gcc-c++-array-ref.patch
Patch379: gcc-c++-flat-initializer.patch
Patch380: gcc-c++-static-member.patch
Patch381: gcc-i386-reg-stack-check.patch
Patch382: gcc-i386-zero-size.patch
Patch383: gcc-loop-check_dbra_loop.patch
Patch384: gcc-pedwarn-string-length.patch
Patch385: gcc-simplify-check-overflow.patch
Patch386: gcc-UDA-option-order.patch
Patch387: gcc-c++-pt-using.patch
Patch388: gcc-c++-pt-using2.patch
Patch389: gcc-attr-visibility2.patch
Patch390: gcc-libstdc++-libc-interface.patch
Patch391: gcc-attr-visibility3.patch
Patch392: gcc-ia64-thread-safe-eh.patch
Patch393: gcc-merge_blocks_nomove.patch
Patch394: gcc-attr-visibility4.patch
Patch395: gcc-unaligned-const.patch
Patch396: gcc-i386-piclabel.patch
Patch397: gcc-2.96-parallel.patch
Patch398: gcc-i386-andhi.patch
Patch399: gcc-mem-scratch.patch
Patch401: gcc-sparc-tfdi.patch
Patch402: gcc-c++-gc-named-label-list.patch
Patch403: gcc-cpp-include-dir.patch
Patch404: gcc-c++-compound-literal.patch
Patch405: gcc-c++-eh-spec-incomplete.patch
Patch406: gcc-fde-merge-compat-2.patch
Patch407: gcc-strict-alias-optimization.patch
Patch408: gcc-cpp-MD-2.patch

# Colorgcc: http://home.i1.net/~jamoyers/software/colorgcc/
Source4:	colorgcc-%{color_gcc_version}.tar.bz2
Patch500:	gcc-2.95.2-colorgcc-mdkconf.patch

# Debian
Patch501:	gcc-2.95.3-alpha-spec.patch

# s@(pc|unknow)@mdk@;
Patch502:	gcc-2.95.3-add-mdk-vendor.patch

# for PDF documentation
Patch503:	gcc-pdfdoc.patch
Patch504:	gcc-pdfg77.patch

# unroll.c (loop_iterations): Extend check for multiple back edges.
Patch600:	gcc-unroll-iterations2.patch

# unroll.c (loop_iterations): Give up on jumps with null JUMP_LABEL
# while scanning for multiple back edges.
Patch601:	gcc-unroll-iterations3.patch

# alpha.c: fix large app link errors
Patch602:	gcc-alpha-braddr-fix-2.96.patch

# decl.c (start_enum): Don't set TREE_ADDRESSABLE on TREE_LIST node.
# Fix GNATS PR c++/6037
Patch603:	gcc-c++-enum-fix.patch

# Merge patch from gcc 3.1 for a working --program-suffix
Patch604:	gcc-program-transform.patch

# c-common.c (split_specs_attrs): Allow for empty attributes with
# empty TREE_PURPOSE. (Joseph S. Myers)
Patch605:	gcc-pr4294.patch

# Patches for libgcj
Patch1001:	libgcj-makej.patch
Patch1002:	libgcj-nomultilib.patch
Patch1003:	libgcj-compile.patch
Patch1004:	libgcj-awt-color.patch
Patch1005:	libgcj-sigaction.patch
Patch1006:	libgcj-boehmgc.patch
Patch1007:	libgcj-libdeps.patch
Patch1008:	libgcj-boehmgc-dyn_load.patch
Patch1009:	libgcj-nozlib.patch
Patch1010:	libgcj-new-boehm-gc.patch
Patch1011:	libgcj-new-boehm-gc-ltconfig.patch
Patch1020:	gcc-libjava-datadir.patch

URL:		http://gcc.gnu.org/
BuildRoot:	%{_tmppath}/gcc-%{version}-root
Requires:	binutils >= 2.11.93.0.2-1mdk
BuildRequires:	binutils >= 2.11.93.0.2-1mdk
BuildRequires:	zlib-devel
Requires:	%{name}-cpp = %{version}-%{release}, make
%ifarch ia64
Requires:       glibc-devel >= 2.2.4
BuildRequires:  glibc-devel >= 2.2.4
%else
Requires:	glibc-devel
%endif
Requires(post):		info-install update-alternatives
Requires(postun):		update-alternatives
Requires(preun):		info-install
# Dadou - 2.96-0.46mdk - ExcludeArch: ppc because this GCC-3.0 snapshot is too
#                        buggy to be safely used on PPC. We currently use
#                        GCC-2.95.3 and will use GCC-3.0 when it will be ready
ExclusiveArch:	%{ix86} ia64
BuildRequires:	bison <= 1.35 , gettext, texinfo, elfutils-devel
%if %{system_compiler}
Obsoletes:	gcc%{branch}
Provides:	gcc%{branch} = %{version}-%{release}
%endif
%if %{build_pdf_doc}
BuildRequires: tetex-dvips, tetex-latex
%endif

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development
environment. You'll need this package in order to compile C/C++ code.

If you have multiple versions of GCC installed on your system, it is
preferred to type "gcc-$(gcc2-version)" (without double quotes) in
order to use the GNU C compiler version %{version}.

%package c++
Summary:	C++ support for gcc
Group:		Development/C++
%if %{system_compiler}
Obsoletes:	gcc%{branch}-c++
Provides:	gcc%{branch}-c++ = %{version}-%{release}
%endif
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-cpp = %{version}-%{release}, glibc-devel, make
Requires:	libstdc++2.10 = %{version}
Requires:	libstdc++2.10-devel = %{version}
Requires(post):		update-alternatives
Requires(postun):		update-alternatives

%description c++
This package adds C++ support to the GNU C compiler. It includes support
for most of the current C++ specification, including templates and
exception handling. It does include the static standard C++
library and C++ header files; the library for dynamically linking
programs is available separately.

If you have multiple versions of GCC installed on your system, it is
preferred to type "g++-$(gcc2-version)" (without double quotes) in
order to use the GNU C++ compiler version %{version}.

%package -n libstdc++2.10
Summary:	GNU C++ library
Group:		System/Libraries
Provides:   	libstdc++ = %{version}-%{release}
Obsoletes:	libstdc++

%description -n libstdc++2.10
The libstdc++ package contains a snapshot of the GCC Standard C++
Library v3, an ongoing project to implement the ISO 14882 Standard C++
library.

%ifarch %{ix86} alpha
%package -n libstdc++-compat
Summary:	GNU old c++ library
Group:		System/Libraries

%description -n libstdc++-compat
This is the GNU implementation of the standard C++ libraries This package
includes the old shared libraries necessary to run C++ applications.
%endif

%package -n libstdc++2.10-devel
Summary:	Header files and libraries for C++ development
Group:		Development/C++
Requires:	libstdc++2.10 = %{version}-%{release}
Obsoletes:  	libstdc++-devel
Provides:   	libstdc++-devel = %{version}-%{release}

%description -n libstdc++2.10-devel
This is the GNU implementation of the standard C++ libraries.  This
package includes the header files and libraries needed for C++
development. This includes SGI's implementation of the STL.

%if %{build_objc}
%package objc
Summary:	Objective C support for gcc
Group:		Development/Other
%if %{system_compiler}
Obsoletes:	gcc%{branch}-objc
Provides:	gcc%{branch}-objc = %{version}-%{release}
%endif
Requires:	%{name} = %{version}-%{release}, glibc-devel, make
Requires:	libobjc >= 2.96-0.59mdk
Provides:	libobjc
%endif

%if %{build_objc}
%description objc
This package adds Objective C support to the GNU C compiler. Objective
C is a object oriented derivative of the C language, mainly used on
systems running NeXTSTEP. This package does not include the standard
objective C object library.
%endif

%if %{build_fortran}
%package g77
Summary:	Fortran 77 support for gcc
Group:		Development/Other
%if %{system_compiler}
Obsoletes:	gcc%{branch}-g77
Provides:	gcc%{branch}-g77 = %{version}-%{release}
%endif
Requires:	%{name} = %{version}-%{release}, glibc-devel, make
%endif

%if %{build_fortran}
%description g77
This package adds support for compiling Fortran 77 programs with the GNU
compiler.

If you have multiple versions of GCC installed on your system, it is
preferred to type "g77-$(gcc2-version)" (without double quotes) in
order to use the GNU Fortran 77 compiler version %{version}.
%endif

%if %{build_java}
%package java
Summary:	Java support for gcc
Group:		Development/Java
%if %{system_compiler}
Obsoletes:	gcc%{branch}-java
Provides:	gcc%{branch}-java = %{version}-%{release}
%endif
Requires:	%{name} = %{version}-%{release}
Requires:	libgcj = %{version}-%{release}
Requires:	libgcj-devel = %{version}-%{release}
Requires(post):		update-alternatives

%description java
This package adds experimental support for compiling Java(tm) programs and
bytecode into native code. To use this you will also need the gcc-libgcj
package.

If you have multiple versions of GCC installed on your system, it is
preferred to type "gcj-$(gcc2-version)" (without double quotes) in
order to use the GNU Java compiler version %{version}.
%endif

%if %{build_java}
%package -n gcj-tools
Summary:	Java related tools from gcc %{version}
Group:		Development/Java
Provides:	gcj = %{version}-%{old_libgcj_release}
Obsoletes:	gcj
Requires:	libgcj2.96 >= %{version}
Requires:	libgcj2.96-devel >= %{version}

%description -n gcj-tools
This package includes Java related tools built from gcc %{version}:

   * gij: a Java ByteCode Interpreter
   * gcjh: generating C++ header files corresponding to ``.class'' files
   * jcf-dump: printing out useful information from a ``.class'' file
   * jv-scan: printing some useful information from a ``.java'' file
%endif

%if %{build_java}
%package -n libgcj2.96
Summary:	Java runtime library for gcc
Group:		System/Libraries
Epoch:		1
Provides:	libgcj = %{version}-%{old_libgcj_release}
Provides:	libgcj = %{version}-%{release}
Obsoletes:	libgcj

%description -n libgcj2.96
The Java runtime utility. You will need this package to run your Java
programs compiled using the gcc Java compiler (gcj).
%endif

%if %{build_java}
%package -n libgcj2.96-devel
Summary:	Libraries for Java development using gcc
Group:		Development/C
Epoch:		1
Requires:	zip >= 2.1
Requires:	zlib-devel
Requires:	libgcj2.96 = %{version}
Provides:	libgcj-devel = %{version}-%{old_libgcj_release}
Provides:	libgcj-devel = %{version}-%{release}
Obsoletes:	libgcj-devel

%description -n libgcj2.96-devel
The Java static libraries and C header files. You will need this
package to compile your Java programs using the gcc Java compiler (gcj).
%endif

%package cpp
Summary:	The C Preprocessor
Group:		Development/C
%if %{system_compiler}
Obsoletes:	gcc%{branch}-cpp
Provides:	gcc%{branch}-cpp = %{version}-%{release}
%endif
Requires(post):		info-install
Requires(post):		update-alternatives

%description cpp
The C preprocessor is a 'macro processor' which is used automatically
by the C compiler to transform your program before actual
compilation. It is called a macro processor because it allows
you to define 'macros,' which are abbreviations for longer
constructs.

The C preprocessor provides four separate facilities that you can use as
you see fit:

* Inclusion of header files. These are files of declarations that can be
  substituted into your program.
* Macro expansion. You can define 'macros,' which are abbreviations for 
  arbitrary fragments of C code, and then the C preprocessor will replace
  the macros with their definitions throughout the program.
* Conditional compilation. Using special preprocessing directives,
  you can include or exclude parts of the program according to various
  conditions.
* Line control. If you use a program to combine or rearrange source files
  into an intermediate file which is then compiled, you can use line
  control to inform the compiler about where each source line originated.

You should install this package if you are a programmer who is searching for
such a macro processor.

%package colorgcc
Summary:	Gcc output colorizer
Group:		Development/Other
%if %{system_compiler}
Obsoletes:	gcc%{branch}-colorgcc
Provides:	gcc%{branch}-colorgcc = %{version}-%{release}
%endif
Requires(post):		%{name}, %{name}-c++
Requires(post):		update-alternatives
Requires:	perl

%description colorgcc
GCC output colorizer.

%if %{build_doc}
%package doc
Summary:	Gcc documentation
Group:		Development/Other
Requires(post):		info-install
Requires(preun):		info-install
%if %{system_compiler}
Obsoletes:	gcc%{branch}-doc
Provides:	gcc%{branch}-doc = %{version}-%{release}
%endif
%endif

%if %{build_doc}
%description doc
GCC is a compiler suite aimed at integrating all the optimizations and
features necessary for a high-performance and stable development
environment. This package contains the compiler documentation in INFO
pages.
%endif

%if %{build_pdf_doc}
%package doc-pdf
Summary:	GCC documentation
Group:		Development/Other
%if %{system_compiler}
Obsoletes:	gcc%{branch}-doc-pdf
Provides:	gcc%{branch}-doc-pdf = %{version}-%{release}
%endif
%endif

%if %{build_pdf_doc}
%description doc-pdf
GCC is a compiler suite aimed at integrating all the optimizations and
features necessary for a high-performance and stable development
environment. This package contains the compiler printable
documentation in PDF.
%endif

%prep
%setup -q -n gcc-%{oversion} -a 4
# Upgrading to CVS
%patch0 -p1

%patch10 -p0 -b .sparc
%patch11 -p0 -b .sparc1
%patch12 -p0 -b .sparc2
%patch13 -p0 -b .sparc3
%patch14 -p0 -b .sparc4
%patch15 -p0 -b .sparc5
%patch16 -p0 -b .sparc6
%patch18 -p0 -b .jword
%patch19 -p0 -b .memcpy
%patch20 -p0 -b .sparcv9
%patch4 -p0 -b .typedef
%patch5 -p0 -b .trigraph
%patch6 -p0 -b .incompl
%patch8 -p0 -b .wnoerror
%patch9 -p0 -b .stringcrash
%patch21 -p0 -b .stmtexpr
%ifarch sparc
%patch22 -p0 -b .sparc32hack
if [ ! -f /usr/lib64/crt1.o ]; then
%patch23 -p0 -b .sparc32hack2
fi
%endif
#%patch25 -p0 -b .hack
%patch28 -p0 -b .loop
%patch29 -p0 -b .addressof
%patch31 -p0 -b .regmoveasm
%patch33 -p0 -b .cpplib
%patch35 -p0 -b .cpp0
%patch36 -p0 -b .canoncond
%patch37 -p0 -b .bogussubreg
%patch38 -p0 -b .cpii
%patch39 -p0 -b .subreggcse
%patch40 -p0 -b .subregbytegcse
%patch41 -p0 -b .combinecomparison
%patch42 -p0 -b .loopnoopt
%patch43 -p0 -b .loopunroll
%patch44 -p0 -b .looptest1
%patch45 -p0 -b .looptest2
%patch46 -p0 -b .loopscanloop
%patch48 -p0 -b .ashlsilea
%patch49 -p0 -b .lea
%patch50 -p0 -b .lowparttest
%patch51 -p0 -b .loopnoopt2
%patch52 -p0 -b .i386sib
%patch53 -p0 -b .cppwarn
%patch54 -p0 -b .wintt
%patch55 -p0 -b .fmtchk
%patch56 -p0 -b .strftime
%patch57 -p0 -b .xopen
%patch58 -p0 -b .c99std
%patch59 -p0 -b .iso-not-ansi
%patch60 -p0 -b .sibcall
%patch61 -p0 -b .ostest
%patch62 -p0 -b .java-misc
%patch63 -p0 -b .java-bytecode
%patch64 -p0 -b .java-pg
# These two are buggy
#%patch65 -p0 -b .cmtable
#%patch66 -p0 -b .relational
%patch67 -p0 -b .finclude
%patch68 -p0 -b .unroll
%patch69 -p0 -b .i386-strops
%patch70 -p0 -b .simplify-rela
%patch71 -p0 -b .alias
%patch72 -p0 -b .jsm1
%patch73 -p0 -b .jsm2
%patch74 -p0 -b .jsm3
%patch75 -p0 -b .scanf
%patch76 -p0 -b .jsm4
%patch77 -p0 -b .jsm5
%patch78 -p0 -b .jsm6
%patch79 -p0 -b .jsm7
%patch80 -p0 -b .jsm8
%patch81 -p0 -b .loop-hack
%patch82 -p0 -b .cpp-warnpaste
%patch83 -p0 -b .float-condmove
%patch84 -p0 -b .i386-call
%patch85 -p0 -b .i386-call2
%patch86 -p0 -b .i386-call-test
%patch87 -p0 -b .i386-arith
%patch88 -p0 -b .i386-ge_geu
%patch89 -p0 -b .i386-gotoff
%patch90 -p0 -b .java-catchup
%patch91 -p0 -b .java-no-super-layout
%patch92 -p0 -b .make-extraction
%patch93 -p0 -b .segv1
%patch94 -p0 -b .segv2
%patch95 -p0 -b .copy-leaf-remap
%patch96 -p0 -b .wchar-const
%patch97 -p0 -b .libio
%patch98 -p0 -b .alpha-tune
%patch99 -p0 -b .alpha-unaligned
%patch100 -p0 -b .cpp-warnpaste2
%patch101 -p0 -b .loop-giv
%patch102 -p0 -b .real-value
%patch103 -p0 -b .sparc-const-pool
%patch104 -p0 -b .sparc64-timode
%patch105 -p0 -b .callersave-segv
%patch106 -p0 -b .libio-printf_fp
%patch107 -p0 -b .pt-enum
%patch108 -p0 -b .sparc-pic
%patch109 -p0 -b .subreg-byte-expmed
%patch110 -p0 -b .test-991206-1
%patch111 -p0 -b .alpha-mi-thunk
%patch112 -p0 -b .c++-pmf
%patch113 -p0 -b .f77-fdebug
%patch114 -p0 -b .libio-endl
%patch115 -p0 -b .i386-compare-test
%patch116 -p0 -b .sparc-may-trap
%patch117 -p0 -b .sparc-mi-thunk
%patch118 -p0 -b .c++-inline16-test
%patch119 -p0 -b .c++-named-return-value
%patch120 -p0 -b .c++-walk-tree
%patch121 -p0 -b .i386-reload-test
%patch122 -p0 -b .i386-reload
%patch123 -p0 -b .sibcall-unchanging
%patch124 -p0 -b .segv3
%patch125 -p0 -b .c++-crash24
%patch126 -p0 -b .do-store-flag
%patch127 -p0 -b .i386-address-cost
%patch128 -p0 -b .i386-arith2
%patch129 -p0 -b .i386-constraint-N
%patch130 -p0 -b .incomplete-aggregate-alias
%patch131 -p0 -b .sibcall-eh2
%patch132 -p0 -b .cpp-assert-crash
%patch133 -p0 -b .c++-undefined-method
%patch134 -p0 -b .sparc-4096
%patch135 -p0 -b .sparc64-reload-test
%patch136 -p0 -b .sparc64-reload2
%patch137 -p0 -b .subreg-byte-operand-subword
%patch139 -p0 -b .c++-static-class
%patch140 -p0 -b .c++-testset1
%patch141 -p0 -b .c++-testset2
%patch142 -p0 -b .place-field
%patch143 -p0 -b .sparc-output-formatting
%patch144 -p0 -b .sparc64-mi-thunk
%patch145 -p0 -b .sparc64-namedret
%patch146 -p0 -b .sparc64-nested-fn
%patch147 -p0 -b .c++-ice
%patch148 -p0 -b .alpha-fold-const
%patch149 -p0 -b .alpha-recog
%patch150 -p0 -b .c++-pointer-to-member-test
%patch151 -p0 -b .c++-sizetype
%patch152 -p0 -b .cpp-64k
%patch153 -p0 -b .cpp-empty-header
%patch154 -p0 -b .i386-regelim
%patch155 -p0 -b .sparc-builtin-setjmp
%patch156 -p0 -b .test-loop-7
%patch157 -p0 -b .c++-dump-expr
%patch158 -p0 -b .c++-inline-cmp
%patch159 -p0 -b .c++-inline-return
%patch160 -p0 -b .c++-label-scope
%patch161 -p0 -b .c++-ptm
%patch162 -p0 -b .c++-qual-error
%patch163 -p0 -b .const-fold
%patch164 -p0 -b .cpp-error-directive
%patch165 -p0 -b .i386-truncxfsf
%patch166 -p0 -b .integrate-clobber
%patch167 -p0 -b .libf2c-mkstemp
%patch168 -p0 -b .local-alloc
%patch169 -p0 -b .loop-hoistmem
%patch170 -p0 -b .sibcall-const
%patch171 -p0 -b .sibcall-emit-queue
%patch172 -p0 -b .unroll-iterations
%patch173 -p0 -b .volatile-local-var
%patch174 -p0 -b .c++-sizetype2
%patch175 -p0 -b .error-diagnostic
%patch176 -p0 -b .aggregate-mode
%patch177 -p0 -b .c++-addressof
%patch178 -p0 -b .aggregate-mode2
%patch179 -p0 -b .c++-addressof2
%patch180 -p0 -b .c++-inline-cmp2.patch
%patch181 -p0 -b .cpp-fno-operator-names
%patch182 -p0 -b .c++-ggc-input
%patch183 -p0 -b .alpha-unaligned2
%patch184 -p0 -b .alpha-ze_and_ne
%patch185 -p0 -b .c++-wchar_t
%patch186 -p0 -b .cpp-arg-loop
%patch187 -p0 -b .cpp-fno-operator-names2
%patch188 -p0 -b .cpp-g3
%patch189 -p0 -b .fshort-wchar
%patch190 -p0 -b .max-strlen
%patch191 -p0 -b .stabs
%patch192 -p0 -b .subreg-byte-gcse2
%patch193 -p0 -b .tradcpp-MD
%patch194 -p0 -b .alpha-expand-block-move
%patch195 -p0 -b .c++-decl-needed
%patch196 -p0 -b .c++-nomods_initdcl0
%patch197 -p0 -b .cpp-MD
%patch198 -p0 -b .fixup-var-refs
%patch199 -p0 -b .frame-related
%patch200 -p0 -b .i386-cmpqi
%patch201 -p0 -b .i386-const-call-address
%patch202 -p0 -b .i386-fcmov
%patch203 -p0 -b .i386-sar
%patch204 -p0 -b .c++-extern-c
%patch205 -p0 -b .c++-inline-static
%patch206 -p0 -b .c++-inline-static2
%patch207 -p0 -b .cpp-M-include
%patch208 -p0 -b .integrate-compare
# Put in cpp snapshot from 20010126
rm -rf gcc/testsuite/gcc.dg/cpp
tar x --bzip2 -f %{SOURCE209}
%patch209 -p0 -b .cpp-20010126
%patch210 -p0 -b .objc-cpp-lineno
%patch211 -p0 -b .cpp-paste-avoid
%patch212 -p0 -b .cpp-paste-avoid2
# Bug fixing continues
%patch213 -p0 -b .c++-inline-modify_expr
%patch214 -p0 -b .i386-testqi_1
%patch215 -p0 -b .c++-anon-union
%patch216 -p0 -b .extract_bit_field
%patch217 -p0 -b .c++-overload-warn
%patch218 -p0 -b .cpp-implicit-extern-c
%patch219 -p0 -b .cpp-paste-avoid3
%patch220 -p0 -b .packed-enum-bitfield
%patch221 -p0 -b .variable-size
%ifarch ia64
%patch222 -p0 -b .ia64
%patch223 -p0 -b .ia64-errata
%endif

%patch224 -p0 -b .cpp-defined-diag
%patch225 -p0 -b .cpp-paste-avoid4
%patch226 -p0 -b .dwarf2out-ice
%patch227 -p0 -b .g++.jason-2371
%patch228 -p0 -b .lex-line
%patch229 -p0 -b .alpha-unaligned3
tar x --bzip2 -f %{SOURCE230}
%patch230 -p0 -b .consistency
%patch231 -p0 -b .nested-parm
%patch232 -p0 -b .alpha-reload
%patch233 -p0 -b .alpha-shift
%patch234 -p0 -b .c++-init-copy-aggr
%patch235 -p0 -b .c++-inline-loop
%patch236 -p0 -b .c++-lookup
%patch237 -p0 -b .c++-taking-address-error
%patch238 -p0 -b .objc-gc
%patch239 -p0 -b .objc-test
%patch240 -p0 -b .reload-hardreg-free
%patch241 -p0 -b .cpp-20010222
%patch242 -p0 -b .expr-safety
%patch243 -p0 -b .debug-static-local
%patch244 -p0 -b .fixup-var-refs2
%patch245 -p0 -b .fold-const-div
%patch246 -p0 -b .g77-unused
%ifarch ia64
%patch247 -p0 -b .ia64-flushrs
%patch248 -p0 -b .ia64-syscall-linkage
%endif
%patch249 -p0 -b .recog-addressof
%patch250 -p0 -b .cpp-20010309
%patch251 -p0 -b .cant-combine
%patch252 -p0 -b .i386-crtendS
%patch253 -p0 -b .reg-stack-clobber
%patch254 -p0 -b .reg-stack
%patch255 -p0 -b .store-expr
%patch256 -p0 -b .target-expr
%patch257 -p0 -b .c++-anonaggr-copy
%patch258 -p0 -b .c++-asmspec
%patch259 -p0 -b .c++-static-local
%patch260 -p0 -b .f77-line
%patch261 -p0 -b .libstdc++-getline
%patch262 -p0 -b .no-new-abi
%patch263 -p0 -b .regrename
%patch264 -p0 -b .subreg-byte-gcse3
%patch265 -p0 -b .wshadow-doc
%patch266 -p0 -b .c++-D__EXCEPTIONS
%patch267 -p0 -b .c++-throttle-inline
%patch268 -p0 -b .fold-pointer-cmp
%patch269 -p0 -b .ifcvt-strict-low-part
%patch270 -p0 -b .gcse-reg-equiv
%patch271 -p0 -b .null-pointer-check
%patch272 -p0 -b .local-inline
%patch273 -p0 -b .cpp-Wcomment
%patch274 -p0 -b .cselib-mode
%patch275 -p0 -b .dwarf2-O0-crash
%patch276 -p0 -b .dwarf2out-splice-child
%patch277 -p0 -b .i386-movcc
%patch278 -p0 -b .ia64-xdata
%patch279 -p0 -b .subregbyte-hard-regno
%patch280 -p0 -b .tradtradcpp0
%patch281 -p0 -b .flow-autoinc
%patch282 -p0 -b .ia64-constconst
%patch283 -p0 -b .ia64-G
%patch284 -p0 -b .integrate-error
%patch285 -p0 -b .MD-nodot
%patch286 -p0 -b .store-constructor-field
%ifarch ia64
%patch287 -p0 -b .ia64-expect
%patch288 -p0 -b .ia64-loc79
# Add -mb-step automatically -- this will go away when production
# hardware is available.
%patch289 -p0 -b .ia64-bstep
%endif
%patch290 -p0 -b .c++-templ-arg
%patch291 -p0 -b .frame-state-for-compat
%patch292 -p0 -b .sibcall-catch
%patch293 -p0 -b .tradcpp-define
%patch294 -p0 -b .c++-inline-method
%patch295 -p0 -b .gcse-trapping
%patch296 -p0 -b .nested-expr-stmt
%patch297 -p0 -b .__NO_INLINE__
%patch298 -p0 -b .bogus-inline
%patch299 -p0 -b .c++-defarg
%patch300 -p0 -b .c++-instantiate
%patch301 -p0 -b .c++-static-ctordtor
%patch302 -p0 -b .c++-templ-arg2
%patch303 -p0 -b .c++-ucs
%patch304 -p0 -b .fsyntax-only
%patch305 -p0 -b .g77-unsigned-char
%patch306 -p0 -b .hash-ident
#%patch307 -p0 -b .jump-threading
%patch308 -p0 -b .regmove-unchanging
%ifarch ia64
%patch309 -p0 -b .ia64-complex-float
%patch310 -p0 -b .ia64-movcc-fail
%patch311 -p0 -b .ia64-stop-bit
%endif
%patch312 -p0 -b .c++-friend
%patch313 -p0 -b .i386-stack-adjust
%ifnarch alpha
%patch314 -p0 -b .SHF_MERGE
%endif
%patch315 -p0 -b .dwarf2-filenames
%patch316 -p0 -b .k6-loop
%patch317 -p0 -b .libobjc-3.0
%patch318 -p0 -b .texinfo-texconfig
%patch319 -p0 -b .c++-complext
%patch320 -p0 -b .c++-conv-cv-ptr
%patch321 -p0 -b .c++-sstream-warn
%patch322 -p0 -b .f77-ffixed
%patch323 -p0 -b .invalid-stabs
%patch324 -p0 -b .libio-test
%patch325 -p0 -b .alpha-function-sections
%patch326 -p0 -b .alpha-vtable-gc
%patch327 -p0 -b .c++-anontypename
%patch328 -p0 -b .c++-array-cast
%patch329 -p0 -b .c++-colonequal
%patch330 -p0 -b .c++-cond-ovl
%patch331 -p0 -b .c++-weak-address
%patch332 -p0 -b .libio-input-float
%patch333 -p0 -b .subreg-byte-stabs
%patch334 -p0 -b .c++-array-side-effects
%patch335 -p0 -b .cpp-memleak
%patch336 -p0 -b .c++-template-throw
%patch337 -p0 -b .c++-tsubst-friend-class
%patch338 -p0 -b .dwarf2-debug-line
%patch339 -p0 -b .ifcvt-eh
%patch340 -p0 -b .ia64-vararg
%patch341 -p0 -b .gcse-hoist
%ifarch ia64
%patch342 -p0 -b .ia64-eh
%endif
%patch343 -p0 -b .libio-stdstream-offset
%patch344 -p0 -b .objc-class-ref
%patch345 -p0 -b .tail-recurse
%patch346 -p0 -b .c++-sstream-seek
%patch347 -p0 -b .loop-combine-givs
%patch348 -p0 -b .alpha-asm-input
%patch349 -p0 -b .c++-anon-union2
%patch350 -p0 -b .c++-inline-sizeof-char
%patch351 -p0 -b .cpp-run-directive
%patch352 -p0 -b .reload-optional
%patch353 -p0 -b .fde-merge-compat
%patch354 -p0 -b .flow-setjmp
%patch355 -p0 -b .pure-reload
%patch356 -p0 -b .sparc-float
%patch357 -p0 -b .sparc-movdf
%patch358 -p0 -b .c++-member-init
%patch359 -p0 -b .autoconf-2.52
%patch360 -p0 -b .makej
%ifarch ia64
%patch361 -p0 -b .ia64-bitfield-return
%patch362 -p0 -b .ia64-NaT
%endif
%ifarch sparc sparc64
%patch363 -p0 -b .sparc-libcall
%endif
#%patch364 -p0 -b .c++-preexpand-calls
%patch365 -p0 -b .libio-stdstreams-vptr
%patch366 -p0 -b .sparc-return
%patch367 -p0 -b .sparc64-nonzero-bits
%patch368 -p0 -b .below-sp
%patch369 -p0 -b .c++-setup-vtbl-ptr
%patch370 -p0 -b .reload-ofp
%patch371 -p0 -b .bitop-shorten
%patch372 -p0 -b .c++-ptrintsum
%patch373 -p0 -b .i386-fxch
%patch374 -p0 -b .i386-regparm-struct
%patch375 -p0 -b .ia64-encode-section-info
%patch376 -p0 -b .attr-visibility
%patch377 -p0 -b .store_field-expand_and
%patch378 -p0 -b .c++-array-ref
%patch379 -p0 -b .c++-flat-initializer
%patch380 -p0 -b .c++-static-member
%patch381 -p0 -b .i386-reg-stack-check
%patch382 -p0 -b .i386-zero-size
%patch383 -p0 -b .loop-check_dbra_loop
%patch384 -p0 -b .pedwarn-string-length
%patch385 -p0 -b .simplify-check-overflow
%patch386 -p0 -b .UDA-option-order
%patch387 -p0 -b .c++-pt-using
%patch388 -p0 -b .c++-pt-using2
%patch389 -p0 -b .attr-visibility2
%patch390 -p0 -b .libstdc++-libc-interface
%patch391 -p0 -b .attr-visibility3
%ifarch ia64
%patch392 -p0 -b .ia64-thread-safe-eh
%endif
%patch393 -p0 -b .merge_blocks_nomove
%patch394 -p0 -b .attr-visibility4
%ifarch ia64
%patch395 -p0 -b .unaligned-const
%endif
%patch396 -p0 -b .i386-piclabel
%patch397 -p0 -b .2.96-parallel
%patch398 -p0 -b .i386-andhi
%patch399 -p0 -b .mem-scratch
%patch401 -p0 -b .sparc-tfdi
%patch402 -p0 -b .c++-gc-named-label-list
%patch403 -p0 -b .cpp-include-dir
%patch404 -p0 -b .c++-compound-literal
%patch405 -p0 -b .c++-eh-spec-incomplete
%patch406 -p0 -b .fde-merge-compat-2
%patch407 -p0 -b .strict-alias-optimization
%patch408 -p0 -b .cpp-MD-2

%if %{build_pdf_doc}
%patch503 -p1 -b .texold
%patch504 -p1 -b .texiold
%endif

%patch600 -p1 -b .unroll-iterations2
%patch601 -p1 -b .unroll-iterations3
%patch602 -p1 -b .alpha-baddr
%patch603 -p1 -b .c++-enum-fix
%patch604 -p1 -b .program-transform
%patch605 -p1 -b .pr4294

%if %{build_java}
%setup -q -n gcc-%{oversion} -T -D -a 2
cd libgcj
%patch1001 -p1 -b .makej
%patch1002 -p1 -b .nomulti
%patch1003 -p1 -b .compile
%patch1004 -p1 -b .awtcolor
%patch1005 -p1 -b .sigaction
%patch1006 -p0 -b .boehmgc
%patch1007 -p0 -b .libdeps
%patch1008 -p0 -b .boehmgc-dyn_load
%patch1009 -p1 -b .nozlib
%patch1010 -p0 -b .new-boehm-gc
rm -rf zlib
# Replace the old boehm-gc with the one from gcc-3.1
mv boehm-gc old_boehm-gc
tar x --bzip2 -f %{SOURCE3}
%patch1011 -p0 -b .new-boehm-gc-ltconfig
cd ..
%patch1020 -p1 -b .libjava-datadir
%endif

perl -pi -e 's/\(experimental\)/\(Mandrake Linux %{mdk_version} %{gcc_version}-%{gcc_release}\)/' gcc/version.c gcc/f/version.c
perl -pi -e 's/#define GCCBUGURL.*$/#define GCCBUGURL "<URL:https:\/\/qa.mandrakesoft.com\/>"/' gcc/system.h

# Debian patches
%patch501 -p1
%patch502 -p1

cd colorgcc-%{color_gcc_version}
# colorgcc patch
%patch500 -p2 -b .mdkconf
perl -pi -e 's|GCC_VERSION|%{version}|' colorgcc*
cd ..

# compat libstdc++ binaries
mkdir compat
tar xjf %{SOURCE5} -C compat

%build
pushd texinfo && autoconf &&  popd

# (gb) FIXME: q&d hack: don't compile libchill
mv ./libchill ./libchill.disabled

cd compat
# Munge binary compatibility C++ libraries, so that they use
# frame info registry and __frame_state_for from glibc
# instead of defining their own (by changing those symbols
# in .dynsym to SHN_UNDEF).
# FIXME: Maybe it should munge .gnu.version section too
# so that those symbols are @GLIBC_2.0, not non-versioned.
gcc -D_FILE_OFFSET_BITS=64 -O2 -o symtabedit symtabedit.c -lelf
for i in i386/libstdc++* sparc/libstdc++*; do
  case "$i" in
  *.dummy) ;; # These are just dummy libs with DT_NEEDED entry
  sparc/*.2.8.0) ;; # This one used libc frame info stuff already
  *) ./symtabedit $i || exit ;;
  esac
done
cd ..

rm -fr obj-%{gcc_target_platform}
mkdir obj-%{gcc_target_platform}
cd obj-%{gcc_target_platform}

CC=gcc
OPT_FLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-fno-rtti//g' -e 's/-fno-exceptions//g'`
%ifarch ia64
# Add -mb-step automatically -- this will go away when production
# hardware is available.
OPT_FLAGS="$OPT_FLAGS -mb-step"
%endif
%if %{build_debug}
OPT_FLAGS=`echo "$OPT_FLAGS -g" | sed -e "s/-fomit-frame-pointer//g"`
%endif
LANGUAGES="c,c++"
%if %{build_fortran}
LANGUAGES="$LANGUAGES,f77"
%endif
%if %{build_objc}
LANGUAGES="$LANGUAGES,objc"
%endif
%if %{build_java}
LANGUAGES="$LANGUAGES,java"
%endif
PROGRAM_SUFFIX=""
%if !%{system_compiler}
PROGRAM_SUFFIX="--program-suffix=%{program_suffix}"
%endif
CC="$CC" CFLAGS="$OPT_FLAGS" CXXFLAGS="$OPT_FLAGS" XCFLAGS="$OPT_FLAGS" \
	TCFLAGS="$OPT_FLAGS" \
	../configure --prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} --datadir=%{gcc_datadir} \
	--enable-shared --enable-threads=posix --enable-haifa --disable-checking \
	--enable-languages="$LANGUAGES" $PROGRAM_SUFFIX \
	--host=%{gcc_target_platform}
touch ../gcc/c-gperf.h
%make bootstrap-lean

# Build libg2c.a with PIC enabled and name the result 'libg2c-pic.a'
%if %{build_fortran}
(cd %{gcc_target_platform};
rm -rf libf2c-pic
cp -a libf2c libf2c-pic
%make -C libf2c-pic clean
%make -C libf2c-pic LIBG2C=libg2c-pic.a CFLAGS="$OPT_FLAGS -fPIC -DPIC"
)
%endif

# run the tests.
# rpm seems to terminate when make -k check fails.
# %make -k check || true

# Make protoize
make -C gcc CC="./xgcc -B ./ -O2" proto

# Copy various doc files here and there
cd ..
mkdir -p rpm.doc/libstdc++ rpm.doc/g77 rpm.doc/objc

(cd libio; for i in ChangeLog*; do
	cp -p $i ../rpm.doc/libstdc++/$i.libio
done)
(cd libstdc++; for i in ChangeLog*; do
	cp -p $i ../rpm.doc/libstdc++/$i.libstdc++
done)
(cd gcc/f; for i in ChangeLog*; do
	cp -p $i ../../rpm.doc/g77/$i.f
done)
(cd libf2c; for i in ChangeLog*; do
	cp -p $i ../rpm.doc/g77/$i.libf2c
done)
(cd gcc/objc; for i in README*; do
	cp -p $i ../../rpm.doc/objc/$i.objc
done)
(cd libobjc; for i in README*; do
	cp -p $i ../rpm.doc/objc/$i.libobjc
done)

%if %{build_java}
GCCDIR=`pwd`/obj-%{gcc_target_platform}/gcc
cd libgcj
rm -fr obj-%{_target_platform}
mkdir obj-%{_target_platform} bin
cat > bin/gcc <<EOF
#!/bin/sh
exec $GCCDIR/xgcc -B $GCCDIR/ "\$@"
EOF
cat > bin/g++ <<EOF
#!/bin/sh
exec $GCCDIR/g++ -B $GCCDIR/ "\$@"
EOF
cat > bin/gcj <<EOF
#!/bin/sh
exec $GCCDIR/gcj -B $GCCDIR/ "\$@"
EOF
chmod +x bin/gcc bin/g++ bin/gcj
ln -f $GCCDIR/gcjh bin/gcjh
ln -f bin/gcc bin/%{gcc_target_platform}-gcc
ln -f bin/g++ bin/%{gcc_target_platform}-g++
ln -f bin/gcj bin/%{gcc_target_platform}-gcj
ln -f bin/gcjh bin/%{gcc_target_platform}-gcjh
export PATH=`pwd`/bin:$PATH
CC=`pwd`/bin/gcc
CXX=`pwd`/bin/g++
GCJ=`pwd`/bin/gcj
cd obj-%{_target_platform}
CC="$CC" CXX="$CXX" GCJ="$GCJ" CFLAGS="$OPT_FLAGS" \
	../configure --prefix=%{_prefix} --datadir=%{gcc_datadir} \
	--enable-shared --enable-threads=posix --host=%{_target_platform} \
	--with-system-zlib
%make
cd ..
for i in boehm-gc/ChangeLog libjava/ChangeLog libffi/ChangeLog; do
  cp -p $i ../ChangeLog.`echo $i | sed 's|/.*||'`
done
cp -p libffi/LICENSE ../LICENSE.libffi
cp -p libffi/README ../README.libffi
cp -p libffi/LICENSE ../LICENSE.libffi
cp -p libffi/README ../README.libffi
%endif

# [ghibo] - build printable documentation
%if %{build_pdf_doc}
(cd gcc
texi2dvi -p -t @afourpaper -t @finalout gcc.texi
texi2dvi -p -t @afourpaper -t @finalout cpp.texi
texi2dvi -p -t @afourpaper -t @finalout f/g77.texi)
%endif

%install
rm -rf $RPM_BUILD_ROOT

# Create some directories, just to make sure (e.g. ColorGCC)
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}
mkdir -p $RPM_BUILD_ROOT%{_infodir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}

# ColorGCC stuff
(cd colorgcc-%{color_gcc_version};
  install -m 755 colorgcc $RPM_BUILD_ROOT%{_bindir}/colorgcc-%{version}
  install -m 644 colorgccrc $RPM_BUILD_ROOT%{_sysconfdir}
  for i in COPYING CREDITS ChangeLog; do
    [ ! -f ../$i.colorgcc ] && mv -f $i ../$i.colorgcc
  done
)

(cd obj-%{gcc_target_platform};
  make prefix=$RPM_BUILD_ROOT%{_prefix} \
       mandir=$RPM_BUILD_ROOT%{_mandir} \
       infodir=$RPM_BUILD_ROOT%{_infodir} \
       datadir=$RPM_BUILD_ROOT%{gcc_datadir} \
       install
  
  # Install libg2c-pic.a
  %if %{build_fortran}
  (cd %{gcc_target_platform};
    make -C libf2c-pic LIBG2C=libg2c-pic.a \
         prefix=$RPM_BUILD_ROOT%{_prefix} \
         mandir=$RPM_BUILD_ROOT%{_mandir} \
         infodir=$RPM_BUILD_ROOT%{_infodir} \
         datadir=$RPM_BUILD_ROOT%{gcc_datadir} \
         install)
  %endif
)

FULLVER=`$RPM_BUILD_ROOT%{_prefix}/bin/%{gcc_target_platform}-gcc%{program_suffix} --version | cut -d' ' -f1`
FULLPATH=$(dirname $RPM_BUILD_ROOT%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/cc1)

if [ "%{gcc_target_platform}" != "%{_target_platform}" ]; then
  mv -f $RPM_BUILD_ROOT%{_prefix}/bin/%{gcc_target_platform}-gcc $RPM_BUILD_ROOT%{_prefix}/bin/%{_target_platform}-gcc
fi

file $RPM_BUILD_ROOT/%{_prefix}/bin/* | grep ELF | cut -d':' -f1 | xargs strip || :
strip $FULLPATH/{cc1,cc1plus,cpp0,tradcpp0}
%if %{build_objc}
strip $FULLPATH/cc1obj
%endif
%if %{build_fortran}
strip $FULLPATH/f771
%endif
%if %{build_java}
strip $FULLPATH/{jc1,jvgenmain}
%endif

# Create /usr/bin/gcc2-version that contains the full version of gcc
cat >$RPM_BUILD_ROOT%{_bindir}/gcc2-version <<EOF
#!/bin/sh
echo "$FULLVER"
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/gcc2-version

# fix some things
ln -sf gcc $RPM_BUILD_ROOT%{_prefix}/bin/cc
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
#gzip -9 $RPM_BUILD_ROOT%{_infodir}/*.info*

# Fix program names
# (gb) For each primary program in every package, I want it to be
# named <program>-<version>
(cd $RPM_BUILD_ROOT%{_bindir}; for file in gcc g++ gcj g77; do
  file_version="${file}-%{version}"
  if [ -x "$file" -a "(" ! -x "$file_version" -o -L "$file_version" ")" ]; then
    cp -f $file $file_version
    rm -f $file
    ln -s $file_version $file
  fi
done)

(
cd $FULLPATH
rm -f libstdc++.so libstdc++.a
ln -sf ../../../libstdc++-libc6*-2.so.3 libstdc++.so
ln -sf ../../../libstdc++-libc6*-2.a.3 libstdc++.a
%if %{build_objc}
mv -f libobjc.so.1* $RPM_BUILD_ROOT%{_prefix}/lib
ln -sf ../../../libobjc.so.1* .
%endif
STDCV=`echo $RPM_BUILD_ROOT%{_prefix}/lib/libstdc++-libc6*-2.so.3 | sed 's/^.*\(libc6.*-2\).*$/\1/'`
)

# install compat libstdc++ binaries
LIB_ARCH=`echo %{_target_cpu} | sed 's/i.86/i386/'`
[ -d compat/$LIB_ARCH ] && {
install -m 755 compat/$LIB_ARCH/* $RPM_BUILD_ROOT%{_libdir}/
}

%if %{build_java}
# Now install libgcj
(cd libgcj;
  export PATH=`pwd`/bin:$PATH
  CC=`pwd`/bin/gcc
  CXX=`pwd`/bin/g++
  GCJ=`pwd`/bin/gcj
  cd obj-%{_target_platform}
  make prefix=$RPM_BUILD_ROOT%{_prefix} datadir=$RPM_BUILD_ROOT%{gcc_datadir} install
  mv -f $RPM_BUILD_ROOT%{_libdir}/libgcj.spec $FULLPATH/libgcj.spec
  mv -f $RPM_BUILD_ROOT%{_libdir}/libgcj*.a $FULLPATH/
  mv -f $RPM_BUILD_ROOT%{_includedir}/j*.h $FULLPATH/include/
  mv -f $RPM_BUILD_ROOT%{_includedir}/{java,gnu,gcj} $FULLPATH/include/
  echo '.text' | gcc -shared -o $RPM_BUILD_ROOT%{_libdir}/libzgcj.so.0.0.0 \
    -Wl,--soname,libzgcj.so.0 -xassembler - -lz
  strip $RPM_BUILD_ROOT%{_libdir}/libzgcj.so.0.0.0
  ln -sf libzgcj.so.0.0.0 $RPM_BUILD_ROOT%{_libdir}/libzgcj.so.0
  (cd $FULLPATH;
    ln -sf ../../../libgcj.so.1.* libgcj.so
    ln -sf ../../../libgcjgc.so.1.* libgcjgc.so
  )
)
%endif

# Fix links to binaries
(cd $RPM_BUILD_ROOT%{_bindir};
  ln -sf colorgcc-%{version} colorg++-%{version}
  for file in cpp gcc g++ c++; do [ -x $file ] && mv $file "$file"-%{version}; done
  %if %{build_java}
  for file in gcjh jcf-dump jv-scan; do [ -x $file -a -n "%{program_suffix}" ] && mv $file "$file"-%{version}; done
  %endif
)

# Create an empty file with perms 0755
FakeAlternatives() {
  for file in ${1+"$@"}; do
    [ -e "$file" ] && (echo "ERROR: $file should not exist at this point!"; exit 1)
    rm -f $file
    touch $file
    chmod 0755 $file
  done
}

# (gb) 2.96-0.59mdk: /usr/bin/cpp is provided by update-alternatives
(cd $RPM_BUILD_ROOT%{_bindir}; [ -x cpp ] && cp -f cpp cpp-%{version}; rm -f cpp)
(cd $RPM_BUILD_ROOT%{_bindir}; FakeAlternatives cpp)
(mkdir -p $RPM_BUILD_ROOT/lib; cd $RPM_BUILD_ROOT/lib; ln -sf %{_bindir}/cpp cpp)

# (gb) 2.96-0.75mdk: /usr/bin/c++ is provided by update-alternatives
(cd $RPM_BUILD_ROOT%{_bindir}; [ -x c++ ] && cp -f c++ c++-%{version}; rm -f c++)
(cd $RPM_BUILD_ROOT%{_bindir}; FakeAlternatives c++)

# (gb) 2.96-0.59mdk: /usr/bin/{f77,g77} are provided by update-alternatives
(cd $RPM_BUILD_ROOT%{_bindir}; [ -x g77 ] && cp -f g77 g77-%{version}; rm -f g77 f77)
(cd $RPM_BUILD_ROOT%{_bindir}; FakeAlternatives g77 f77)

# (gb) 2.96-0.59mdk: /usr/bin/gcj is provided by update-alternatives
(cd $RPM_BUILD_ROOT%{_bindir}; [ -x gcj ] && cp -f gcj gcj-%{version}; rm -f gcj)
(cd $RPM_BUILD_ROOT%{_bindir}; FakeAlternatives gcj)

# Fix cpp manpage name
(cd $RPM_BUILD_ROOT%{_mandir}/man1;
  if [ -n "%{program_suffix}" ]; then
    mv cpp.1 cpp%{program_suffix}.1
  fi
)

%if %{build_debug}
# Don't strip in debug mode
export DONT_STRIP=1
%endif


%clean
#rm -rf $RPM_BUILD_ROOT

%post
update-alternatives --install %{_bindir}/gcc gcc %{_bindir}/gcc-%{version} %{alternative_priority}
[ -e %{_bindir}/gcc ] || update-alternatives --auto gcc

%postun
if [ ! -f %{_bindir}/gcc-%{version} ]; then
  update-alternatives --remove gcc %{_bindir}/gcc-%{version}
fi

%post colorgcc
update-alternatives --install %{_bindir}/gcc gcc %{_bindir}/colorgcc-%{version} %(expr %{alternative_priority} + 10)
update-alternatives --install %{_bindir}/g++ g++ %{_bindir}/colorg++-%{version} %(expr %{alternative_priority} + 10) \
                      --slave %{_bindir}/c++ c++ %{_bindir}/colorg++-%{version}

%postun colorgcc
if [ ! -f %{_bindir}/colorgcc-%{version} ]; then
  update-alternatives --remove gcc %{_bindir}/colorgcc-%{version}
  update-alternatives --remove g++ %{_bindir}/colorg++-%{version}
fi

%if %{build_objc}
%if %mdkversion < 200900
%post objc -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun objc -p /sbin/ldconfig
%endif
%endif

%post cpp
update-alternatives --install %{_bindir}/cpp cpp %{_bindir}/cpp-%{version} %{alternative_priority} --slave /lib/cpp lib_cpp %{_bindir}/cpp-%{version}
# (gb) 2.96-0.59mdk: remove binary if not already alternativeszificated (primary is not a symlink)
[ ! -L %{_bindir}/cpp ] && /bin/rm -f %{_bindir}/cpp
[ -e %{_bindir}/cpp ] || update-alternatives --auto cpp

%postun cpp
if [ ! -f %{_bindir}/cpp-%{version} ]; then
  update-alternatives --remove cpp %{_bindir}/cpp-%{version}
fi

%if %{build_fortran}
%post g77
update-alternatives --install %{_bindir}/g77 g77 %{_bindir}/g77-%{version} %{alternative_priority} --slave %{_bindir}/f77 f77 %{_bindir}/g77-%{version}
# (gb) 2.96-0.59mdk: remove binary if not already alternativeszificated (primary is not a symlink)
[ ! -L %{_bindir}/g77 ] && /bin/rm -f %{_bindir}/g77
[ -e %{_bindir}/g77 ] || update-alternatives --auto g77
%endif

%if %{build_fortran}
%postun g77
if [ ! -f %{_bindir}/g77-%{version} ]; then
  update-alternatives --remove g77 %{_bindir}/g77-%{version}
fi
%endif

%if %{build_java}
%post java
update-alternatives --install %{_bindir}/gcj gcj %{_bindir}/gcj-%version %{alternative_priority}
# (gb) 2.96-0.60mdk: remove binary if not already alternativeszificated (primary is not a symlink)
[ ! -L %{_bindir}/gcj ] && /bin/rm -f %{_bindir}/gcj
[ -e %{_bindir}/gcj ] || update-alternatives --auto gcj

%postun java
if [ ! -f %{_bindir}/gcj-%{version} ]; then
  update-alternatives --remove gcj %{_bindir}/gcj-%{version}
fi
%endif

%if %{build_java}
%if %mdkversion < 200900
%post -n libgcj2.96 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n libgcj2.96 -p /sbin/ldconfig
%endif
%endif

%post c++
update-alternatives --install %{_bindir}/g++ g++ %{_bindir}/g++-%version %{alternative_priority} --slave %{_bindir}/c++ c++ %{_bindir}/g++-%{version}
[ -e %{_bindir}/g++ ] || update-alternatives --auto g++

%postun c++
if [ ! -f %{_bindir}/g++-%{version} ]; then
  update-alternatives --remove g++ %{_bindir}/g++-%{version}
fi

%if %mdkversion < 200900
%post -n libstdc++2.10 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n libstdc++2.10 -p /sbin/ldconfig
%endif

%ifarch %{ix86} alpha
%if %mdkversion < 200900
%post -n libstdc++-compat -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n libstdc++-compat -p /sbin/ldconfig
%endif
%endif

%if %{build_doc}
%post doc
%_install_info gcc.info
%_install_info cpp.info
%_install_info g77.info
%endif

%if %{build_doc}
%preun doc
if [ "$1" = "0" ];then /sbin/install-info %{_infodir}/gcc.info.bz2 --dir=%{_infodir}/dir --remove;fi
%_remove_install_info cpp.info
%_remove_install_info g77.info
%endif

#FILES list
%files
%defattr(-,root,root)
%if %{system_compiler}
%{_prefix}/bin/cc
%endif
%{_prefix}/bin/gcc2-version
%{_prefix}/bin/gcc-%version
%{_prefix}/bin/protoize%{program_suffix}
%{_prefix}/bin/unprotoize%{program_suffix}
%{_prefix}/bin/gcov%{program_suffix}
%{_prefix}/bin/%{_target_platform}-gcc%{program_suffix}
%{_mandir}/man1/gcc%{program_suffix}.1*
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/stddef.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/stdarg.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/varargs.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/float.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/limits.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/stdbool.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/iso646.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/syslimits.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/proto.h
%ifarch ia64
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/ia64intrin.h
%endif
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/README
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/cc1
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/collect2
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/crt*.o
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/libgcc.a
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/SYSCALLS.c.X
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/specs
%doc gcc/README* gcc/*ChangeLog*

%files cpp
%defattr(-,root,root)
/lib/cpp
%ghost %{_bindir}/cpp
%{_prefix}/bin/cpp-%{version}
%{_mandir}/man1/cpp%{program_suffix}.1*
%dir %{_prefix}/lib/gcc-lib/%{gcc_target_platform}
%dir %{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}
%dir %{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/cpp0
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/tradcpp0

%files c++
%defattr(-,root,root)
%{_mandir}/man1/g++%{program_suffix}.1*
%ghost %{_bindir}/c++
%{_bindir}/g++-%{version}
%{_prefix}/bin/c++filt%{program_suffix}
%{_prefix}/bin/%{gcc_target_platform}-c++%{program_suffix}
%{_prefix}/bin/%{gcc_target_platform}-g++%{program_suffix}
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/cc1plus
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/cxxabi.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/exception
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/new
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/new.h
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/typeinfo
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/libstdc++.so
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/libstdc++.a
%doc gcc/cp/ChangeLog*

%files -n libstdc++2.10
%defattr(-,root,root)
%{_prefix}/%{_lib}/libg++.so.2.7*
%{_prefix}/%{_lib}/libstdc++.so.2.*
%{_prefix}/%{_lib}/libstdc++-3-libc*-%{libstdc_version}.so
%{_prefix}/%{_lib}/libstdc++-2-libc*-2.9.0.so
%{_prefix}/%{_lib}/libstdc++-libc*.so.3
%{_prefix}/%{_lib}/libstdc++-libc*.so.2

%files -n libstdc++2.10-devel
%defattr(-,root,root)
%{_prefix}/include/g++-3
%{_prefix}/%{_lib}/libstdc++-3-libc*-%{libstdc_version}.a
%{_prefix}/%{_lib}/libstdc++-libc*.a.3
%doc rpm.doc/libstdc++/*

%if %{build_objc}
%files objc
%defattr(-,root,root)
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/objc
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/cc1obj
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/libobjc.a
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/libobjc.la
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/libobjc.so*
%{_prefix}/%{_lib}/libobjc.so.1*
%doc rpm.doc/objc/*
%doc libobjc/THREADS* libobjc/ChangeLog
%endif

%if %{build_fortran}
%files g77
%defattr(-,root,root)
%ghost %{_bindir}/g77
%ghost %{_bindir}/f77
%{_bindir}/g77-%{version}
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/f771
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/libg2c.a
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/libg2c-pic.a
%{_mandir}/man1/g77%{program_suffix}.1*
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/include/g2c.h
%doc gcc/f/README rpm.doc/g77/*
%endif

%if %{build_java}
%files java
%defattr(-,root,root)
%ghost %{_prefix}/bin/gcj
%{_prefix}/bin/gcj-%{version}
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/jc1
%{_prefix}/lib/gcc-lib/%{gcc_target_platform}/%{version}/jvgenmain
%doc gcc/java/ChangeLog*
%endif

%if %{build_java}
%files -n gcj-tools
%defattr(-,root,root)
%{_bindir}/gij
%{_bindir}/gcjh
%{_bindir}/jcf-dump
%{_bindir}/jv-scan
%{_bindir}/jv-convert
%endif

%if %{build_java}
%files -n libgcj2.96
%defattr(-,root,root)
%doc LICENSE.libffi
%{_libdir}/libgcj.so.1
%{_libdir}/libgcj.so.1.0.0
%{_libdir}/libgcjgc.so.1
%{_libdir}/libgcjgc.so.1.0.1
%{_libdir}/libzgcj.so.0
%{_libdir}/libzgcj.so.0.0.0
#
%dir %{gcc_datadir}
%{gcc_datadir}/libgcj.zip
%endif

%if %{build_java}
%files -n libgcj2.96-devel
%defattr(-,root,root)
%doc README.libffi
#
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/libgcj.a
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/libgcj.so
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/libgcjgc.a
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/libgcjgc.so
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/libgcj.spec
#
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/include/jni.h
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/include/jvmpi.h
%dir %{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/include/gcj
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/include/gcj/*.h
%dir %{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/include/gnu
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/include/gnu/*
%dir %{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/include/java
%{_libdir}/gcc-lib/%{gcc_target_platform}/%{version}/include/java/*
%endif

%if %{build_colorgcc}
%files colorgcc
%defattr (-,root,root)
%doc COPYING.colorgcc CREDITS.colorgcc ChangeLog.colorgcc
%config(noreplace) %{_sysconfdir}/colorgccrc
%{_bindir}/colorgcc-%{version}
%{_bindir}/colorg++-%{version}
%endif

%if %{build_doc}
%files doc
%defattr(-,root,root)
%{_infodir}/gcc*
%{_infodir}/cpp.info*
%if %{build_fortran}
%{_infodir}/g77.info*&
%endif
%endif

%if %{build_pdf_doc}
%files doc-pdf
%defattr(-,root,root)
%doc gcc/doc/cppinternals.pdf
%doc gcc/doc/gcc.pdf
%doc gcc/doc/cpp.pdf
%if %{build_fortran}
%doc gcc/f/g77.pdf
%endif
%endif
